from flask import render_template, url_for, redirect, request, jsonify

from config import app
from models import Test


@app.route('/home')
def home():
    """
    This function redirects the root page to the home route.

    :return: render template called home.html
    """

    return render_template("home.html")

@app.route('/')
def root():
    """
    This function redirects the root page to the home route.
    :return: redirect to home
    """
    return redirect(url_for("home"))

def

@app.route('/test_get', methods=['GET'])
def test_get():
    '''
    This route is an example route that handles a get request and handles it appropriately
    :return:
    '''
    if request.method == 'GET':
        data = {arg: request.args.get(arg) for arg in request.args}
        print(data['name'])
        response = jsonify({'response': str(Test.query.filter_by(name=data['name']).all())})
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add('Access-Control-Allow-Headers', "*")
        response.headers.add('Access-Control-Allow-Methods', "*")
        print(response.headers)

        return response
