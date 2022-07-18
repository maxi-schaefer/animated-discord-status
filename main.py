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
        >> Made by gokiimax                                              >> github.com/gokiimax
{Fore.RESET}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{Fore.LIGHTRED_EX}

                [1] Start                                                [2] Exit 

{Fore.RESET}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

"""

authorization = {
    'Authorization': get_path("Token")
}

def main():

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    print(banner)
    command = input(f"{Fore.LIGHTRED_EX}Choose: {Fore.RESET}")

    if command == "1":
        print("Custom Status started...")
        while True:
            for i in range(3):
                print(f"Status changed to: {get_path(f'Emoji{i + 1}')} | {get_path(f'Status{i + 1}')} | Time between change: {str(get_path('TimeBetweenChange'))}s")
                requests.patch("https://discord.com/api/v7/users/@me/settings", headers=authorization, json={"custom_status": {"text": get_path(f"Status{i + 1}"), "emoji_name": get_path(f"Emoji{i + 1}")}})
                time.sleep(get_path("TimeBetweenChange"))
    else:
        exit(-1)

main()