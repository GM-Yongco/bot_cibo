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

	def check_os():
		ret_val:str = "unknonwn_os"
		if platform.system() == 'Windows':
			ret_val = "windows"
		elif platform.system() == 'Linux':
			ret_val = "linux"
		elif platform.system() == 'Darwin':
			ret_val = "macos"
		print(f"current working operating system is {ret_val}")
		return ret_val

	def restart(self) -> None:
		print(f"starting in:")
		wait_seconds = 10
		for i in range(wait_seconds, 0, -1):
			print(i)
			time.sleep(1)

		operating_system:str = self.check_os()
		if operating_system == "Windows":
			os.system("python main.py")
		elif operating_system == "Linux":
			os.system("python3 main.py")

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