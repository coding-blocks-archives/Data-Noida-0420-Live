from flask import Flask, request, templating
import json

app = Flask("hh")

@app.route("/")
def say_hello():
    return templating.render_template("first.template")

