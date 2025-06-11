# Author			: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Author			: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date				: ur my date uwu
# Description		: A template class to abstract away discord stuff
# Real Description	: all date based commands
# HEADERS ================================================================

import discord
import discord.ext.commands
from discord import app_commands

from utils_log_sleep import CREATE_sleep_log, READ_sleep_log, READ_last_2

# ========================================================================
# FUNCTIONS 
# ========================================================================

def define_commands_sleep(bot:discord.ext.commands.bot.Bot) -> None:

	@bot.tree.command(name = 'log_sleep', description = "logs sleep")
	@app_commands.describe(hour_sleep_start = 'int : 24-hour format')
	@app_commands.describe(hour_sleep_end = 'int : 24-hour format')
	async def log_sleep(
			interaction: discord.Interaction, 
			hour_sleep_start:int, 
			hour_sleep_end:int
		):
		function_prefix:str = "command : log_sleep"
		print(f"{function_prefix}")
		CREATE_sleep_log(hour_sleep_start=hour_sleep_start, hour_sleep_end=hour_sleep_end)
		await interaction.response.send_message("ok")

	@bot.tree.command(name = 'get_sleep_stats', description = "gets the entire sleep database")
	async def get_stats(interaction: discord.Interaction):
		function_prefix:str = "command : get_sleep_stats"
		print(f"{function_prefix}")
		await interaction.response.send_message(f"```{READ_sleep_log()}```")
	
	@bot.tree.command(name = 'get_sleep_status', description = "gets the last 2 sleep entries and decides if we can sleep late or not")
	async def get_status(interaction: discord.Interaction):
		# this is whatll tell me if im allowed to sleep late tonight
		function_prefix:str = "command : get_sleep_status"
		print(f"{function_prefix}")
		await interaction.response.send_message(f"```{READ_last_2()}```")