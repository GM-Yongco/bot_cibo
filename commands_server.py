# Author			: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date				: ur my date uwu
# Description		: A template class to abstract away discord stuff
# Real Description	: all exterenal server based commands
# HEADERS ================================================================

import discord
import discord.ext.commands

import socket
import requests

# for bot tokens and ids and such things that need to be hidden from github
from dotenv import load_dotenv
import os

# ========================================================================
# FUNCTIONS 
# ========================================================================

def define_commands_server(bot:discord.ext.commands.bot.Bot) -> None:
	load_dotenv()
	USER_ID_01:discord.user = int(os.getenv("ID_USER_01"))
	USER_ID_02:discord.user = int(os.getenv("ID_USER_02"))

	@bot.tree.command(name = "get_server_ip", description = "retrieves the current ip address of my server device, usually for ssh")
	async def get_server_ip(interaction: discord.Interaction):


		function_prefix:str = "command : get_server_ip"

		# checking credentials
		if interaction.user.id == USER_ID_01 or interaction.user.id == USER_ID_02:
			ip_local:str = ":DDD"
			ip_public:str = ":DDD"
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			try:
				s.connect(("8.8.8.8", 80))
				ip_local = s.getsockname()[0]
			except Exception as e:
				ip_local = e 
			finally:
				s.close()

			try:
				ip_public = requests.get("https://api.ipify.org").text
			except Exception as e:
				ip_public = e 

			ret_val:str = f"{'Local':8}IP address: {ip_local}"
			ret_val += "\n" + f"{'Public':8}IP address: {ip_public}"
			
			await interaction.user.send(f"```{ret_val}```")
			function_prefix += " authorized"
			await interaction.response.send_message(f"```addresses sent to dms```")
		else:
			function_prefix += " not authorized"
			await interaction.response.send_message(f"```you dont have credentials for this bucko```")

		print(function_prefix)