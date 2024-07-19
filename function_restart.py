# Description		: Code that will impress u ;)
# Author			: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date				: ur my date uwu
# Real Description	: for restarting the bot when necessary
# HEADERS ================================================================

import os
import time

# ========================================================================
# FUNCTIONS 
# ========================================================================

def start_python_program(file_name:str = "main.py", wait_seconds:int = 60)->None:
	try:
		print(f"starting {file_name} in:")
		for i in range(wait_seconds, 0, -1):
			print(i)
			time.sleep(1)

		os.system(f"python {file_name}")
	except Exception as e:
		start_python_program(file_name = "function_restart.py", wait_seconds = 30)
	exit(0)

# ========================================================================
# RUNNER 
# ========================================================================

if __name__ == '__main__':
	start_python_program()