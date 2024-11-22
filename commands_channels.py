# Author			: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date				: ur my date uwu
# Description		: A template class to abstract away discord stuff
# Real Description	: all channel based commands
# HEADERS ================================================================

import discord
import discord.ext.commands

# ========================================================================
# FUNCTIONS 
# ========================================================================

def define_commands_channels(bot:discord.ext.commands.bot.Bot, authorized_user_id:str) -> None:

	@bot.tree.command(name = "channel_clone_delete", description = "clones channels the command is done in")
	async def channel_clone_delete(interaction: discord.Interaction):

		function_prefix:str = "command : channel_clone_delete"

		# checking credentials
		if interaction.user.id == int(authorized_user_id):
			await interaction.channel.clone()
			await interaction.channel.delete()
			print(f"{function_prefix} authorized")
		else:
			await interaction.response.send_message("you dont have credentials for this bucko")
			print(f"{function_prefix} not authorized")