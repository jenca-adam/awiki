#!/usr/bin/env python3
import os
import sys
import glob
import mimetypes
from .page import Page
from bs4 import BeautifulSoup
from stat import S_ISREG, ST_CTIME, ST_MODE

from flask import Flask, request, url_for, redirect, Response, abort
from wtforms import Form, validators, TextAreaField, StringField
import yaml
import markdown
from jinja2 import Template, FileSystemLoader, Environment

# import pagetools,pagetools.search_works
app = Flask(__name__)




@app.route("/view/<string:pagename>")
def view_page(pagename):
    page = Page(pagename)
    if not page.exists:
        return redirect(f"/edit/{pagename}")
    meta, html = page.load()
    env = Environment(loader=FileSystemLoader("templates"))
    t = env.get_template("page.html")
    return t.render(
        meta=meta,
        content=html,
        current=pagename,
        prohibited=["index", "myown", "notmyown", "referee", "students", "DT_garant"],
    )


@app.route("/makebib/<string:pagename>.bib")
def get_bib(pagename):

    mdf = MarkdownFile(pagename)
    try:
        mdf.load()
    except FileNotFoundError:
        abort(404)
    soup = BeautifulSoup(mdf.html, "lxml")
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

    mdf = MarkdownFile(pagename)
    try:
        mdf.load()
    except FileNotFoundError:
        pass
    env = Environment(loader=FileSystemLoader("templates"))
    if request.method == "POST":
        form = EditForm(request.form)
        if form.validate():
            mdf.meta["title"] = form["title"].data
            mdf.markdown = "\n".join(form["markdown"].data.splitlines())
            mdf.save()
            os.system('hg add "%s"' % mdf.filename)
            os.system(
                'hg commit "%s" -m "%s"' % (mdf.filename, form["commit_message"].data)
            )
            return redirect("/view/" + pagename)
    else:
        form = EditForm()
        form["title"].process_data(mdf.meta["title"])
        form["markdown"].process_data(mdf.markdown)
    t = env.get_template("edit_page.html")
    return t.render(meta=mdf.meta, content=mdf.html, form=form)


@app.route("/addpage/<path:id>")
def auth(id):
    global addpageform
    id = id.split("?")[0]
    env = Environment(loader=FileSystemLoader("templates"))
    beh = pagetools.add(id, **request.args)
    print(beh)
    if beh and beh["status"] == "error":
        return env.get_template("file_exists.html").render(
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
    env = Environment(loader=FileSystemLoader("templates"))
    pwd_rm_t = env.get_template("pwd_remove.html")
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
    env = Environment(loader=FileSystemLoader("templates"))
    search_t = env.get_template("search.html")
    if request.method == "POST":
        form = request.form
    else:
        form = request.args
    try:
        print(form["query"])
        results = pagetools.search_arxiv(form["query"], form.get("fields", "all"))
        # print(results[0][2])
        return search_t.render(results=results, query=form["query"])
    except KeyError:
        pass
    return search_t.render(results=[[]], query="")


@app.route("/arxiv/<path:id>")
def arxivview(id):
    page = pagetools.arxiv.ArXivPage(id)
    return page.html()


@app.route("/my_search/", methods=["GET", "POST"])
def ms():
    env = Environment(loader=FileSystemLoader("templates"))
    search_t = env.get_template("results.html")

    if request.method == "POST":
        f = request.form
        q = f["q"]
        return search_t.render(results=pagetools.search_works.search(q), q=q)


@app.route("/cite/<string:page>")
def cite(page):
    bibpath = os.path.join("pages", page, "bib.bib")
    try:
        with open(bibpath, "r") as f:
            bibcite = f.read()
    except FileNotFoundError:
        abort(404)
    return Response(bibcite, mimetype="text/plain")


@app.route("/")
def index():
    return redirect("/view/index")


def run_app(awiki_config, *args, **kwargs):
    global AWIKI_CONFIG
    AWIKI_CONFIG = awiki_config
    app.run(*args, **kwargs)
