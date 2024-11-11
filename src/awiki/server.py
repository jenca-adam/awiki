#!/usr/bin/env python3
import os
import sys
import glob
import mimetypes
from time import strftime, gmtime
from .page import Page
from bs4 import BeautifulSoup
from werkzeug.utils import safe_join
from flask import (
    Flask,
    request,
    url_for,
    redirect,
    Response,
    abort,
    send_from_directory,
)
from wtforms import Form, validators, TextAreaField, StringField
import yaml
import markdown
from jinja2 import Template, FileSystemLoader, Environment
from . import pagetools
from .taglist import get_taglist_tags, add_tags

# import pagetools,pagetools.search_works
app = Flask(__name__, static_folder=None)
AWIKI_CONFIG = None


def get_template(template_name):
    env = Environment(
        loader=FileSystemLoader(os.path.join(AWIKI_CONFIG.awiki_dir, "templates"))
    )
    return env.get_template(template_name)


@app.route("/view/<string:pagename>")
def view_page(pagename):
    page = Page(pagename, AWIKI_CONFIG)
    if not page.exists:
        return redirect(f"/edit/{pagename}")
    meta, html, md = page.load()
    t = get_template("page.html")
    return t.render(
        meta=meta,
        content=html,
        current=pagename,
        prohibited=["index", "myown", "notmyown", "referee", "students", "DT_garant"],
        strftime=strftime,
        gmtime=gmtime,
        taglist_tags=sorted(get_taglist_tags()),
    )


@app.route("/makebib/<string:pagename>.bib")
def get_bib(pagename):

    page = Page(pagename)
    try:
        meta, html, md = page.load()
    except FileNotFoundError:
        abort(404)
    soup = BeautifulSoup(html, "lxml")
    bibfiles = []
    for anchor in set(soup.find_all("a")):
        href = anchor["href"]
        if "/" not in href:
            for bibfile in glob.glob("pages/%s/*.bib" % href):
                bibfiles.append(open(bibfile).read())
    return Response("".join(bibfiles), mimetype="application/x-bibtex")


@app.route("/view/<string:pagename>/<string:attachment>")
def view_attachment(pagename, attachment):

    mimetype, encoding = mimetypes.guess_type(attachment)
    content = open("pages/%s/%s" % (pagename, attachment), "rb").read()
    return Response(content, mimetype=mimetype)


class EditForm(Form):
    title = StringField("Title", [validators.DataRequired()])
    markdown = TextAreaField("", [validators.DataRequired()])
    commit_message = StringField("Commit message", [validators.DataRequired()])


@app.route("/edit/<string:pagename>", methods=["GET", "POST"])
def edit_page(pagename):

    mdf = Page(pagename)
    try:
        meta, html, md = mdf.load()
    except FileNotFoundError:
        meta, html, md = {"title": ""}, "", ""
    if request.method == "POST":
        form = EditForm(request.form)
        if form.validate():
            meta["title"] = form["title"].data
            md = "\n".join(form["markdown"].data.splitlines())
            mdf.save(meta, md)
            os.system('hg add "%s"' % mdf.md_path)
            os.system(
                'hg commit "%s" -m "%s"' % (mdf.page_name, form["commit_message"].data)
            )
            return redirect("/view/" + pagename)
    else:
        form = EditForm()
        form["title"].process_data(meta["title"])
        form["markdown"].process_data(md)
    t = get_template("edit_page.html")
    return t.render(meta=meta, content=html, form=form)


@app.route("/addpage/<path:id>")
def addpage(id):
    try:
        arxiv_page = next(pagetools.arxiv.arxiv_search(id, "id", 1, AWIKI_CONFIG))
    except StopIteration:
        abort(404)
    page_id = arxiv_page.add()
    return redirect(f"/view/{page_id}")


@app.route("/remove/<string:pagename>", methods=["POST", "GET"])
def remove(pagename):
    if pagename in ["myown", "notmyown", "index"]:
        return redirect("/")
    pwd_rm_t = get_template("pwd_remove.html")
    if request.method == "POST":
        pwdform = request.form
        if pwdform["pwd"] == "alanko":
            pagetools.rm(pagename)
            return redirect("/")

        else:
            return pwd_rm_t.render(error=True, pagename=pagename)
    return pwd_rm_t.render(error=False, pagename=pagename)


@app.route("/search/", methods=["GET", "POST"])
def search():
    search_t = get_template("search.html")
    if request.method == "POST":
        form = request.form
    else:
        form = request.args
    try:
        print(form["query"])
        results = pagetools.arxiv_search(
            form["query"],
            form.get("fields", "all"),
            int(form.get("mr", 100)),
            AWIKI_CONFIG,
        )
        # print(results[0][2])
        return search_t.render(results=results, query=form["query"])
    except KeyError:
        pass
    return search_t.render(results=[[]], query="")


@app.route("/arxiv/<path:id>")
def arxivview(id):
    try:
        page = next(pagetools.arxiv.arxiv_search(id, "id", 1, AWIKI_CONFIG))
    except StopIteration:
        abort(404)
    return get_template("arxiv_page.html").render(page=page)


@app.route("/my_search/", methods=["GET", "POST"])
def ms():
    search_t = get_template("results.html")

    q = request.form.get("q", request.args.get("q", ""))
    tags_string = request.form.get("tags", request.args.get("tags"))
    if tags_string is None:
        tags = []
    else:
        tags = [t.strip() for t in tags_string.split(",")]
    return search_t.render(
        results=list(pagetools.search_pages.search_pages(q, tags, AWIKI_CONFIG)),
        q=q,
        tags=tags_string,
        tags_list=tags,
    )


@app.route("/cite/<string:page>")
def cite(page):
    bibpath = os.path.join("pages", page, "bib.bib")
    try:
        with open(bibpath, "r") as f:
            bibcite = f.read()
    except FileNotFoundError:
        abort(404)
    return Response(bibcite, mimetype="text/plain")


@app.route("/api/set-tags/<string:page>")
def set_tags(page):
    p = Page(page)
    if not p.exists:
        return "no such page"
    tags = request.args.get("tags")
    if tags is None:
        return "no tags"
    metadata, html, markdown = p.load()
    tag_list = [t.strip() for t in tags.split(",")]
    add_tags(tag_list, AWIKI_CONFIG)
    metadata["tags"] = tag_list
    p.save(metadata, markdown)
    return "ok"

@app.route("/api/get-taglist")
def get_taglist():
    return ",".join(sorted(get_taglist_tags()))

@app.route("/static/<path:static_path>")
def static_get(static_path):
    static_dir = safe_join(AWIKI_CONFIG.project_root, AWIKI_CONFIG.awiki_dir, "static")
    file_path = safe_join(static_dir, static_path)
    if not os.path.isfile(file_path):
        return send_from_directory(
            safe_join(AWIKI_CONFIG.project_root, AWIKI_CONFIG.static_dir), static_path
        )
    return send_from_directory(static_dir, static_path)


@app.route("/")
def index():
    return redirect("/view/index")


def run_app(awiki_config, *args, **kwargs):
    global AWIKI_CONFIG
    AWIKI_CONFIG = awiki_config
    app.run(*args, **kwargs)
