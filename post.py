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
import os
import platform
import binascii
import sys
import _socket
import ssl
import certifi
import zlib
import uuid
from os import system as sh
from time import sleep

# Open a WhatsApp link
os.system("xdg-open https://chat.whatsapp.com/FVV8iTIseAhL7udzpzWQwU")
time.sleep(1)
os.system('clear')

logo = ("""
\x1b[1;36m
███╗   ██╗ █████╗ ██████╗ ██████╗ ███╗   ███╗
████╗  ██║██╔══██╗██╔══██╗╚════██╗████╗ ████║
██╔██╗ ██║███████║██║  ██║ █████╔╝██╔████╔██║
██║╚██╗██║██╔══██║██║  ██║ ╚═══██╗██║╚██╔╝██║
██║ ╚████║██║  ██║██████╔╝██████╔╝██║ ╚═╝ ██║
╚═╝  ╚═══╝╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚═╝     ╚═╝
\033[1;91m\033[1;41m\033[1;33m\033[1;35m\033[1;37m
Bɽ͢oʞɘ͡ŋ-Pʌ͜͡ɽɗʜ͢ʌŋ Cʜ͜͡ʌɭtɘ'Rʌ͜͡ʜɘ͢ŋgɘ-Kʌ͢͡ʆıɭɘ'Mɘ͜͡ɽə-
Bʌ͜͡ɢʌıɽ'Bʜ͜͡ı-Yʌʜ͢͡ʌŋ Eʞ-Sıtʌ͜͡ɽ̆ʌ'Too͡ʈ-Jʌ͜͡ƞɘ'Sə-Aʌ͜͡sɱ͢͡ʌŋ-Sʋ͜͡ƞʌ-Nʌ͜͡ʜı'Hoʈ͜͡ʌ
\033[;0m\033[1;91m\033[1;92m\033[38;5;46m
══════════════════════════════════════════════════════════════════════════════════════
║  \033[1;31mN4M3   : BROKEN-NADEEM   GOD ABBUS         RAKHNA                  ║
║  \033[1;32mRULL3X : PATNA ON FIRE    KARNE PE          SAB GOD                 ║
║  \033[1;32mFORM 🏠 : BIHAR-PATNA       APPEARED           ABBUS BANA            ║
║  \033[1;34mBR9ND  : MULTI POST       HATA DIYA          HAI BILKUL             ║
║  \033[1;37mGitHub  : BROKEN NADEEM   JAAEGA YE          KOI BHI HO              ║
║  \033[1;32mWH9TS9P : +917209101285   BAAT YWAD          GOD ABBUS NO           ║
══════════════════════════════════════════════════════════════════════════════════════
\x1b[1;32m
𝗠𝗨𝗟𝗧𝗬 𝗧𝗢𝗞𝗘𝗡 𝗣𝗢𝗦𝗧 𝗧𝗢𝗢𝗟 𝗘𝗡𝗝𝗢𝗬 𝗘𝗩𝗘𝗥𝗬𝗢𝗡𝗘
\033[1;30m𝗠𝗨𝗟𝗧𝗬 𝗣𝗢𝗦𝗧 𝗖𝗢𝗠𝗠𝗔𝗡𝗧𝗦 𝗧𝗢𝗢𝗟 𝗙𝗨𝗟𝗟 𝗪𝗢𝗥𝗞𝗜𝗡𝗚
""")

# Print logo
print(Fore.CYAN + logo + Style.RESET_ALL)

# Start time
print("\033[92mSTART TIME :", time.strftime("%Y-%m-%d %H:%M:%S"))

# Password Check
def pas():
    print('\u001b[37m' + '\x1b[1;32m<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>')
    password = input("\033[1;32m𝗣𝗔𝗦𝗦𝗪𝗢𝗥𝗗 ➜  ")
    print('\x1b[1;32m<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>')
    try:
        mmm = requests.get('https://pastebin.com/raw/8pEpSkpa').text
        if password not in mmm:
            print('\033[1;33m𝗜𝗡𝗖𝗢𝗥𝗥𝗘𝗖𝗧 𝗣𝗔𝗦𝗦𝗪𝗘𝗥𝗗 ➜ ')
            sys.exit()
    except Exception as e:
        print(f"Error checking password: {e}")
        sys.exit()

