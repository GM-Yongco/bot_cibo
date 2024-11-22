# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: main file that runs the bot and appends to initialization functions
# HEADERS ================================================================

from class_Eunus import EunusBot

# ========================================================================
# TEST 
# ========================================================================

if __name__ == '__main__':
	bot:EunusBot = EunusBot()
	bot.initialization_functions.append(bot.define_more_bot_commands)
	bot.initialization_functions.append(bot.define_more_bot_events)
	bot.run()