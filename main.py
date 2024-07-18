# Description     : Code that will impress u ;)
# Author          : G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date            : ur my date uwu
# HEADERS ================================================================

from discord_class import *

from commands_motivate import define_commnands_motivate

# ========================================================================
# NEW CLASS
# ========================================================================

class EunusBot(DiscordBot):

	def define_bot_commands(self)->None:
		define_commnands_motivate(self.bot)

# ========================================================================
# TEST 
# ========================================================================

if __name__ == '__main__':
	bot:EunusBot = EunusBot()
	bot.run()