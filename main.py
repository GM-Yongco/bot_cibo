# Author			: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date				: ur my date uwu
# Description		: main discord bot loop
# HEADERS ================================================================
import discord
from discord.ext import commands
from discord import app_commands

import io

import asyncio
from random import randint as ri

import misc_functions as mf

# ========================================================================
# GLOBAL
# ========================================================================

bot_info:dict = mf.reference_read()

# ========================================================================
# DISCORD FUNCTIONS
# ========================================================================
async def channel_message(
		bot:discord.Client,
		channel_id:int = bot_info["log_channel"],
		user_id:int = bot_info["users"]["Veee"],
		message:str = "default message"
	) -> None:
	
	text_channel:discord.channel.TextChannel = bot.get_channel(channel_id)
	user:discord.User = await bot.fetch_user(user_id)

	message = f"{user.mention} \n {message}"
	await text_channel.send(message)
	print("message sent")

# ========================================================================
# MAIN
# ========================================================================

def run_discord_bot():

	# ====================================================================
	# INITIALIZATION
	# ====================================================================
	TOKEN = bot_info["bot_tokens"]["Eunus"]

	intents:discord.Intents = discord.Intents.all()
	bot:discord.Client = commands.Bot(command_prefix='', intents=intents)

	# ====================================================================
	# DEFAULT EVENTS
	# ====================================================================
	@bot.event
	async def on_ready():
		print(f'{bot.user} is now running')
		synced:list = await bot.tree.sync()
		
		print(f"Synched {len(synced)} commands")
		for index, command in enumerate(synced):
			print(f"{index + 1:3} : {command}")

		#on ready tasks

		await channel_message(bot = bot)

		# status_check:asyncio.Task = asyncio.create_task(mf.time_loop(delay_seconds=4))
		# await asyncio.gather(status_check)
	
	# ====================================================================
	
	@bot.event	
	async def on_message(message:discord.message.Message):
		if(message.author != bot.user):
			username        = str(message.author)	
			channel         = str(message.channel)
			content         = str(message.content)

			print(f"\n\n'{username}':\nsaid: {content}\n in channel: '{channel}'")

	# ====================================================================
	# CUSTOM COMMANDS
	# ====================================================================
	
	@bot.tree.command(name = "add_three_numbers", description = "adds 3 numbers with a message")
	@app_commands.describe(n1 = 'n1')
	@app_commands.describe(n2 = 'n2')
	@app_commands.describe(n3 = 'n3')
	@app_commands.describe(lil_message = 'string')
	async def add_three_numbers(interaction: discord.Interaction, n1:int, n2:int, n3:int, lil_message:str):
		print("add_three_numbers command")
		await interaction.response.send_message(f"{n1 + n2 + n3}:{lil_message}")

	# ====================================================================

	@bot.tree.command(name = "greet_me", description = "will greet you based on the number you give")
	async def greet_me(interaction: discord.Interaction, input:int):
		print("greet_me command")
		message:list = ["aloha", "greetings, adverturer", "salutations"]
		await interaction.response.send_message(message[ri(0, len(message) - 1)])

	# ====================================================================
	
	@bot.tree.command(name = "motivate_me", description = "will give you a random link of motivation")
	async def motivate_me(interaction: discord.Interaction):
		print("motivate_me command")

		messages:list = []
		file_ptr:io.TextIOWrapper = open("REFERENCES/motivation.txt", "r")
		for line in file_ptr:
			if line[0] not in ['#', '\n']:									#if not line that is empty or comment in the text file
				messages.append((line.strip('\n')).replace(rf"\n", "\n")) 	#formatting; removing the end line \n and turing the raw text"\n" to new line characters
		file_ptr.close()

		await interaction.response.send_message(messages[ri(0, len(messages) - 1)])
	
	# ====================================================================

	@bot.tree.command(name = "motivate_add", description = "adds to the list of motivations")
	@app_commands.describe(message = 'message')
	async def motivate_add(interaction: discord.Interaction, message:str):
		print("motivate_add command")
		
		file_ptr = open("REFERENCES/motivation.txt", "a")
		file_ptr.write(f"\n{message}")
		file_ptr.close()

		await interaction.response.send_message("done")
	
		
	# ====================================================================
	# RUN BOT
	# ====================================================================
	bot.run(TOKEN)

if __name__ == '__main__':
	run_discord_bot()