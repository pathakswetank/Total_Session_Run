from flask import Flask, request, jsonify, render_template
import util

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Run.html')

@app.route('/player_names', methods=['GET'])
def player_names():
    response = jsonify({
        'PLAYER': util.player_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_run', methods=['GET', 'POST'])
def predict_run():
    PLAYER = request.form['PLAYER']
    Mat = int(request.form['Mat'])
    Inns = int(request.form['Inns'])
    NO = int(request.form['NO'])
    Avg = float(request.form['Avg'])
    HS = int(request.form['HS'])
    BF = int(request.form['BF'])
    SR = float(request.form['SR'])
    HUNDREDS = int(request.form['HUNDREDS'])
    FIFTY = int(request.form['FIFTY'])
    Fours = int(request.form['Fours'])
    Six = int(request.form['Six'])

    response = {
        'estimated_run': util.estimated_run(PLAYER,Mat, Inns, NO, Avg, HS, BF, SR, HUNDREDS, FIFTY,Fours, Six)
    }
    #response.headers.add('Access-Control-Allow-Origin', '*')

    #return response
    return render_template("result.html", response = response)
        

if __name__ == "__main__":
    print("Starting Python Flask Server For Run Prediction...")
    util.load_saved_artifacts()
    app.run()