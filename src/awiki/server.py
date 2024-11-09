#!/usr/bin/env python3
import os
import sys
import glob
import mimetypes
from .page import Page
from bs4 import BeautifulSoup
from stat import S_ISREG, ST_CTIME, ST_MODE
from werkzeug.utils import safe_join
from flask import Flask, request, url_for, redirect, Response, abort, send_from_directory
from wtforms import Form, validators, TextAreaField, StringField
import yaml
import markdown
from jinja2 import Template, FileSystemLoader, Environment
from . import pagetools
# import pagetools,pagetools.search_works
app = Flask(__name__, static_folder=None)
AWIKI_CONFIG = None
def get_template(template_name):
    env = Environment(loader=FileSystemLoader(os.path.join(AWIKI_CONFIG.awiki_dir,"templates")))
    return env.get_template(template_name)
@app.route("/view/<string:pagename>")
def view_page(pagename):
    print(pagename)
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
    )


@app.route("/makebib/<string:pagename>.bib")
def get_bib(pagename):

    page = Page(pagename)
    try:
        meta, html, md =page.load()
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
        meta,html,md={"title":""},"",""
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
def auth(id):
    global addpageform
    id = id.split("?")[0]
    beh = pagetools.add(id, **request.args)
    print(beh)
    if beh and beh["status"] == "error":
        return get_template("file_exists.html").render(
            msg=beh["response"]["message"],
            type=beh["response"]["type"],
            cleanup=beh["cleanup"],
            traceback=beh["tb"],
        )
    return redirect("/")


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
    search_t =get_template("search.html")
    if request.method == "POST":
        form = request.form
    else:
        form = request.args
    try:
        print(form["query"])
        results = pagetools.arxiv_search(form["query"], form.get("fields", "all"), int(form.get("mr",100)), AWIKI_CONFIG)
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
    search_t =get_template("results.html")

    if request.method == "POST":
        f = request.form
        q = f["q"]
        return search_t.render(results=list(pagetools.search_pages.search_pages(q, AWIKI_CONFIG)), q=q)
    return abort(405)

@app.route("/cite/<string:page>")
def cite(page):
    bibpath = os.path.join("pages", page, "bib.bib")
    try:
        with open(bibpath, "r") as f:
            bibcite = f.read()
    except FileNotFoundError:
        abort(404)
    return Response(bibcite, mimetype="text/plain")

@app.route("/static/<path:static_path>")
def static_get(static_path):
    static_dir = safe_join(AWIKI_CONFIG.project_root, AWIKI_CONFIG.awiki_dir, "static")
    file_path = safe_join(static_dir, static_path)
    if not os.path.isfile(file_path):
        return send_from_directory(safe_join(AWIKI_CONFIG.project_root,AWIKI_CONFIG.static_dir),static_path)
    return send_from_directory(static_dir, static_path)
@app.route("/")
def index():
    return redirect("/view/index")

def run_app(awiki_config, *args, **kwargs):
    global AWIKI_CONFIG
    AWIKI_CONFIG = awiki_config
    app.run(*args, **kwargs)
