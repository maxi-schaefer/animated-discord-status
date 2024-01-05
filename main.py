import os
import time
import requests
from colorama import Fore
from assets.config import *


banner = f"""{Fore.LIGHTRED_EX}

        _________                 __                   _________ __          __                
        \_   ___ \ __ __  _______/  |_  ____   _____  /   _____//  |______ _/  |_ __ __  ______
        /    \  \/|  |  \/  ___/\   __\/  _ \ /     \ \_____  \\\   __\__  \\\   __\  |  \/  ___/
        \     \___|  |  /\___ \  |  | (  <_> )  Y Y  \/        \|  |  / __ \|  | |  |  /\___ \ 
         \______  /____//____  > |__|  \____/|__|_|  /_______  /|__| (____  /__| |____//____  >
                \/           \/                    \/        \/           \/                \/ 
        >> Made by max                                              >> github.com/maxi-schaefer
{Fore.RESET}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{Fore.LIGHTRED_EX}

                [1] Start                                                [2] Exit 

{Fore.RESET}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

"""

authorization = {
    'Authorization': get_path("token")
}

def getCurrentTimeString():
    t = time.localtime()
    currentTime = time.strftime("%H:%M:%S", t)
    return currentTime

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def main():

    clear()

    print(banner)
    command = input(f"{Fore.LIGHTRED_EX}Choose: {Fore.RESET}")

    if command == "1":
        while True:
            for status in get_path("statuses"):
                print(f"[{getCurrentTimeString()}] Status changed to: {status['emoji']} {status['status']}")
                requests.patch("https://discord.com/api/v7/users/@me/settings", headers=authorization, json={"custom_status": {"text": status['status'], "emoji_name": status['emoji']}})
                print(f"[{getCurrentTimeString()}] 😴 Sleeping for {get_path('timeBetweenChange')} seconds!")
                time.sleep(get_path("timeBetweenChange"))
    else:
        exit(-1)

main()