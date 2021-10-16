from datetime import datetime
from flask import Flask, render_template ,request
import pickle
from flask.wrappers import Request
import numpy as np

app = Flask(__name__)

modle=pickle.load(open('modle.pkl','rb'))
@app.route("/", methods=['POST','GET'])
def hello_world():
    return render_template('index.html')

@app.route("/predict-tesla",methods=['POST','GET'])
def predict_tesla():
    data=[[request.form['high'],request.form['low'],request.form['open'],request.form['volume']]]
    predictions=modle.predict(data)
    predictions=predictions.reshape(-1)[0]
    return render_template('tesla.html',pred='{}'.format(predictions))

@app.route("/tesla")
def tesla():
    return render_template('tesla.html')

@app.route("/google")
def google():
    return render_template('google.html')

if __name__=="__main__":
    app.run(debug=True)