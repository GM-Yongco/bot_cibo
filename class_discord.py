# Author			: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date				: ur my date uwu
# Description		: A template class to bstact away discord stuff
# HEADERS ================================================================

# discord
import discord
import discord.ext.commands
from discord.ext import commands
from discord import app_commands

# type definitions
import io
from typing import List, Callable

# built in stuff
import os
import json

class DiscordBot():
	def __init__(
			self, TOKEN:str = "", 
			LOG_CHANNEL_ID:str = ""
		) -> None:

		self.TOKEN:str = TOKEN
		self.LOG_CHANNEL_ID:str = LOG_CHANNEL_ID
		self.additional_functions:List[Callable] = []
	
		self.LOG_CHANNEL:discord.TextChannel
		self.bot:discord.ext.commands.bot.Bot

	def __dict__(self)->dict:
		ret_val:dict = {
			"BOT_NAME" : str(self.bot.user), 
			"LOG_CHANNEL_ID" : str(self.bot.get_channel(int(self.LOG_CHANNEL_ID))),
			"additional_functions" : []
		}

		additional_functions:List[str] = ret_val["additional_functions"]
		for functions in self.additional_functions:
			additional_functions.append(functions.__name__)
		print(f"function : __dict__ success")

		return ret_val
	
	def __str__(self)->str:
		print(f"function : __str__ success")
		return str(json.dumps(obj = self.__dict__(), indent = 4))

	# ====================================================================
	# CORE CLASS FUNCTIONS
	# ====================================================================

	def get_references(self, path:str = "REFERENCES/bot_info.json"):
		json_details:dict = {"error":"error"}
		try:
			file:io.TextIOWrapper = open(path, "r")
			json_details:dict = json.load(file)
			file.close()

			self.TOKEN:str = json_details["bot_tokens"]["Eunus"]
			self.LOG_CHANNEL_ID:str = json_details["log_channel_id"]
			print(f"function : get_references success")
		except Exception as e:
			print(f"function : get_references failed")
			print(e)

	def add_functions(self, func:Callable):
		self.additional_functions.append(func)
		print(f"function : add_functions success")

	# ====================================================================
	# DISCORD FUNCTIONS
	# ====================================================================

	def define_bot(
			self, 
			intents:discord.Intents = discord.Intents.all(),
			command_prefix:str = "^"
		)->None:
		self.bot = commands.Bot(command_prefix = command_prefix, intents=intents)

	def define_log_channel(self)->None:
		try:
			self.LOG_CHANNEL = self.bot.get_channel(int(self.LOG_CHANNEL_ID))
			print(f"function : define_log_channel success")
		except Exception as e:
			print(f"function : define_log_channel\n{e}")

	# ====================================================================
	# DISCORD EVENTS
	# ====================================================================

	def define_bot_events(self) -> None:
		@self.bot.event
		async def on_connect():
			print(f"{self.bot.user} is now connected")
		
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

	# ====================================================================
	# DISCORD COMMANDS
	# ====================================================================

	def define_bot_commands(self) -> None:
		@self.bot.tree.command(name = "greet_me", description = "greets you plus more")
		@app_commands.describe(message = "str : additional greeting")
		async def greet_me(interaction: discord.Interaction, message:str = ""):
			print("command : greet_me ")
			try:
				await interaction.response.send_message(f"get greeted :P - {message}")
			except Exception as e:
				await interaction.response.send_message(f"{e}")

		
		@self.bot.tree.command(name = "give_deets", description = "will give you a random link of motivation")
		async def give_deets(interaction: discord.Interaction):
			print("command : give_deets ")
			try:
				await interaction.response.send_message(str(self.__str__()))
			except Exception as e:
				await interaction.response.send_message(f"{e}")

		print("default bot commands")

	# ====================================================================
	# RUN
	# ====================================================================

	def run(self):

		# always need to be done first and the order is important
		self.get_references()
		self.define_bot()

		# can be overwritten
		self.add_functions(self.define_bot_events)
		self.add_functions(self.define_bot_commands)

		# make sure the functions here are okay before the bot is ready/connected
		for index, functions in enumerate(self.additional_functions):
			try:
				functions()
			except Exception as e:
				print(f"{index} :\n{e}")

		
		try:
			self.bot.run(self.TOKEN)
		except Exception as e:
			print('='*50)
			print(e)
			print('='*50)
			os.system("python function_restart.py")
			exit()

# ========================================================================
# TESTS
# ========================================================================

if __name__ == '__main__':
	bot:DiscordBot = DiscordBot()
	bot.run()