from wsgiref import simple_server
from flask import Flask, request, render_template
from werkzeug.utils import redirect
#import pickle
#import json
#import numpy as np
"""
*****************************************************************************
*
* filename:       main.py
* version:        1.0
* author:         HARISH
* creation date:  05-MAY-2020
*
* change history:
*
* who             when           version  change (include bug# if apply)
* ----------      -----------    -------  ------------------------------
* HARISH          20-JAN-2021    1.0      initial creation
*
*
* description:    flask main file to run application
*
****************************************************************************
"""

app = Flask(__name__)


@app.route('/')
def index_page():
    """
    * method: index_page
    * description: method to call index html page
    * return: index.html
    *
    * who             when           version  change (include bug# if apply)
    * ----------      -----------    -------  ------------------------------
    * HARISH          20-JAN-2021    1.0      initial creation
    *
    * Parameters
    *   None
    """
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    """
    * method: predict
    * description: method to predict
    * return: index.html
    *
    * who             when           version  change (include bug# if apply)
    * ----------      -----------    -------  ------------------------------
    * HARISH          20-JAN-2021    1.0      initial creation
    *
    * Parameters
    *   None
    """
    if request.method == 'POST':
        Selection = request.form["Select Table"]
        #output = get_predict_profit(r_d_expenses, administration_expenses, marketing_expenses, state)
        if Selection == 'fifth':
            return redirect("https://fifth-table-shaanu.herokuapp.com/")
        if Selection == 'four':
            return redirect("https://fourth-table-for-shaanu.herokuapp.com/")
        elif Selection == 'three':
            return redirect("https://third-table-for-shaanu.herokuapp.com/")
        elif Selection == 'two':
            return redirect("https://second-table-for-shaanu.herokuapp.com/")
        elif Selection == 'one':
            return redirect("https://first-table-for-shaanu.herokuapp.com/")


    #return redirect("https://fourth-table-for-shaanu.herokuapp.com/")


if __name__ == "__main__":
    #app.run(debug=True)
    host = '0.0.0.0'
    port = 5000
    httpd = simple_server.make_server(host, port, app)
    httpd.serve_forever()
