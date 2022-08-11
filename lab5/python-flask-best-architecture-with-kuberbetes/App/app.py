from flask import Flask
app = Flask(__name__)
import math
import random
import os


@app.route("/")
def hello():
    _ = {
        "version": "v1",
        "computation": str(math.sqrt(random.randint(1, 100000))),
        "testenv": "ok"

    }
    return _


@app.route("/health")
def check():
    return "ok", 200

@app.route("/livez")
def livez():
    return "ok", 200

@app.route("/readyz")
def readyz():
    return "ok", 200

