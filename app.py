#Import flask
from flask import Flask, render_template, request, url_for,flash
from flask_sqlalchemy import SQLAlchemy
from config import db_password
import numpy as np
import pickle as pk
import os

#Load App and Database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:db_password@127.0.0.1:5432/Heart_Ache'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
sql = SQLAlchemy(app)

#Load the model
model = pk.load(open('model.pkl','rb'))

#<img src="../Images/heart_pill.jpg" alt="headerpic" width = "100%" height="500">
#Set up app route
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    #they clicked the nav bar
    return render_template("index.html")


@app.route("/states")
def states():
    return render_template("states.html")

@app.route("/checkyourheart")
def checkheart():
    #heart = sql.db.Heart.find_one()
    return render_template("checkheart.html")

@app.route("/results",methods= ['POST'])
def results():
    # Get the data from the POST request.
    if request.method == "POST":
        
        #data = request.get_json(force=True)
        ageInput = int(request.form['ageInput'])
        beatsInput = int(request.form["beatsInput"])
        cholesterol = int(request.form["cholesterolInput"])
        fastBS = int(request.form["fastBS"])
        maxHeart = int(request.form["maxHeart"])
        oldPeak = float(request.form["oldPeak"])

        data = [ageInput, beatsInput, cholesterol, fastBS, maxHeart, oldPeak]

        print(ageInput, beatsInput)

        #data = float(request.form['exp'])
        #print("Data", model.predict([[data]]))
        # Make prediction using model loaded from disk as per the data.
        prediction = model.predict([data])

        print(prediction)
        result = ""
        if(prediction[0] == 1):
            result="You Go Breaking Your Heart(you should not break your heart)!"
        else:
            result = "Go eat fast food today you're fine!"

        # Take the first value of prediction
        #output = prediction[0]

        return render_template("results.html", result = result) #, output=output, exp=data)

#Define other code for use
#def ValuePredictor(to_predict_list):
    #to_predict = np.array(to_predict_list).reshape(1,4)
    #loaded_model = pk.load()

if __name__ == "__main__":
   app.run()