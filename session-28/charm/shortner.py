from flask import Flask, request, templating, redirect

app = Flask("hh")

shortof = {"cb" : "https://codingblocks.com/"}

@app.route("/")
def say_hello():
    return templating.render_template("first.template")

@app.route("/<short>/")
def data(short):
    return redirect(shortof[short])

