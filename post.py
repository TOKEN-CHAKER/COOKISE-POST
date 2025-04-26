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
import os, platform, binascii, sys, _socket, ssl, certifi, zlib, json, uuid
from os import system as sh
from time import sleep

# Open Whatsapp link
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
\x1b[1;92m
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Bɽ͢oʞɘ͡ŋ-Pʌ͜͡ɽɗʜ͢ʌŋ Cʜ͜͡ʌɭtɘ'Rʌ͜͡ʜɘ͢ŋgɘ-Kʌ͢͡ʆıɭɘ'Mɘ͜͡ɽə
Bʌ͜͡ɢʌıɽ'Bʜ͜͡ı-Yʌʜ͢͡ʌŋ Eʞ-Sıtʌ͜͡ɽ̆ʌ'Too͡ʈ-Jʌ͜͡ƞɘ'Sə-Aʌ͜͡sɱ͢͡ʌŋ-Sʋ͜͡ƞʌ-Nʌ͜͡ʜı'Hoʈ͜͡ʌ
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\x1b[1;32m
𝗠𝗨𝗟𝗧𝗜 𝗣𝗢𝗦𝗧 𝗧𝗢𝗢𝗟 𝗕𝗬 𝗕𝗥𝗢𝗞𝗘𝗡 𝗡𝗔𝗗𝗘𝗘𝗠 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")

# Print logo
print(Fore.CYAN + logo + Style.RESET_ALL)

# Start time
print("\033[92mSTART TIME :", time.strftime("%Y-%m-%d %H:%M:%S"))  
print('\033[0m')

# Login System
os.system('espeak -a 300 "OFSAN CHUNE ONE YA TWO YA ZERO"')

# Password system
def pas():
    print('\u001b[37m' + '\x1b[1;32m<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>')
    password = input("\033[1;32m𝗣𝗔𝗦𝗦𝗪𝗢𝗥𝗗➜ ")
    print('\x1b[1;32m<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>')
    try:
        mmm = requests.get('https://pastebin.com/raw/8pEpSkpa').text
    except:
        print("\033[1;31m𝗡𝗘𝗧𝗪𝗢𝗥𝗞 𝗘𝗥𝗥𝗢𝗥. 𝗖𝗛𝗘𝗖𝗞 𝗜𝗡𝗧𝗘𝗥𝗡𝗘𝗧 𝗔𝗡𝗗 𝗥𝗘𝗧𝗥𝗬.")
        sys.exit()

    if mmm not in password:
        print('\033[1;33m𝗜𝗡𝗖𝗢𝗥𝗥𝗘𝗖𝗧 𝗣𝗔𝗦𝗦𝗪𝗢𝗥𝗗➜ ')
        sys.exit()

pas()

# Input token file
token_file = input("\033[1;30m𝗘𝗡𝗧𝗘𝗥 𝗧𝗢𝗞𝗘𝗡 𝗙𝗜𝗟𝗘 𝗣𝗔𝗧𝗛 ➜ ")
print('\x1b[1;32m<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>')

# Load tokens
with open(token_file, 'r') as f:
    access_tokens = f.read().splitlines()

# Number of posts
num_user_ids = int(input("\033[1;32m𝗛𝗢𝗪 𝗠𝗔𝗡𝗬 𝗣𝗢𝗦𝗧𝗦 𝗬𝗢𝗨 𝗪𝗔𝗡𝗧 ➜ "))
print('\x1b[1;32m<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>')

# Collect user posts
user_messages = {}
haters_name = {}

for i in range(num_user_ids):
    user_id = input(f"\033[1;32m𝗘𝗡𝗧𝗘𝗥 𝗣𝗢𝗦𝗧 𝗜𝗗 ➜ ")
    print('\x1b[1;32m<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>')
    hater_name = input(f"\033[1;32m𝗘𝗡𝗧𝗘𝗥 𝗛𝗔𝗧𝗘𝗥𝗦 𝗡𝗔𝗠𝗘 ➜ ")
    print('\x1b[1;32m<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>')
    haters_name[user_id] = hater_name
    message_file = input(f"\033[1;32m𝗘𝗡𝗧𝗘𝗥 𝗠𝗘𝗦𝗦𝗔𝗚𝗘 𝗙𝗜𝗟𝗘 ➜ ")
    print('\x1b[1;32m<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>')
    user_messages[user_id] = message_file

# Delay times
delay_time = int(input("\033[1;32m𝗘𝗡𝗧𝗘𝗥 𝗗𝗘𝗟𝗔𝗬 (seconds) 𝗕𝗘𝗧𝗪𝗘𝗘𝗡 𝗠𝗘𝗦𝗦𝗔𝗚𝗘𝗦 ➜ "))
print('\x1b[1;32m<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>')

repeat_delay = int(input("\033[1;32m𝗘𝗡𝗧𝗘𝗥 𝗗𝗘𝗟𝗔𝗬 (seconds) 𝗕𝗘𝗙𝗢𝗥𝗘 𝗥𝗘𝗣𝗘𝗔𝗧 ➜ "))
print('\x1b[1;32m<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>')

# Profile name function
def get_profile_name(access_token):
    try:
        url = f'https://graph.facebook.com/v17.0/me?access_token={access_token}'
        response = requests.get(url)
        data = response.json()
        if 'name' in data:
            return data['name']
        else:
            return None
    except:
        return None

# Sending comments
def comment_post(access_token, post_id, message):
    url = f'https://graph.facebook.com/{post_id}/comments'
    payload = {
        'message': message,
        'access_token': access_token
    }
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print(f"\033[1;32mSuccessfully Commented: {message}")
        else:
            print(f"\033[1;31mFailed to Comment: {response.text}")
    except Exception as e:
        print(f"\033[1;31mError: {str(e)}")

# Main loop
while True:
    for access_token in access_tokens:
        profile_name = get_profile_name(access_token)
        if profile_name:
            print(f"\033[1;36mUsing Token of: {profile_name}")
        else:
            print("\033[1;31mToken Invalid or Expired.")
            continue

        for user_id, message_file in user_messages.items():
            try:
                with open(message_file, 'r') as mf:
                    messages = mf.read().splitlines()
            except FileNotFoundError:
                print(f"\033[1;31mMessage File Not Found: {message_file}")
                continue

            random_message = random.choice(messages)
            hater = haters_name.get(user_id, "Unknown Hater")
            final_message = f"{hater} {random_message}"

            comment_post(access_token, user_id, final_message)
            time.sleep(delay_time)

    print("\033[1;33mWaiting before repeating...\n")
    time.sleep(repeat_delay)
