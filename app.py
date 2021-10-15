from datetime import datetime
from flask import Flask, render_template ,request
import pickle
from flask.wrappers import Request
import numpy as np

app = Flask(__name__)

modle=pickle.load(open('modle.pkl','rb'))
@app.route('/', methods=['POST','GET'])
def hello_world():
    return render_template('index.html')

@app.route("/predict",methods=['POST','GET'])
def predict():
    data=[[request.form['high'],request.form['low'],request.form['open'],request.form['volume']]]
    predictions=modle.predict(data)
    predictions=predictions.reshape(-1)[0]
    return render_template('index.html',pred='{}'.format(predictions))

if __name__=="__main__":
    app.run(debug=True)