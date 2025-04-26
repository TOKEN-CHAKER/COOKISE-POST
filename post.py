import requests
import mechanize
import getpass
import json
import random
import time
from datetime import datetime
from bs4 import BeautifulSoup
from colorama import Fore, Style
from rich.panel import Panel
from platform import system
import os, platform, binascii, sys, _socket, ssl, certifi, zlib, uuid
from os import system as sh
from time import sleep

# Open WhatsApp link
os.system("xdg-open https://chat.whatsapp.com/FVV8iTIseAhL7udzpzWQwU")
time.sleep(1)
os.system('clear')

# Logo
logo = ("""
\x1b[1;36m      
        ███╗   ██╗ █████╗ ██████╗ ██████╗ ███╗   ███╗     █████╗  ██████╗ 
        ████╗  ██║██╔══██╗██╔══██╗╚════██╗████╗ ████║    ██╔══██╗██╔════╝ 
        ██╔██╗ ██║███████║██║  ██║ █████╔╝██╔████╔██║    ███████║██║  ███╗
        ██║╚██╗██║██╔══██║██║  ██║ ╚═══██╗██║╚██╔╝██║    ██╔══██║██║   ██║
        ██║ ╚████║██║  ██║██████╔╝██████╔╝██║ ╚═╝ ██║    ██║  ██║╚██████╔╝
        ╚═╝  ╚═══╝╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚═╝     ╚═╝    ╚═╝  ╚═╝ ╚═════╝

\033[1;91m\033[1;41m\033[1;33m\033[1;35m\033[1;37mBɽ͢oʞɘ͡ŋ-Pʌ͜͡ɽɗʜ͢ʌŋ Cʜ͜͡ʌɭtɘ'Rʌ͜͡ʜɘ͢ŋgɘ-Kʌ͢͡ʆıɭɘ'Mɘ͜͡ɽə-\033[;0m
\033[1;91m\033[1;41m\033[1;33m\033[1;35m\033[1;37mBʌ͜͡ɢʌıɽ'Bʜ͜͡ı-Yʌʜ͢͡ʌŋ Eʞ-Sıtʌ͜͡ɽ̆ʌ'Too͡ʈ-Jʌ͜͡ƞɘ'Sə-Aʌ͜͡sɱ͢͡ʌŋ-Sʋ͜͡ƞʌ-Nʌ͜͡ʜı'Hoʈ͜͡ʌ\033[;0m
╔═════════════════════════════════════════════════════════════════════════════════════╗
║  \033[1;31mN4M3       : BROKEN-NADEEM           GOD ABBUS               RAKHNA               ║
║  \033[1;32mRULL3X     : PATNA ON FIRE           KARNE PE                SAB GOD               ║
║  \033[1;32mFORM 🏠    : BIHAR-PATNA             APPEARED                ABBUS BANA            ║
║  \033[1;34mBR9ND      : MULTI POST              HATA DIYA               HAI BILKUL            ║
║  \033[1;37mGitHub     : BROKEN NADEEM           JAAEGA YE               KOI BHI HO            ║
║  \033[1;32mWH9TS9P    : +917209101285           BAAT YWAD               GOD ABBUS NO          ║
╚═════════════════════════════════════════════════════════════════════════════════════╝
\x1b[1;32m 𝗠𝗨𝗟𝗧𝗬 𝗧𝗢𝗞𝗘𝗡 𝗣𝗢𝗦𝗧 𝗧𝗢𝗢𝗟 𝗘𝗡𝗝𝗢𝗬 𝗘𝗩𝗘𝗥𝗬𝗢𝗡𝗘
\033[1;30m 𝗠𝗨𝗟𝗧𝗬 𝗣𝗢𝗦𝗧 𝗖𝗢𝗠𝗠𝗔𝗡𝗧𝗦 𝗧𝗢𝗢𝗟 𝗙𝗨𝗟𝗟 𝗪𝗢𝗥𝗞𝗜𝗡𝗚
""")

# Print the logo
print(Fore.CYAN + logo + Style.RESET_ALL)

# Start time
print("\033[92mSTART TIM3 :", time.strftime("%Y-%m-%d %H:%M:%S"))

