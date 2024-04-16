# Description     : Code that will impress u ;)
# Author          : G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date            : ur my date uwu

# ========================================================================
# IMOPRTS
# ========================================================================
import discord
from discord.ext import commands
from discord import app_commands

from random import randint as ri

# ========================================================================
# FUNCTIONS
# ========================================================================

async def send_interaction_message(interaction: discord.Interaction, message:str):
	await interaction.response.send_message(f"{message}")

# ========================================================================
# MAIN
# ========================================================================

def run_discord_bot():

	# ====================================================================
	# INITIALIZATION
	# ====================================================================
	TOKEN = open("REFERENCES/TOKEN_VESSEL.txt", "r").read()

	intents = discord.Intents.all()
	bot = commands.Bot(command_prefix='', intents=intents)

	# ====================================================================
	# DEFAULT EVENTS
	# ====================================================================
	@bot.event
	async def on_ready():
		print(f'{bot.user} is now running')
		synced = await bot.tree.sync()
		print(f"Synched {len(synced)} commands")

	@bot.event														
	async def on_message(message):
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
		message = ["aloha", "greetings, adverturer", "salutations"]
		await interaction.response.send_message(message[ri(0, len(message) - 1)])

	# ====================================================================
	
	@bot.tree.command(name = "motivate_me", description = "will give you a random link of motivation")
	async def motivate_me(interaction: discord.Interaction):
		print("motivate_me command")

		messages = []
		file_ptr = open("REFERENCES/motivation.txt", "r")
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