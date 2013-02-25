#!/usr/bin/env python
#*_* coding=utf8 *_*
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()