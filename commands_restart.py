# Description		: Code that will impress u ;)
# Author			: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date				: ur my date uwu
# Real Description	: for restarting the bot when necessary
# HEADERS ================================================================

# discord stuff
import discord
import discord.ext.commands

# built in
import os
import time

# ========================================================================
# FUNCTIONS 
# ========================================================================

def restart_file(file_name:str = "main.py", wait_seconds:int = 30) -> None:
	start_python_program(file_name = file_name, wait_seconds = wait_seconds)
	exit(0)

# ========================================================================

def define_commands_restart(bot:discord.ext.commands.bot.Bot) -> None:

	@bot.tree.command(name = "restart", description = "will give you a random link of motivation")
	async def restart(interaction: discord.Interaction):
		print("command : restart")
		await bot.close()

# ========================================================================

def start_python_program(file_name:str = "main.py", wait_seconds:int = 60)->None:
	try:
		print(f"starting {file_name} in:")
		for i in range(wait_seconds, 0, -1):
			print(i)
			time.sleep(1)

		os.system(f"python {file_name}")
	except Exception as e:
		start_python_program(file_name = "function_restart.py", wait_seconds = wait_seconds*2)
	exit(0)

# ========================================================================
# RUNNER 
# ========================================================================

if __name__ == '__main__':
	start_python_program()