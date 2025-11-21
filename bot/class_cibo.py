# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: essence of what makes cibo is
#	basically all the compiled features of cibo
# HEADERS ================================================================

import asyncio

from class_discord import *
from util_misc import section

from functions_routines import bot_task_cycle
from util_restart import functionalityRestart
from commands_motivate import define_commands_motivate
from commands_channels import define_commands_channels
from commands_server import define_commands_server
from commands_dates import define_commands_dates
from commands_sleep import define_commands_sleep

# ========================================================================
# NEW CLASS
# ========================================================================

class Cibo(DiscordBot):
	
	# ====================================================================
	# ADDITIONAL CLASS VARIABLES
	# ====================================================================
	functionality_restart:functionalityRestart = functionalityRestart()

	# ====================================================================
	# ADDITIONAL CLASS FUNCTIONALITY
	# ====================================================================

	async def define_more_on_ready_functions(self)->None:
		bot_log:asyncio.Task = asyncio.create_task(
			bot_task_cycle(self.bot)
			)
		await asyncio.gather(bot_log)

	# ====================================================================

	def define_more_bot_events(self) -> None:
		self.functionality_restart.define_events_restart(self.bot)

	# ====================================================================

	def define_more_bot_commands(self)->None:
		define_commands_dates(self.bot)
		define_commands_sleep(self.bot)
		define_commands_motivate(self.bot)

		define_commands_server(self.bot)
		define_commands_channels(self.bot)
		
		self.functionality_restart.define_commands_restart(self.bot)

# ========================================================================
# TEST 
# ========================================================================

if __name__ == '__main__':
	bot:Cibo = Cibo()
	bot.functions_initialization.append(bot.define_more_bot_commands)
	bot.functions_initialization.append(bot.define_more_bot_events)
	bot.functions_on_ready.append(bot.define_more_on_ready_functions)
	bot.run()