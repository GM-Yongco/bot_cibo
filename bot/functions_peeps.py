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

def peeps_post(
		name_first:str = "", 
		name_last:str = "",
		birth_year:int = 2001,
		birth_month:int = 1,
		birth_date:int = 1
	):
	request:req.Response = req.post(
		url = "http://127.0.0.1:5000/people",
		timeout=2,
		json = {
			'name_first' : name_first,
			'name_last' : name_last,
			'birth_date' : birth_date,
			'birth_month' : birth_month,
			'birth_year' : birth_year
		}
	)
	ret_val: str = f"{'command : post_peeps':25}"
	return ret_val

def peeps_get_birthdays() -> str:
	request:req.Response = req.get(
		url = "http://127.0.0.1:5000/people/birthdays",
		timeout=2
	)
	ret_val:str = ""
	for row in request.json():
		ret_val += f"{row[0]:15}{row[1]:15}|{row[2]}\n"
	ret_val.strip("\n")
	return ret_val
