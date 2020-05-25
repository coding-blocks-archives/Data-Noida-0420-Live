from flask import Flask, request, templating, redirect
import json

app = Flask("hh")

@app.route("/")
def say_hello():
    return templating.render_template("first.template")

@app.route("/submit/", methods=["get", "post"])
def submit_karne_wala():

    if request.method.lower() == "get":
        return redirect("/")

    return "We have got request for " + request.form["fname"]

