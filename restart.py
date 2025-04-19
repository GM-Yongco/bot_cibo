# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: seprate/independent program that gets called to restart the bot
# HEADERS ================================================================

import os
import time
import platform

print(f"starting in:")
wait_seconds = 5
for i in range(wait_seconds, 0, -1):
    print(i)
    time.sleep(1)

working_os:str = "unknonwn_os"
if platform.system() == 'Windows':
    working_os = "windows"
elif platform.system() == 'Linux':
    working_os = "linux"
elif platform.system() == 'Darwin':
    working_os = "macos"
print(f"current working operating system is {working_os}")

if working_os == "windows":
    os.system("python main.py")
elif working_os == "linux":
    os.system("python3 main.py")