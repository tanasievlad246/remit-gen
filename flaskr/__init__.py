import os
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import itertools

def find_sum(arr):
	"""This function returns the sum of all elements in a list """
	sum = 0
	for i in range(0, len(arr)):
   		sum = sum + float(arr[i]);
	return sum

def combinations(varr, search_for):
	"""This function prints out all the combinations of numbers in a list that equal a certain sum when added """
	for i in range(len(varr)):
		for j in itertools.combinations(varr, i):
			if find_sum(j) == float(search_for):
			    #returns array of combinations
				return j


	return "None found"

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    def hello():
        return render_template('index.html')
        
    @app.route('/process', methods=['POST'])
    def process_info():
        
        payment = request.form['payment']
        invoices = request.form['invoices'].split()
        
        remit = combinations(invoices, payment)
        
        if request.method == "POST":
            result = {
                "payment": request.form['payment'],
                "remit": remit
            }
        else:
            result = {}
  
        return render_template('/remit.html', result = result)

    return app
