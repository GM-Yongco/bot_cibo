# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: A template class to abstact away discord stuff
# HEADERS ================================================================

# discord
import discord
import discord.ext.commands
from discord.ext import commands

# type definitions
from typing import List, Callable

# built in stuff
import json
import inspect

# for bot tokens and ids and such things that need to be hidden from github
from dotenv import load_dotenv
import os

class DiscordBot():
	def __init__(
			self, TOKEN:str = "", 
			LOG_CHANNEL_ID:str = ""
		) -> None:

		# ALL public variables should be here
		self.TOKEN:str = TOKEN
		self.LOG_CHANNEL_ID:str = LOG_CHANNEL_ID
	
		self.functions_initialization:List[Callable] = []
		self.functions_on_ready:List[Callable] = []

		self.LOG_CHANNEL:discord.TextChannel
		self.bot:discord.ext.commands.bot.Bot

	# ====================================================================
	# STANDARD CLASS FUNCTIONS
	# ====================================================================

	def __dict__(self)->dict:
		ret_val:dict = {
			"BOT_NAME" : str(self.bot.user), 
			"LOG_CHANNEL_ID" : str(self.bot.get_channel(int(self.LOG_CHANNEL_ID))),
			"functions_initialization" : [],
			"functions_on_ready":[]
		}

		functions_initialization:List[str] = ret_val["functions_initialization"]
		for functions in self.functions_initialization:
			functions_initialization.append(functions.__name__)
		functions_on_ready:List[str] = ret_val["functions_on_ready"]
		for functions in self.functions_on_ready:
			functions_on_ready.append(functions.__name__)
					
		print(f"function : __dict__ success")
		return ret_val
	
	def __str__(self)->str:
		print(f"function : __str__ success")
		return str(json.dumps(obj = self.__dict__(), indent = 4))

	# ====================================================================
	# CORE CLASS FUNCTIONS
	# ====================================================================

	def get_references(self):
		try:
			load_dotenv()
			self.TOKEN:str = os.getenv("TOKEN")
			self.LOG_CHANNEL_ID:str = os.getenv("ID_CHANNEL_LOG")
			print(f"function : get_references success")
		except Exception as e:
			print(f"function : get_references failed")
			print(e)

	# ====================================================================
	# DISCORD FUNCTIONS
	# ====================================================================

	# DONT REMOVE, this function makes run look pretty
	def define_bot(
			self, 
			intents:discord.Intents = discord.Intents.all(),
			command_prefix:str = "^"
		)->None:
		self.bot = commands.Bot(command_prefix = command_prefix, intents=intents)

	# ====================================================================
	# DISCORD ON_READY FUNCTIONS
	# ====================================================================

	def define_log_channel(self)->None:
		try:
			self.LOG_CHANNEL = self.bot.get_channel(int(self.LOG_CHANNEL_ID))
			print(f"function : define_log_channel success")
		except Exception as e:
			print(f"function : define_log_channel\n{e}")

	async def synch_commands(self)->None:
		# synch the current commands
		synced:List[discord.app_commands.models.AppCommand] = await self.bot.tree.sync()
		print(f"Synched {len(synced)} commands:")
		for index, command in enumerate(synced):
			print(f"{index + 1:3} : {command}")

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

			# these have to go first in the on_ready list
			self.functions_on_ready.insert(0, self.define_log_channel)
			self.functions_on_ready.insert(0, self.synch_commands)
			# use append for the other ones so they come next

			for function in self.functions_on_ready:
				try:
					print(f"initializing_function - {'START':8} : {function.__name__}")
					if inspect.iscoroutinefunction(function):
						await function()
					else:
						function()
					print(f"initializing_function - {'SUCCESS':8} : {function.__name__}")
				except Exception as e:
					print(f"initializing_function - {'ERROR':8} : {function.__name__}\n\t{e}")

			# ready
			message:str = f"{self.bot.user} is now ready"
			await self.LOG_CHANNEL.send(f"```{message}```")
			print(message)
			print("-" * 50)

	# ====================================================================
	# DISCORD COMMANDS
	# ====================================================================

	def define_bot_commands(self) -> None:
		@self.bot.tree.command(name = "get_deets", description = "gets attributes of the bot")
		async def get_deets(interaction: discord.Interaction):
			function_prefix:str = "command : get_deets "
			if interaction.user.id == int(os.getenv("ID_USER_01")):
				print(f"{function_prefix} authorized")
				await interaction.response.send_message(f"```{str(self.__str__())}```")
			else:
				await interaction.response.send_message("you dont have credentials for this bucko")
				print(f"{function_prefix} not authorized")

		@self.bot.tree.command(name = "shutdown", description = "shutsdown the bot")
		async def shutdown(interaction: discord.Interaction):
			function_prefix:str = "command : shutdown "
			if interaction.user.id == int(os.getenv("ID_USER_01")) or interaction.user.id == int(os.getenv("ID_USER_02")):
				print(f"{function_prefix} authorized")
				await interaction.response.send_message("shutdown attempt")
				await self.bot.close()
			else:
				await interaction.response.send_message("you dont have credentials for this bucko")
				print(f"{function_prefix} not authorized")

	# ====================================================================
	# RUN
	# ====================================================================

	def run(self):

		# always need to be done first and the order is important
		self.functions_initialization.insert(0, self.define_bot_commands) 
		self.functions_initialization.insert(0, self.define_bot_events) 
		self.functions_initialization.insert(0, self.define_bot) 
		self.functions_initialization.insert(0, self.get_references) 
		# use append for the other ones so they come next

		# makes sure the functions here are okay before the bot is ready/connected
		for function in self.functions_initialization:
			try:
				function()
				print(f"initializing_function - {'SUCCESS':8} : {function.__name__}")
			except Exception as e:
				print(f"initializing_function - {'ERROR':8} : {function.__name__}\n\t{e}")


		self.bot.run(self.TOKEN)

# ========================================================================
# TESTS
# ========================================================================

if __name__ == '__main__':
	bot:DiscordBot = DiscordBot()
	bot.run()