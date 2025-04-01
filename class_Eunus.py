# Description     : Code that will impress u ;)
# Author          : G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date            : ur my date uwu
# HEADERS ================================================================

import asyncio

from class_discord import *

from util_restart import functionalityRestart
from util_routine import bot_task_cycle
from utils_misc import section
from commands_motivate import define_commands_motivate
from commands_channels import define_commands_channels
from commands_dates import define_commands_dates
from commands_server import define_commands_server

# ========================================================================
# NEW CLASS
# ========================================================================

class EunusBot(DiscordBot):
	
	# ====================================================================
	# ADDITIONAL CLASS VARIABLES
	# ====================================================================
	functionality_restart:functionalityRestart = functionalityRestart()

	# ====================================================================
	# ADDITIONAL CLASS FUNCTIONALITY
	# ====================================================================

	def define_more_bot_events(self) -> None:
		@self.bot.event
		async def on_ready():
			self.define_log_channel() 

			synced:List[discord.app_commands.models.AppCommand] = await self.bot.tree.sync()
			print(f"Synched {len(synced)} commands:")
			for index, command in enumerate(synced):
				print(f"{index + 1:3} : {command}")

			# announcing ones Awakening
			message:str = f"{self.bot.user} is now ready"
			section(message)
			await self.LOG_CHANNEL.send(f"```{message}```")

			# timed tasks for bot at startup
			bot_log = asyncio.create_task(bot_task_cycle(channel = self.LOG_CHANNEL, interval_seconds = 30))
			await asyncio.gather(bot_log)
		
		self.functionality_restart.define_events_restart(self.bot)

	# ====================================================================

	def define_more_bot_commands(self)->None:
		self.functionality_restart.define_commands_restart(self.bot, self.user_ids[0])

		define_commands_dates(self.bot)
		define_commands_motivate(self.bot)

		define_commands_server(self.bot, self.user_ids[0])
		define_commands_channels(self.bot, self.user_ids[0])
		
