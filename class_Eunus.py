# Description     : Code that will impress u ;)
# Author          : G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date            : ur my date uwu
# HEADERS ================================================================

from class_discord import *

from util_restart import functionalityRestart
from utils import section
from functions_daily import bot_time_log
from commands_motivate import define_commands_motivate
from commands_channels import define_commands_channels

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
			# bot_log = asyncio.create_task(bot_time_log(channel = self.LOG_CHANNEL, interval_seconds = 300))
			# await asyncio.gather(bot_log)
		
		self.functionality_restart.define_events_restart(self.bot)

	# ====================================================================

	def define_more_bot_commands(self)->None:
		define_commands_motivate(self.bot)
		define_commands_channels(self.bot, self.user_ids[0])
		self.functionality_restart.define_commands_restart(self.bot, self.user_ids[0])
