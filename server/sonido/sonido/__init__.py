from flask import Flask, request, render_template, url_for, redirect, request
import urllib2
from pymongo import MongoClient
import database


app = Flask(__name__)
client = MongoClient("mongodb://sshi:1@troup.mongohq.com:10070/sonido")
db = client.sonido
collection = db.mapdata

@app.route("/")
def home():
    blub="blublublub"
    return render_template("index.html", blub=blub)

@app.route("/mangos", methods=['GET','POST'])
def mangos():
    params = None
    if request.method == 'GET':
        params = request.args
    if request.method == 'POST':
        return render_template("error.html")
    doc = {"long":float(params.get("long")), 
           "lat":float(params.get("lat")), 
           "amp":float(params.get("amp")), 
           "freq":float(params.get("freq")),
           "author":"shan"}
    collection.insert(doc)
    blub=collection.find_one({"lat":"8"})["lat"]
    #blub=params.get("long")+params.get("lat")+params.get("amp")+params.get("freq")    
    return render_template("index.html", blub=blub)

@app.route("/map")
def mapprev():
    #heatlist = returnAll()
    return render_template("map.html")#, heatlist=heatlist)
    
if __name__ == "__main__":
    app.run()