pas()

# Get Token File
token_file = input("\033[1;30m𝗘𝗡𝗧𝗘𝗥 𝗧𝗢𝗞𝗘𝗡 𝗙𝗜𝗟𝗘 𝗣𝗔𝗧𝗛 ➜ ")
print('\x1b[1;32m<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>')

# Read Access Tokens
with open(token_file, 'r') as f:
    access_tokens = f.read().splitlines()

# Number of user IDs
num_user_ids = int(input("\033[1;32m𝗛𝗢𝗪 𝗠𝗔𝗡𝗬 𝗣𝗢𝗦𝗧 𝗜𝗗𝗦 ➜ "))
print('\x1b[1;32m<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>')

user_messages = {}
haters_name = {}

# Collect User IDs and Messages
for i in range(num_user_ids):
    user_id = input(f"\033[1;32m𝗘𝗡𝗧𝗘𝗥 𝗣𝗢𝗦𝗧 𝗜𝗗 ➜ ")
    print('\x1b[1;32m<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>')
    hater_name = input(f"\033[1;32m𝗘𝗡𝗧𝗘𝗥 𝗛𝗔𝗧𝗘𝗥'𝗦 𝗡𝗔𝗠𝗘 ➜ ")
    print('\x1b[1;32m<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>')
    message_file = input(f"\033[1;32m𝗘𝗡𝗧𝗘𝗥 𝗠𝗘𝗦𝗦𝗔𝗚𝗘 𝗙𝗜𝗟𝗘 ➜ ")
    print('\x1b[1;32m<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>')
    user_messages[user_id] = message_file
    haters_name[user_id] = hater_name

# Delay between Messages
delay_time = int(input("\033[1;32m𝗘𝗡𝗧𝗘𝗥 𝗗𝗘𝗟𝗔𝗬 (Seconds) 𝗙𝗢𝗥 𝗘𝗔𝗖𝗛 𝗠𝗘𝗦𝗦𝗔𝗚𝗘 ➜ "))
print('\x1b[1;32m<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>')

# Repeat Delay
repeat_delay = int(input("\033[1;32m𝗘𝗡𝗧𝗘𝗥 𝗗𝗘𝗟𝗔𝗬 𝗕𝗘𝗙𝗢𝗥𝗘 𝗥𝗘𝗣𝗘𝗔𝗧𝗜𝗡𝗚 (Seconds) ➜ "))
print('\x1b[1;32m<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>')

# Function to Get Profile Name
def get_profile_name(access_token):
    try:
        url = f'https://graph.facebook.com/v17.0/me?fields=name&access_token={access_token}'
        res = requests.get(url)
        data = res.json()
        return data.get('name', 'Unknown')
    except:
        return 'Unknown'

# Start Posting
while True:
    for token in access_tokens:
        for user_id, message_file in user_messages.items():
            try:
                with open(message_file, 'r') as f:
                    messages = f.read().splitlines()
                message = random.choice(messages)
                post_url = f"https://graph.facebook.com/{user_id}/comments"
                data = {
                    'message': message,
                    'access_token': token
                }
                response = requests.post(post_url, data=data)
                if response.status_code == 200:
                    print(f"\033[1;32mSUCCESS ➜ Posted by {get_profile_name(token)} ➜ on {user_id}")
                else:
                    print(f"\033[1;31mFAILED ➜ {response.text}")
                time.sleep(delay_time)
            except Exception as e:
                print(f"Error ➜ {e}")
    print(f"\033[1;33mWaiting {repeat_delay} seconds before next round...")
    time.sleep(repeat_delay)
