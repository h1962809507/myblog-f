from flask import render_template

from . import about_blu


@about_blu.route("/about")
def about():
    return render_template("blog/about.html")


@about_blu.route("/contact")
def contact():
    return render_template("blog/contact.html")
