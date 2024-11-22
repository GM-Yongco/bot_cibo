# Description     : Code that will impress u ;)
# Author          : G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date            : ur my date uwu
# HEADERS ================================================================

# discord stuff
import discord
import discord.ext.commands
from discord import app_commands


import os
import time
import platform

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

	# ========================================================================

	def define_commands_restart(self, bot:discord.ext.commands.bot.Bot, authorized_user_id:str) -> None:
		
		@bot.tree.command(name = "restart", description = "restarts the bot")
		async def restart(interaction: discord.Interaction):

			
			function_prefix:str = "command : restart"

			# checking credentials
			if interaction.user.id == int(authorized_user_id):
				print(f"{function_prefix} authorized")
				await interaction.response.send_message("restarting in a few seconds")
				self.will_restart = True
				await bot.close() #goes to the defined on_diconnect event
			else:
				await interaction.response.send_message("you dont have credentials for this bucko")
				print(f"{function_prefix} not authorized")

	# ========================================================================

	def define_events_restart(self, bot:discord.ext.commands.bot.Bot) -> None:
		@bot.event
		async def on_disconnect():
			print(f"{bot.user} has disconnected")

			# so we can still shutdown the bot normally
			if(self.will_restart == True):
				print("initializing restart")
				self.restart()