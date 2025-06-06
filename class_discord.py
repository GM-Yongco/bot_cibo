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
import io
from typing import List, Callable

# built in stuff
import json

class DiscordBot():
	def __init__(
			self, TOKEN:str = "", 
			LOG_CHANNEL_ID:str = ""
		) -> None:

		# ALL public variables should be here
		self.TOKEN:str = TOKEN
		self.LOG_CHANNEL_ID:str = LOG_CHANNEL_ID

		self.user_ids:List[str] = []
	
		self.initialization_functions:List[Callable] = []

		self.LOG_CHANNEL:discord.TextChannel
		self.bot:discord.ext.commands.bot.Bot

	# ====================================================================
	# STANDARD CLASS FUNCTIONS
	# ====================================================================

	def __dict__(self)->dict:
		ret_val:dict = {
			"BOT_NAME" : str(self.bot.user), 
			"LOG_CHANNEL_ID" : str(self.bot.get_channel(int(self.LOG_CHANNEL_ID))),
			"initialization_functions" : [],
			"user_ids" : []
		}

		initialization_functions:List[str] = ret_val["initialization_functions"]
		for functions in self.initialization_functions:
			initialization_functions.append(functions.__name__)
		user_ids:List[str] = ret_val["user_ids"]
		for users in self.user_ids:
			user_ids.append(users)
			
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

			self.user_ids.append(json_details["user_ids"]["Veee"])
			self.user_ids.append(json_details["user_ids"]["ViDeinde"])

			print(f"function : get_references success")
		except Exception as e:
			print(f"function : get_references failed")
			print(e)

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

	# ====================================================================
	# DISCORD COMMANDS
	# ====================================================================

	def define_bot_commands(self) -> None:
		@self.bot.tree.command(name = "get_deets", description = "gives attributes of the bot")
		async def get_deets(interaction: discord.Interaction):
			print("command : get_deets")
			try:
				await interaction.response.send_message(str(self.__str__()))
			except Exception as e:
				await interaction.response.send_message(f"{e}")

	# ====================================================================
	# RUN
	# ====================================================================

	def run(self):

		# always need to be done first and the order is important
		self.get_references()
		self.define_bot()

		# order shouldnt matter here
		self.define_bot_events()
		self.define_bot_commands()

		# makes sure the functions here are okay before the bot is ready/connected
		for functions in self.initialization_functions:
			try:
				functions()
				print(f"initializing_function - {'SUCCESS':8} : {functions.__name__}")
			except Exception as e:
				print(f"initializing_function - {'ERROR':8} : {functions.__name__}\n\t{e}")

		self.bot.run(self.TOKEN)

# ========================================================================
# TESTS
# ========================================================================

if __name__ == '__main__':
	bot:DiscordBot = DiscordBot()
	bot.run()