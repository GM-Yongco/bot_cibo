# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: class that hold all the restart, shutdown, and similar functionalities
# HEADERS ================================================================

# discord stuff
import discord
import discord.ext.commands

# built in stuff
import os
import platform

# for bot tokens and ids and such things that need to be hidden from github
from dotenv import load_dotenv
import os

# ========================================================================
# FUNCTIONS
# ========================================================================

class functionalityRestart():	
	
	will_restart:bool = False

	def restart(self) -> None:
		working_os:str = "unknonwn_os"
		if platform.system() == 'Windows':
			working_os = "windows"
		elif platform.system() == 'Linux':
			working_os = "linux"
		elif platform.system() == 'Darwin':
			working_os = "macos"
		print(f"current working operating system is {working_os}")

		if working_os == "windows":
			os.system("python restart.py")
		elif working_os == "linux":
			os.system("python3 restart.py")

	# ====================================================================

	def define_commands_restart(self, bot:discord.ext.commands.bot.Bot) -> None:

		# ================================================================

		@bot.tree.command(name = "restart", description = "restarts the bot")
		async def restart(interaction: discord.Interaction):			
			function_prefix:str = "command : restart"

			# checking credentials
			if interaction.user.id == int(os.getenv("ID_USER_01")) or interaction.user.id == int(os.getenv("ID_USER_02")):
				print(f"{function_prefix} authorized")
				await interaction.response.send_message("restarting in a few seconds")
				self.will_restart = True
				await bot.close() #goes to the defined on_diconnect event
			else:
				await interaction.response.send_message("you dont have credentials for this bucko")
				print(f"{function_prefix} not authorized")

	# ====================================================================

	def define_events_restart(self, bot:discord.ext.commands.bot.Bot) -> None:
		@bot.event
		async def on_disconnect():
			print(f"{bot.user} has disconnected")

			# so we can still shutdown the bot normally
			if(self.will_restart == True):
				print("initializing restart")
				self.restart()
		