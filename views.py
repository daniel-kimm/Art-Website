from flask import Blueprint, render_template

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/theme/")
def theme():
    return render_template("theme.html")

@views.route("/artworks/")
def artworks():
    return render_template("artworks.html")

@views.route("/awards/")
def awards():
    return render_template("awards.html")

@views.route("/exhibitions/")
def exhibitions():
    return render_template("exhibitions.html")