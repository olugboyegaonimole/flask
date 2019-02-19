# blog application


import os
from flask import Flask




# 2.3 create application factory

def create_app(test_config=None): 

	# create and configure the app

	app = Flask(__name__, instance_relative_config=True) 

				# "A Flask application is an instance of the Flask class". 
				# "An instance of the Flask class will be our WSGI application". 
				# The above mean that 'app' - a Flask application - is a WSGI application. Is 'app' a WSGI application or a web app. Please confirm.
				# Is __name__ the name of the current Python module or the name of the application's module/package? Please confirm.
				# The app needs to know where it’s located in order to set up paths
				# __name__ is a convenient way to tell the app where it’s located


	app.config.from_mapping(
		SECRET_KEY='dev',
		DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
	)


	
	# load configuration

	if test_config is None:

		# load the instance config when not testing

		app.config.from_pyfile('config.py', silent=True)


	else:

		# load the test config if passed in

		app.config.from_mapping(test_config)




	# ensure the instance folder exists

	try:
		os.makedirs(app.instance_path)
	
	except OSError:
		pass




	# below are some of my view functions

	# the route() decorator tells Flask what URL should trigger what function


	@app.route('/cartoon')# a URI (API endpoint); a unique URL that represents an object or collection of objects
	def cartoon():
		return 'bananaman!'


	@app.route('/')# a URI (API endpoint); a unique URL that represents an object or collection of objects
	def index():
		return 'hey!'



	@app.route('/greeting')# a URI (API endpoint); a unique URL that represents an object or collection of objects
	def greeting():
		return 'e kaaro oooooooooooooooooooooooooooooo!!!!!!!!!!!!!'



	@app.route('/name')# a URI (API endpoint); a unique URL that represents an object or collection of objects
	def name():
		return 'G-boy!'



	@app.route('/age')# a URI (API endpoint); a unique URL that represents an object or collection of objects
	def age():
		return '40!'



	@app.route('/address')# a URI (API endpoint); a unique URL that represents an object or collection of objects
	def address():
		return 'here!'



	@app.route('/comedy')# a URI (API endpoint); a unique URL that represents an object or collection of objects
	def comedy():
		return 'tom and jerry!'



	@app.route('/mum')# a URI (API endpoint); a unique URL that represents an object or collection of objects
	def mum():
		return 'my mum!'




	# 3.3 register close_db and init_db_command with your application (part 2 - import and call this function from the factory)
	
	from . import db
	db.init_app(app)		# register the commands written to create the tables 



	from . import auth
    app.register_blueprint(auth.bp) # register the authentication blueprint



	return app