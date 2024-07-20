# Author			: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date				: ur my date uwu
# Description		: A template class to bstact away discord stuff
# Real Description	: A template class to bstact away discord stuff
# HEADERS ================================================================

import discord
import discord.ext.commands
from discord import app_commands

import time

# ========================================================================
# FUNCTIONS 
# ========================================================================

def define_commands_channels(bot:discord.ext.commands.bot.Bot) -> None:

		# ================================================================

		@bot.tree.command(name = "get_this_channel", description = "gets the currents channels details")
		async def get_this_channel(interaction: discord.Interaction):
			print("command : get_this_channel ")

			message:str = ""

			# interaction.channel_id can return has type int|None
			if(interaction.channel_id != None):
				message += f"\ntype\t: {type(interaction.channel)}"
				message += f"\nname\t: '{str(interaction.channel.name)}'"
				message += f"\nid\t: {str(interaction.channel_id)}"
			else:
				message += f"channel id of channel does not exist"
			
			await interaction.response.send_message(f"{message}")
			
		# ================================================================

		@bot.tree.command(name = "get_channel", description = "gets channel details")
		@app_commands.describe(channel = 'discord native : channel to be deleted')
		async def get_channel(
				interaction: discord.Interaction, 
				channel:discord.TextChannel|discord.VoiceChannel|discord.Thread
			):
			print("command : get_channel ")

			message:str = ""

			# interaction.channel_id can return has type int|None
			if(interaction.channel_id != None):
				message += f"\ntype\t: {type(channel)}"
				message += f"\nname\t: '{str(channel)}'"
				message += f"\nid\t: {str(channel.id)}"
			else:
				message += f"channel id of channel does not exist"
			
			await interaction.response.send_message(f"{message}")

		# ================================================================

		@bot.tree.command(name = "channel_clone_delete", description = "clones channels the command is done in")
		async def channel_clone_delete(interaction: discord.Interaction):
			print("command : channel_clone_delete ")

			delay_seconds:int = 5
			await interaction.response.send_message(f"deletion in {delay_seconds}")

			await interaction.channel.clone()
			for i in range(delay_seconds + 1, 0, -1):
				time.sleep(1)
				await interaction.channel.send(i)
			await interaction.channel.delete()