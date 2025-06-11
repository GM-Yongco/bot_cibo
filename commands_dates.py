# Author			: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date				: ur my date uwu
# Description		: A template class to abstract away discord stuff
# Real Description	: all date based commands
# HEADERS ================================================================

import discord
import discord.ext.commands

import datetime

# ========================================================================
# FUNCTIONS 
# ========================================================================

def define_commands_dates(bot:discord.ext.commands.bot.Bot) -> None:

	@bot.tree.command(name = "get_week", description = "retrieves the current date information in iso format")
	async def get_week(interaction: discord.Interaction):

		function_prefix:str = "command : get_week"
		print(f"{function_prefix}")

		iso_stuff:datetime._IsoCalendarDate = datetime.datetime.now().isocalendar()
		
		ret_val:str = f"{'year':10}: {iso_stuff.year}"
		ret_val += "\n" + f"{'week':10}: {iso_stuff.week}"
		ret_val += "\n" + f"{'week_day':10}: {iso_stuff.weekday}"

		await interaction.response.send_message(f"```{ret_val}```")