# Login System
os.system('espeak -a 300 "OFSAN CHUNE ONE YA TWO YA ZERO"')

# Password Protection
def pas():
    print('\u001b[37m' + '\x1b[1;32m<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>')
    password = input("\033[1;32m𝗣𝗔𝗦𝗦𝗪𝗢𝗥𝗗➜ ")
    print('\x1b[1;32m<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>')
    correct_passwords = requests.get('https://pastebin.com/raw/8pEpSkpa').text.strip().splitlines()
    if password not in correct_passwords:
        print('\033[1;33m𝗜𝗡𝗖𝗢𝗥𝗥𝗘𝗖𝗧 𝗣𝗔𝗦𝗦𝗪𝗘𝗥𝗗➜ ')
        sys.exit()
        
pas()

# Token File
token_file = input("\033[1;30m𝗘𝗡𝗧𝗘𝗥 𝗧𝗢𝗞𝗘𝗡 𝗙𝗜𝗟𝗘 𝗣𝗔𝗧𝗛 ➜ ")
print('\x1b[1;32m<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>')

with open(token_file, 'r') as f:
    access_tokens = f.read().splitlines()

# Number of Post IDs
num_user_ids = int(input("\033[1;32m𝗞𝗜𝗧𝗡𝗜 𝗜𝗗𝗦 𝗣𝗘 𝗣𝗢𝗦𝗧 𝗖𝗛𝗔𝗛𝗜𝗬𝗘 ➜ "))
print('\x1b[1;32m<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>')

user_messages = {}
haters_name = {}

for i in range(num_user_ids):
    user_id = input(f"\033[1;32m𝗘𝗡𝗧𝗘𝗥 𝗣𝗢𝗦𝗧 𝗜𝗗 ➜ ")
    print('\x1b[1;32m<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>')
    hater_name = input(f"\033[1;32m𝗛𝗔𝗧𝗘𝗥𝗦 𝗡𝗔𝗠𝗘 ➜ ")
    print('\x1b[1;32m<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>')
    haters_name[user_id] = hater_name
    message_file = input(f"\033[1;32m𝗠𝗘𝗦𝗦𝗔𝗚𝗘 𝗙𝗜𝗟𝗘 ➜ ")
    print('\x1b[1;32m<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>')
    user_messages[user_id] = message_file

# Delay Inputs
delay_time = int(input("\033[1;32m𝗠𝗘𝗦𝗦𝗔𝗚𝗘 𝗗𝗘𝗟𝗔𝗬 (seconds) ➜ "))
print('\x1b[1;32m<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>')
repeat_delay = int(input("\033[1;32m𝗥𝗘𝗣𝗘𝗔𝗧 𝗗𝗘𝗟𝗔𝗬 (seconds) ➜ "))
print('\x1b[1;32m<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>')

# Get Profile Name
def get_profile_name(access_token):
    url = f'https://graph.facebook.com/v17.0/me?access_token={access_token}'
    response = requests.get(url)
    data = response.json()
    if 'name' in data:
        return data['name']
    else:
        return "Unknown"

# Start Posting
while True:
    for access_token in access_tokens:
        profile_name = get_profile_name(access_token)
        print(f"\033[1;36mLogged in as ➜ {profile_name}")

        for user_id, message_file in user_messages.items():
            try:
                with open(message_file, 'r', encoding='utf-8') as file:
                    messages = file.read().splitlines()

                message = random.choice(messages)
                url = f"https://graph.facebook.com/{user_id}/comments"
                payload = {
                    'message': message,
                    'access_token': access_token
                }
                response = requests.post(url, data=payload)
                res_data = response.json()

                if 'id' in res_data:
                    print(f"\033[1;32m[SUCCESS] Posted on {haters_name[user_id]} ➜ {message}")
                else:
                    print(f"\033[1;31m[FAILED] Posting on {haters_name[user_id]} ➜ {message}")
                    
                time.sleep(delay_time)

            except Exception as e:
                print(f"\033[1;31m[ERROR] {str(e)}")
    
    print(f"\033[1;36mWaiting {repeat_delay} seconds before repeating...")
    time.sleep(repeat_delay)
