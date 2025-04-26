import requests
import os
import re
import time
import random
from requests.exceptions import RequestException

# Function to clear the terminal screen
def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")

# Function to set up single or multiple cookies
def set_cookie():
    choice = input("\033[1;33m[?] 1 Cookie (1) ya Cookie File (2) Choose karo: \033[0m")
    if choice == "1":
        Cookie = input("\033[1;37mENT3R YOUR COOKI3 :: ")
        return [Cookie]
    elif choice == "2":
        filepath = input("\033[1;37mENT3R COOKI3 F1L3 P9TH :: ")
        with open(filepath, 'r') as file:
            cookies = [line.strip() for line in file if line.strip()]
        return cookies
    else:
        print("\033[91m[!] Invalid choice, defaulting to single cookie input.")
        Cookie = input("\033[1;37mENT3R YOUR COOKI3 :: ")
        return [Cookie]

# Function to prompt for commenter's name
def get_commenter_name():
    return input(" \033[1;32mH9TT3R N9M3 :: ")

# Logo
clear_screen()
logo = """
 \033[1;32m____  _____       _       ______   _____  ____    ____     ______   
\033[1;32m|_   \\|_   _|     / \\     |_   _ `.|_   _||_   \\  /   _|  .' ___  |  
  \033[1;33m|   \\ | |      / _ \\      | | `. \\ | |    |   \\/   |   / .'   \\_|  
  \033[1;32m| |\\ \\| |     / ___ \\     | |  | | | |    | |\\  /| |   | |    ___  
 \033[1;33m_| |_\\   |_ _/ /   \\ \\_  _| |_.' /_| |_  _| |_\\/|_| |_  \\ `.___]  | 
\033[1;32m|_____\\____||____| |____||______.'|_____||_____||_____|  `._____.'
\033[1;32m<<══════════════════════════════════════════════════════════════════>>
\033[1;33m[=] OWNER                  : BROKEN NADEEM                        [=]
\033[1;32m[=] GITHUB                 : BROKEN NADEEM                        [=]
\033[1;36m[=] RULEX                  : COOKIE POST                          [=]
\033[1;33m[=] FACEBOOK               : PARDHAN KIING                        [=]
\033[1;32m<<══════════════════════════════════════════════════════════════════>>
"""
print(logo)
print("\033[92mStart Time:", time.strftime("%Y-%m-%d %H:%M:%S"))  

# Request function
def make_request(url, headers, cookies):
    try:
        response = requests.get(url, headers=headers, cookies=cookies, timeout=10).text
        return response
    except RequestException as e:
        print("\033[91m[!] Error making request:", e)
        return None

# Safe Post function with retry
def safe_post(url, data, cookies):
    while True:
        try:
            response = requests.post(url, data=data, cookies=cookies, timeout=10).json()
            return response
        except RequestException as e:
            print("\033[91m[!] Retry due to network error:", e)
            time.sleep(random.uniform(3,5))

# Login and comment start
while True:
    try:
        print()
        cookie_list = set_cookie()
        tokens = []
        for cook in cookie_list:
            response = make_request('https://business.facebook.com/business_locations', headers={
                'Cookie': cook,
                'User-Agent': 'Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]'
            }, cookies={'Cookie': cook})
            if response:
                token_eaag = re.search('(EAAG\w+)', str(response))
                if token_eaag:
                    tokens.append((token_eaag.group(1), cook))
                else:
                    print("\033[91m[!] Token extraction failed for one cookie.")
            else:
                print("\033[91m[!] Failed to connect for one cookie.")

        if not tokens:
            print("\033[91m[!] No valid tokens extracted. Exiting...")
            break

        id_post = input(" \033[92mENT3R POST ID :: ")
        commenter_name = get_commenter_name()
        delay = float(input(" \033[92mENT3R D3ALY S3COND3 (Allow decimal eg 3.5):: "))
        comment_file_path = input(" \033[92mENT3R YOUR C0MM3NT F1L3 P9TH :: ")
        
        with open(comment_file_path, 'r') as file:
            comments = [line.strip() for line in file if line.strip()]
        
        x, y = 0, 0
        print()

        while True:
            try:
                token, cook = random.choice(tokens)
                teks = comments[x].strip()
                comment_with_name = f"{commenter_name}: {teks}"
                
                data = {
                    'message': comment_with_name,
                    'access_token': token
                }
                post_response = safe_post(f'https://graph.facebook.com/{id_post}/comments/', data, {'Cookie': cook})

                if post_response and 'id' in post_response:
                    print("\033[1;37mTARG3T P0ST ID ::", id_post)
                    print("\033[1;30mDAT3 T1M3      ::", time.strftime("%Y-%m-%d %H:%M:%S"))
                    print("\033[92mBROKEN NADEEM::", comment_with_name)
                    print('\033[1;33m' + '<<══════════════════════════════════════════════════════════════════>>')
                    x = (x + 1) % len(comments)
                else:
                    y += 1
                    print("\033[91m[{}] Status : Failure".format(y))
                    print("\033[91m[/]Link : https://m.basic.facebook.com/{}".format(id_post))
                    print("\033[91m[/]Comments : {}\n".format(comment_with_name))
                
                # Random slight variation delay to prevent block
                time.sleep(delay + random.uniform(0.5, 1.7))
                
            except KeyboardInterrupt:
                print("\033[91m[!] Script Stopped by User")
                break
            except Exception as e:
                print("\033[91m[!] An unexpected error occurred:", e)
                time.sleep(5)
                continue

    except Exception as e:
        print("\033[91m[!] An unexpected error occurred:", e)
        break
