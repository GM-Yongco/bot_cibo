# Description     : Code that will impress u ;)
# Author          : G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date            : ur my date uwu
# Real Description: Scheduled execution for bot
# HEADERS ================================================================

# discord
import discord
import discord.ext.commands

# time stuff
import asyncio
from datetime import datetime,time, timedelta

# GLOBAL VARIABLES =======================================================

MINUTE_SECONDS:int 	= 60
HOUR_SECONDS:int 	= MINUTE_SECONDS * 60
DAY_SECONDS:int 	= HOUR_SECONDS * 24

# ========================================================================
# FUNCTIONS MISC
# ========================================================================

def section(section_name:str = "SECTION") -> None:
	section_name = f"\n {section_name} {'-' * (40 - len(section_name))}\n"
	print(section_name)

# ========================================================================
# FUNCTIONS 
# ========================================================================

def nearest_divisible_int_more(num:int = 420, divisible_by = 69) -> int:
	return num + (divisible_by - (num % divisible_by))

def raw_seconds(time:time = datetime.now().time()):
	return (time.hour * 3600) + (time.minute * 60) + time.second

def interval_synchronize(interval_seconds:int = MINUTE_SECONDS) -> int:
	return interval_seconds - (raw_seconds()%interval_seconds)

async def bot_time_log(channel:discord.TextChannel, interval_seconds:int = MINUTE_SECONDS):
	print("function : bot_time_log started")
	
	cycle_num:int = 0

	# sleeps so that the log update will match the intervals
	# ex: if interval is 5 mins, log will happen in a minute divisible by 5
	await asyncio.sleep(interval_synchronize(interval_seconds = interval_seconds))

	while True:
		up_time: str = f"{'up time':20}:{cycle_num}"
		currrent_time : str = f"{'cycle number':20}:{datetime.now().strftime('%Y|%d|%M - %H:%M:%S')}"
		await channel.send(f"```I am still alive\n{up_time}\n{currrent_time}```")

		if cycle_num%10 == 0:
			await asyncio.sleep(interval_synchronize(interval_seconds = interval_seconds))
		else:
			await asyncio.sleep(interval_seconds)
		cycle_num += 1

# ========================================================================
# TEST 
# ========================================================================

if __name__ == '__main__':
	section("START")
	
	print(nearest_divisible_int_more(num=69, divisible_by=420))
	print(nearest_divisible_int_more(num=420, divisible_by=69))
	print(nearest_divisible_int_more(num=43, divisible_by=5))

	print(datetime.now().time())
	seconds = raw_seconds()
	print(raw_seconds())
	print(f"raw = {int(seconds/HOUR_SECONDS)}:{int((seconds%HOUR_SECONDS)/MINUTE_SECONDS)}:{seconds%MINUTE_SECONDS}")
	interval_seconds:int = 300
	print(interval_seconds - (raw_seconds()%interval_seconds))

	section("END")
