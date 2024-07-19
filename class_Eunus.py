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
	def define_new_bot_events(self) -> None:
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
			bot_log = asyncio.create_task(bot_time_log(channel = self.LOG_CHANNEL, interval_seconds = 300))
			await asyncio.gather(bot_log)

		@self.bot.event
		async def on_disconnect():
			print(f"{self.bot.user} has disconnected, initializing restart")
			os.system("python function_restart.py")
			exit()

	# ====================================================================

	def define_bot_commands(self)->None:
		define_commnands_motivate(self.bot)

	# ====================================================================

	def run(self):

		# always need to be done first and the order is important
		self.get_references()
		self.define_bot()

		# can be overwritten
		self.add_functions(self.define_bot_events)
		# self.add_functions(self.define_bot_commands)

		# make sure the functions here are okay before the bot is ready/connected
		for functions in self.additional_functions:
			try:
				functions()
				print(f"additional_functions : {functions.__name__} - success")
			except Exception as e:
				print(f"additional_functions : {functions.__name__} - ERROR\n\t{e}")

		self.bot.run(self.TOKEN)

		
		try:
			self.bot.run(self.TOKEN)
		except Exception as e:
			print('='*50)
			print(e)
			print('='*50)
			os.system("python function_restart.py")
			exit()

# ========================================================================
# TEST 
# ========================================================================

if __name__ == '__main__':
	bot:EunusBot = EunusBot()
	bot.add_functions(bot.define_new_bot_events)
	bot.run()