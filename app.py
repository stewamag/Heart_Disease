#Import flask
from flask import Flask, render_template, request, url_for,flash
from flask_sqlalchemy import SQLAlchemy
from config import db_password
import os

#Load App and Database
app = Flask(_name_)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:db_password@127.0.0.1:5432/Heart_Ache3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
sql = SQLAlchemy(app)


#Set up app route
@app.route("/")
def index():
    heart = sql.db.Heart.find_one()
    return render_template("index.html", heart=Heart_Ache)

@app.route("/")
def states():
    return render_template("states.html")




if __name__ == "__main__":
   app.run()