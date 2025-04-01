# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: the supposed sheduling program of the bot
# HEADERS ================================================================

# discord
import discord
import discord.ext.commands

# time stuff
import asyncio
import datetime

from utils_misc import section

# GLOBAL VARIABLES =======================================================

MINUTE_SECONDS:int 	= 60
HOUR_SECONDS:int 	= MINUTE_SECONDS * 60
DAY_SECONDS:int 	= HOUR_SECONDS * 24

# ========================================================================
# FUNCTIONS 
# ========================================================================

def cycle_message_date_format(
		date_type:str = "year", 
		previous_date_value:int = -1,
		current_date_value:int = 1)->str:
	return f"\n\t{date_type:10} update {previous_date_value:05} -> {current_date_value:05}"

async def bot_task_cycle(channel:discord.TextChannel, interval_seconds:int = MINUTE_SECONDS):
	cycle_count:int = 0

	previous_year:int = -1
	previous_month:int = -1
	previous_week:int = -1
	previous_day:int = -1
	previous_hour:int = -1
	previous_minute:int = -1

	while(True):
		time_now:datetime.datetime = datetime.datetime.now()
		cycle_message:str = f"cycle: {cycle_count}"

		# ==================================================
		# put the tasks on the given date type

		if time_now.year != previous_year:
			cycle_message += cycle_message_date_format("year", previous_year, time_now.year)
			previous_year = time_now.year

		if time_now.month != previous_month:
			cycle_message += cycle_message_date_format("month", previous_month, time_now.month)
			previous_month = time_now.month

		if time_now.isocalendar()[1] != previous_week:
			cycle_message += cycle_message_date_format("week", previous_week, time_now.isocalendar()[1])
			previous_week = time_now.isocalendar()[1]

		if time_now.day != previous_day:
			cycle_message += cycle_message_date_format("day", previous_day, time_now.day)
			previous_day = time_now.day

		if time_now.hour != previous_hour:
			cycle_message += cycle_message_date_format("hour", previous_hour, time_now.hour)
			previous_hour = time_now.hour
			await channel.send(f"```I am alive\n{cycle_message}```")

		if time_now.minute != previous_minute:
			cycle_message += cycle_message_date_format("minute", previous_minute, time_now.minute)
			previous_minute = time_now.minute

		# ==================================================

		print(cycle_message)
		cycle_count += 1
		await asyncio.sleep(interval_seconds)

# ========================================================================
# TEST 
# ========================================================================

if __name__ == '__main__':
	section("START")
	
	section("END")
