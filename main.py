# Description     : Code that will impress u ;)
# Author          : G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date            : ur my date uwu
# HEADERS ================================================================

from discord_class import *
from random import randint as ri

# ========================================================================
# NEW CLASS
# ========================================================================

class EunusBot(DiscordBot):

	def define_bot_commands(self)->None:

		# ================================================================

		@self.bot.tree.command(name = "motivate_me", description = "will give you a random link of motivation")
		async def motivate_me(interaction: discord.Interaction):
			print("command : motivate_me")

			messages:list = []
			file_ptr:io.TextIOWrapper = open("REFERENCES/motivation.txt", "r")
			for line in file_ptr:
				if line[0] not in ['#', '\n']:									#if not a line that is empty or comment in the text file
					messages.append((line.strip('\n')).replace(rf"\n", "\n")) 	#formatting; removing the end line \n and turing the raw text"\n" to new line characters
			file_ptr.close()

			await interaction.response.send_message(messages[ri(0, len(messages) - 1)])
		
		# ====================================================================

		@self.bot.tree.command(name = "motivate_add", description = "adds to the list of motivations")
		@app_commands.describe(message = 'message')
		async def motivate_add(interaction: discord.Interaction, message:str):
			print("command : motivate_add")
			
			file_ptr = open("REFERENCES/motivation.txt", "a")
			file_ptr.write(f"\n{message}")
			file_ptr.close()

			await interaction.response.send_message("done")

# ========================================================================
# TEST 
# ========================================================================

if __name__ == '__main__':
	bot:EunusBot = EunusBot()
	bot.run()