# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: Code that will impress u ;)
# ========================================================================
# HEADERS
# ========================================================================

from flask import Flask, request as f_req, jsonify

from sleep_db import DBSleep

# ========================================================================
# FUNCTIONS 
# ========================================================================

def define_routes_sleep(app:Flask):
	db_access:DBSleep = DBSleep(db_file_name = "sleep_log.db")
	db_access.INIT_table_sleep_log()

	@app.route("/sleep_log", methods=["GET"])
	def GET_sleep_log():
		return jsonify(db_access.GET_sleep_log())

	# Route with URL parameter
	@app.route("/sleep_log_head", methods=["GET"])
	def GET_sleep_log_head():
		return jsonify(db_access.GET_sleep_log_last_2())

	# POST route for addition
	@app.route("/sleep_log", methods=["POST"])
	def POST_sleep_log():
		ret_val = 200
		try:
			data:dict = f_req.get_json()

			sleep_start = data.get("sleep_start", 0)
			sleep_end = data.get("sleep_end", 0)

			db_access.CREATE_sleep_log(
				hour_sleep_end=sleep_end, 
				hour_sleep_start=sleep_start
			)
		except Exception as e:
			ret_val = 500
		return jsonify({"status": str(ret_val)})

# ========================================================================
# MAIN 
# ========================================================================