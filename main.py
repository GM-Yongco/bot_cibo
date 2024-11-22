# Description     : Code that will impress u ;)
# Author          : G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date            : ur my date uwu
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