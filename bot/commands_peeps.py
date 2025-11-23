# Author			: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Author			: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date				: ur my date uwu
# Description		: A template class to abstract away discord stuff
# Real Description	: all sleep based commands
# HEADERS ================================================================

import discord
import discord.ext.commands
from discord import app_commands

from functions_peeps import peeps_get_birthdays, peeps_post
# ========================================================================
# FUNCTIONS 
# ========================================================================

def define_commands_peeps(bot:discord.ext.commands.bot.Bot) -> None:

	@bot.tree.command(name = 'peeps_post', description = "logs sleep (use 24 hour format)")
	@app_commands.describe(name_first = 'int : 24-hour format')
	@app_commands.describe(name_last = 'int : 24-hour format')
	@app_commands.describe(birth_year = 'int : 24-hour format')
	@app_commands.describe(birth_month = 'int : 24-hour format')
	@app_commands.describe(birth_date = 'int : 24-hour format')
	async def command_peeps_post(
			interaction: discord.Interaction, 
			name_first:str = "", 
			name_last:str = "",
			birth_year:int = 2001,
			birth_month:int = 1,
			birth_date:int = 1
		):
		function_prefix:str = "command : peeps_create"
		print(f"{function_prefix}")

		peeps_post(
			name_first = name_first,
			name_last = name_last,
			birth_year = birth_year,
			birth_month = birth_month,
			birth_date = birth_date
		)
		
		await interaction.response.send_message(f"```{function_prefix}```")

	@bot.tree.command(name = 'peeps_get_birthdays', description = "gets near-past and near-future birthdays")
	async def command_peeps_get_birthdays(interaction: discord.Interaction):
		function_prefix:str = "command : peeps_get_birthdays"
		print(f"{function_prefix}")

		await interaction.response.send_message(f"```{peeps_get_birthdays()}```")
	