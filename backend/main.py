# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: Creating an api for the database
# ========================================================================
# HEADERS
# ========================================================================

from flask import Flask
from sleep_routes import define_routes_sleep

# ========================================================================
# CLASS
# ========================================================================

class API():
	def __init__(self):
		self.flask_object:Flask = Flask(__name__)
	
	def run(self):
		define_routes_sleep(app = self.flask_object)
		self.flask_object.run(
			debug=True, 
			host='0.0.0.0', 
			port=5125
		)

# Run server
if __name__ == "__main__":
	backend:API = API()
	backend.run()
