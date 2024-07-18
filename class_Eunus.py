# Description     : Code that will impress u ;)
# Author          : G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date            : ur my date uwu
# HEADERS ================================================================

from class_discord import *

import asyncio
from functions_daily import bot_time_log
from commands_motivate import define_commnands_motivate

# ========================================================================
# NEW CLASS
# ========================================================================

class EunusBot(DiscordBot):
	def define_bot_events(self) -> None:
		@self.bot.event
		async def on_connect():
			print(f"{self.bot.user} is now connected")

		@self.bot.event
		async def on_ready():
			# get channel can only be used after the bot has been ready
			self.define_log_channel() 

			# synch the current commands
			synced:List[discord.app_commands.models.AppCommand] = await self.bot.tree.sync()
			print(f"Synched {len(synced)} commands:")
			for index, command in enumerate(synced):
				print(f"{index + 1:3} : {command}")

			# ready
			print(f"{self.bot.user} is now ready")
			print("-" * 50)

			# tasks for bot after setup
			bot_log = asyncio.create_task(bot_time_log(channel = self.LOG_CHANNEL, interval_seconds = 10))
			await asyncio.gather(bot_log)

	# ====================================================================

	def define_bot_commands(self)->None:
		define_commnands_motivate(self.bot)

# ========================================================================
# TEST 
# ========================================================================

if __name__ == '__main__':
	bot:EunusBot = EunusBot()
	bot.run()