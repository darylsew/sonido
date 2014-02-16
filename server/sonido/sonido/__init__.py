from flask import Flask, request, render_template, url_for, redirect, request
import urllib2
from pymongo import MongoClient
app = Flask(__name__)
client = MongoClient("mongodb://sshi:1@troup.mongohq.com:10070/sonido")

@app.route("/")
def hello():
    blub="asdfasdf"
    return render_template("index.html", blub=blub)

if __name__ == "__main__":
    app.run()
