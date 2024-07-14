# Author			: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date				: ur my date uwu
# Description		: functions of the bot to prevent clutter
# HEADERS ================================================================
import io
import json

import discord

import asyncio
from datetime import datetime
from typing import Callable

# ========================================================================
# FUNCTIONS
# ========================================================================

def reference_read(path:str = "REFERENCES/bot_info.json") -> dict:
	json_details:dict = {"error":"error"}
	try:
		file:io.TextIOWrapper = open(path, "r")
		json_details = json.load(file)
		file.close()
	except Exception as e:
		print(e)

	return json_details

def default_func()->None:
	print("Ahoy")

async def time_loop(func:Callable = default_func, delay_seconds:int = 5, ):
	while True:
		func()
		print(datetime.now().strftime(rf"%Y|%b|%d - %H:%M:%S"))
		await asyncio.sleep(delay_seconds)

