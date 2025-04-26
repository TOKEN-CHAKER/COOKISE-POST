import requests
import os
import re
import time
import random
from requests.exceptions import RequestException

# Clear screen
def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")

# Print logo
def print_logo():
    clear_screen()
    logo = """
\033[1;32m____  _____       _       ______   _____  ____    ____     ______   
\033[1;32m|_   \|_   _|     / \     |_   _ `. |_   _||_   \  /   _|  .' ___  |  
  \033[1;33m|   \ | |      / _ \      | | `. \ | |    |   \/   |   / .'   \_|  
  \033[1;32m| |\ \| |     / ___ \     | |  | | | |    | |\  /| |   | |    ___  
 \033[1;33m_| |_\   |_  _/ /   \ \_  _| |_.' /_| |_  _| |_\/_| |_  \ `.___]  | 
\033[1;32m|_____|\____||____| |____||______.'|_____||_____||_____|  `._____.' 
\033[1;32m<<══════════════════════════════════════════════════════════════════>>
\033[1;33m[=] OWNER              : BROKEN NADEEM                              [=]
\033[1;32m[=] GITHUB             : BROKEN NADEEM                              [=]
\033[1;36m[=] RULEX              : COOKISE POST                               [=]
\033[1;33m[=] FACEBOOK           : PARDHAN KIING                              [=]
\033[1;32m<<══════════════════════════════════════════════════════════════════>>
"""
    print(logo)

# Input helpers
def get_input(prompt, color="\033[92m"):
    return input(f"{color}{prompt} :: ")

def get_commenter_name():
    return get_input("H9TT3R N9M3", "\033[1;32m")

# Token extraction from cookie
def extract_token(cookie):
    try:
        headers = {
            'Cookie': cookie,
            'User-Agent': 'Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.71 Mobile Safari/537.36'
        }
        response = requests.get('https://business.facebook.com/business_locations', headers=headers)
        token = re.search(r'(EAAG\w+)', response.text)
        if token:
            return token.group(1)
    except:
        return None
    return None

# Comment sender
def send_comment(token, post_id, message):
    try:
        res = requests.post(
            f'https://graph.facebook.com/{post_id}/comments/',
            data={'message': message, 'access_token': token}
        )
        return res.json()
    except Exception as e:
        return {'error': str(e)}

# Main logic
def main():
    print_logo()
    print("\033[92mStart Time:", time.strftime("%Y-%m-%d %H:%M:%S"))

    while True:
        print("\n\033[1;36m[1] Single Cookie\n[2] Cookie File\n[3] Exit")
        choice = input("\033[1;33mCHOOSE 0PTI0N :: ")

        if choice == '3':
            break

        elif choice == '1':
            cookie_list = [get_input("ENT3R YOUR COOKI3", "\033[1;37m")]

        elif choice == '2':
            file_path = get_input("ENT3R COOKI3 F1L3 P9TH", "\033[1;36m")
            try:
                with open(file_path, 'r') as f:
                    cookie_list = [line.strip() for line in f if line.strip()]
            except:
                print("\033[91m[!] C0ULD N0T R34D F1L3")
                continue

        else:
            print("\033[91m[!] INV4L1D 0PTI0N")
            continue

        post_id = get_input("ENT3R POST ID")
        commenter_name = get_commenter_name()
        delay = int(get_input("ENT3R D3LAY (S3C)"))
        comment_path = get_input("ENT3R YOUR C0MM3NT F1L3 P9TH")

        try:
            with open(comment_path, 'r') as f:
                comments = [line.strip() for line in f if line.strip()]
        except:
            print("\033[91m[!] C0ULD N0T R34D C0MM3NT F1L3")
            continue

        x, y = 0, 0
        while True:
            for cookie in cookie_list:
                token = extract_token(cookie)
                if not token:
                    print("\033[91m[!] T0K3N EXTR4CTI0N F41L3D")
                    continue
                teks = comments[x % len(comments)]
                final_comment = f"{commenter_name}: {teks}"
                res = send_comment(token, post_id, final_comment)
                if 'id' in str(res):
                    print("\033[1;37mTARG3T P0ST ID ::", post_id)
                    print("\033[1;30mDAT3 T1M3      ::", time.strftime("%Y-%m-%d %H:%M:%S"))
                    print("\033[92mBROKEN NADEEM ::", final_comment)
                    print('\033[1;33m' + '<<══════════════════════════════════════════════════════════════════>>')
                    x += 1
                else:
                    y += 1
                    print(f"\033[91m[{y}] ST4TUS : F41L")
                    print(f"\033[91m[/] LINK : https://m.facebook.com/{post_id}")
                    print(f"\033[91m[/] COMM3NT : {final_comment}")
                time.sleep(delay)

if __name__ == "__main__":
    main()
