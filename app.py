from flask import Flask, render_template, request
from datetime import datetime
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('random_forest_classification_model.pkl','rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Principal = int(request.form['Principal'])
        Terms=int(request.form['Terms'])
        Effective_date=request.form['Effective_date']
        date_object = datetime.strptime(Effective_date, '%Y-%m-%d').date()
        Day_of_week = date_object.weekday()
        Weekend=0
        if(Day_of_week>3):
            Weekend=1
        Age= int(request.form['Age'])
        Gender=request.form['Gender']
        if(Gender=='Male'):
            Gender=0
        else:
            Gender=1
        Education_level=request.form['Education_level']
        Bachelor = HSBelow = College = 0
        if(Education_level=='Bachelor'):
            Bachelor=1
        elif(Education_level=='HSBelow'):
            HSBelow=1
        else:
            College=1
        if((Principal > 1000) or (Terms > 30) or (Age<18)):
            return render_template('index.html',incorrect_fields="Sorry some fields haven't been filled in correctly")
        else:
            prediction=model.predict([[Principal,Terms,Age,Gender,Weekend, Bachelor, HSBelow, College]])
            output=prediction[0]
            return render_template('result.html',prediction=output)
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)