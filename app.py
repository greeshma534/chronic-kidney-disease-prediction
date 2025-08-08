import os
import MySQLdb
from flask import Flask, session, url_for, redirect, render_template, request, abort, flash
 
 
from werkzeug.utils import secure_filename
import numpy as np
import joblib
import numpy as np
from flask import Flask, redirect, url_for, request, render_template
import pandas as pd
from sklearn.preprocessing import LabelEncoder

from database import *
from joblib import load

from pathlib import Path
import pickle


app = Flask(__name__)
app.secret_key='detection'
 
app.config['UPLOAD_FOLDER'] = 'static/uploads'
 
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/registera")
def registera():
    return render_template("register.html")

@app.route("/logina")
def logina():
    return render_template("login.html")

@app.route("/predicta")
def predicta():
    return render_template("predict.html")


@app.route("/predictionoutputa")
def predictoutputa():
    return render_template("predictionoutput.html")


@app.route("/register",methods=['POST','GET'])
def signup():
    if request.method=='POST':
        username=request.form['username']
        email=request.form['email']
        password=request.form['password']
        status = user_reg(username,email,password)
        if status == 1:
            return render_template("/login.html")
        else:
            return render_template("/register.html",m1="failed")        
    

@app.route("/login",methods=['POST','GET'])
def login():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        status = user_loginact(request.form['username'], request.form['password'])
        print(status)
        if status == 1:                                      
            return render_template("/menu.html", m1="sucess")
        else:
            return render_template("/login.html", m1="Login Failed")
             
 
    
 


app.static_folder = 'static'

    
# @app.route("/")
# def home():
#     return render_template("index.html")

@app.route('/logouta')
def logout():
    # Clear the session data
    session.clear()
    return redirect(url_for('logina'))

@app.route('/predicta2')
def predicta2():
    # Clear the session data
    session.clear()
    return render_template('/p2 copy.html')


@app.route('/m')
def m():
    # Clear the session data
    session.clear()
    return render_template('/menu.html')   




@app.route('/predict2', methods=['POST'])
def predict2():
    #para=request.form['para']
    #BCN = load('theworking2.joblib')

    # Input data (in the same order as the features)
    #input_data = para.split()
    best_model = joblib.load('bcn.pkl')
    # Convert '?' values to NaN
    #input_data = [np.nan if val == '?' else val for val in input_data]
    
    if request.method == 'POST':
        age = float(request.form['age'])
        bp = float(request.form['bp'])
        sg = float(request.form['sg'])
        al = float(request.form['al'])
        su = float(request.form['su'])
        rbc = float(request.form['rbc'])
        pc = float(request.form['pc'])
        pcc = float(request.form['pcc'])
        ba = float(request.form['ba'])
        bgr = float(request.form['bgr'])
        bu = float(request.form['bu'])
        sc = float(request.form['sc'])
        sod = float(request.form['sod'])
        pot = float(request.form['pot'])
        hemo = float(request.form['hemo'])
        wc = float(request.form['wc'])
        rc = float(request.form['rc'])
        htn = float(request.form['htn'])
        dm = float(request.form['dm'])
        cad = float(request.form['cad'])
        appet = float(request.form['appet'])
        pe = float(request.form['pe'])
        ane = float(request.form['ane'])
        
        

        values = np.array([[age, bp, sg, al, su, rbc, pc, pcc, ba, bgr, bu, sc, sod, pot, hemo, wc, rc, htn, dm, cad, appet, pe, ane]])
        prediction = best_model.predict(values)
    # Make predictions
    
        return render_template("result.html",prediction=prediction)





if __name__ == "__main__":
    app.run(debug=True)
