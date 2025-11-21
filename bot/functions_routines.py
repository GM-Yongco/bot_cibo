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

from util_misc import log_write
from utils_log_sleep import READ_last_2

# for bot tokens and ids and such things that need to be hidden from github
from dotenv import load_dotenv
import os

# ========================================================================
# FUNCTIONS 
# ========================================================================

def cycle_message_date_format(
		date_type:str = "year", 
		previous_date_value:int = -1,
		current_date_value:int = 1)->str:
	return f"\n\t{date_type:10} update {previous_date_value:05} -> {current_date_value:05}"

# ========================================================================

async def bot_task_cycle(bot:discord.ext.commands.bot.Bot):
	interval_seconds:int = 30

	load_dotenv()
	LOG_CHANEL:discord.TextChannel = bot.get_channel(int(os.getenv("ID_CHANNEL_LOG")))
	USER_01:discord.User = bot.get_user(int(os.getenv("ID_USER_01")))
	USER_02:discord.User = bot.get_user(int(os.getenv("ID_USER_02")))

	cycle_count:int = 0

	# time updates
	previous_year:int = -1
	previous_month:int = -1
	previous_week:int = -1
	previous_day:int = -1
	previous_hour:int = -1
	previous_minute:int = -1

	# task updates
	previous_day_daily_report:int = -1

	while(True):
		time_now:datetime.datetime = datetime.datetime.now()
		cycle_message:str = f"cycle: {cycle_count:06}"

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
			await LOG_CHANEL.send(f"```I am alive: {time_now.strftime('%Y-%m-%d %H:%M:%S')}```")

		if time_now.minute != previous_minute:
			cycle_message += cycle_message_date_format("minute", previous_minute, time_now.minute)
			previous_minute = time_now.minute

			if (time_now.hour >= 10) and (time_now.day != previous_day_daily_report):
				previous_day_daily_report = time_now.day

				message:str = ""
				message += "GOOD MORNING\nnew day, new you, lets get on the grind.\nremember you are human and have both material and social needs to work on"
				message += f"\n\n{READ_last_2()}"
				await USER_01.send(f"```{message}```")
				await USER_02.send(f"```{message}```")

		# ==================================================

		log_write(file_name="logs_routines.csv", category="cycle", details=cycle_message)
		cycle_count += 1
		await asyncio.sleep(interval_seconds)