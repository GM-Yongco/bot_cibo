# Author			: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Author			: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date				: ur my date uwu
# Description		: A template class to abstract away discord stuff
# Real Description	: abstract away some of the requests
# HEADERS ================================================================

import requests as req

# ========================================================================
# FUNCTIONS 
# ========================================================================

def sleep_post(
		hour_sleep_start:int, 
		hour_sleep_end:int
	):
	request:req.Response = req.post(
		url = "http://127.0.0.1:5125/sleep_log",
		timeout=2,
		json = {
			'sleep_start' : hour_sleep_start,
			'sleep_end' : hour_sleep_end
		}
	)
	ret_val: str = f"{'command : log_sleep':25}"
	if request.json()["status"] == "500":
		ret_val += "failed"
	else:
		ret_val += "success"

	return ret_val

def sleep_get_logs() -> str:
	request:req.Response = req.get(
		url = "http://127.0.0.1:5125/sleep_log",
		timeout=2
	)
	ret_val: str = "\n".join(", ".join(map(str, row)) for row in request.json()) 
	return ret_val

def sleep_get_status() -> str:
	request:req.Response = req.get(
		url = "http://127.0.0.1:5125/sleep_log",
		timeout=2
	)
	rows = request.json()
	message:str = f"you slept at {rows[0][1]:02} on last sleep entry"
	message += f"\nyou slept at {rows[1][1]:02} on second to the last sleep entry"
	if (rows[0][1] > 0 and rows[0][1] <12) or (rows[1][1] > 0 and rows[1][1] <12) :
		message += "\nyou didnt sleep early in both days, no sleep late tonight"
		pass
	else:
		message += "\nyou slept early the past 2 days so you get to play league late :DDD"

	return message
