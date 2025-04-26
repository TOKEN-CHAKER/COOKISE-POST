import requests
import os
import re
import time
import random
import threading
from requests.exceptions import RequestException

# Function to clear screen
def clear_screen():
    os.system("clear")

# Cookie input
def set_cookie():
    return input("\033[1;37mENTER YOUR COOKIE :: ")

# Commenter's name input
def get_commenter_name():
    return input("\033[1;32mENTER COMMENTER NAME :: ")

# Password input
def get_password():
    return input("\033[92mENTER PASSWORD :: ")

# Safe network request
def make_request(url, headers, cookies):
    try:
        response = requests.get(url, headers=headers, cookies=cookies, timeout=10).text
        return response
    except RequestException as e:
        print("\033[91m[!] Request Error:", e)
        return None

# Safe POST request
def post_comment(url, data, cookies):
    try:
        response = requests.post(url, data=data, cookies=cookies, timeout=10)
        return response.json()
    except RequestException as e:
        print("\033[91m[!] Comment Post Error:", e)
        return None

# Rotate User-Agent list
USER_AGENTS = [
    'Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 Chrome/90.0.4430.210 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; Redmi Note 9) AppleWebKit/537.36 Chrome/91.0.4472.101 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 12; RMX2151) AppleWebKit/537.36 Chrome/92.0.4515.159 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 9; vivo 1904) AppleWebKit/537.36 Chrome/86.0.4240.110 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 8.1.0; OPPO A3s) AppleWebKit/537.36 Chrome/80.0.3987.99 Mobile Safari/537.36'
]

# Logo
clear_screen()
logo = """
\033[1;32m____  _____       _       ______   _____  ____    ____     ______   
\033[1;32m|_   \\|_   _|     / \\     |_   _ `.|_   _||_   \\  /   _|  .' ___  |  
\033[1;33m|   \\ | |      / _ \\      | | `. \\ | |    |   \\/   |   / .'   \\_|  
\033[1;32m| |\\ \\| |     / ___ \\     | |  | | | |    | |\\  /| |   | |    ___  
\033[1;33m_| |_\\   |_  _/ /   \\ \\_  _| |_.' /_| |_  _| |_\\/| |_  \\ `.___]  | 
\033[1;32m|_____|\____||____| |____||______.'|_____||_____||_____|  `._____.'                                                

\033[1;32m<<══════════════════════════════════════════════════════════════════>>
\033[1;33m[=] OWNER    : BROKEN NADEEM
\033[1;32m[=] GITHUB   : BROKEN NADEEM
\033[1;36m[=] RULEX    : COOKIE POST
\033[1;33m[=] FACEBOOK : PARDHAN KIING
\033[1;32m<<══════════════════════════════════════════════════════════════════>>
"""
print(logo)
print("\033[92mStart Time:", time.strftime("%Y-%m-%d %H:%M:%S"))

# Comment Posting Function (Threaded)
def comment_spammer(post_id, token, cookies, commenter_name, comments, delay):
    x, fail_count = 0, 0
    while True:
        try:
            teks = comments[x].strip()
            full_comment = f"{commenter_name}: {teks}"

            headers = {
                'User-Agent': random.choice(USER_AGENTS),
                'Content-Type': 'application/x-www-form-urlencoded'
            }

            data = {
                'message': full_comment,
                'access_token': token
            }

            response = post_comment(f"https://graph.facebook.com/{post_id}/comments/", data, cookies={'Cookie': cookies})
            if response and 'id' in str(response):
                print("\033[1;37m[+] Posted: {}".format(full_comment))
            else:
                fail_count += 1
                print("\033[91m[-] Failed [{}]: {}".format(fail_count, full_comment))

            x = (x + 1) % len(comments)
            time.sleep(delay + random.uniform(0.5, 2))  # Random safe delay
        except Exception as e:
            print("\033[91m[!] Unexpected Error:", e)
            time.sleep(5)
            continue

# Main program
while True:
    try:
        cookies = set_cookie()

        response = make_request('https://business.facebook.com/business_locations', headers={
            'Cookie': cookies,
            'User-Agent': random.choice(USER_AGENTS)
        }, cookies={'Cookie': cookies})

        if response is None:
            break

        token_eaag = re.search('(EAAG\w+)', str(response)).group(1)
        post_id = input("\033[92mENTER POST ID :: ")
        commenter_name = get_commenter_name()
        delay = int(input("\033[92mENTER BASE DELAY (SECONDS) :: "))
        comment_file_path = input("\033[92mENTER COMMENT FILE PATH :: ")

        with open(comment_file_path, 'r') as file:
            comments = file.readlines()

        thread_count = int(input("\033[92mENTER THREAD COUNT (Recommended 3-5) :: "))

        for _ in range(thread_count):
            t = threading.Thread(target=comment_spammer, args=(post_id, token_eaag, cookies, commenter_name, comments, delay))
            t.start()

        break  # Break after starting threads

    except Exception as e:
        print("\033[91m[!] An unexpected error occurred:", e)
        break
