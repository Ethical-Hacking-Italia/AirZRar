"""

            © JProgrammer-it, C0MPL3XDEV | LICENSE: GNU General Public License v2.0

"""


from colorama import Fore
import colorama, os
colorama.init(autoreset=True)

from utils.graphics import *
from utils.bruteforce import *

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
charsandnumbers = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
advence_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!"£$%&/()=?ì\' '

def run():
    global chars, charsandnumbers, advence_chars
    while True:
        filename = input(f'{Fore.YELLOW}[ * ] Zip file name >')
        type = input(f'{Fore.YELLOW}[ * ] File Type (zip/rar) >')
        method = input(f'{Fore.YELLOW}[ * ] BruteForce Method to use (wordlist/generate)>')
        if method == "generate":
            custom_chars = input("\n" + Fore.LIGHTYELLOW_EX + "="*50 + f"\n [1] {advence_chars}\n [2] {charsandnumbers}\n [3] {chars}\n [4] custom chars\n\n{Fore.YELLOW}[ * ] chars to use (1/2/3/4) >")
            while True:
                if custom_chars == '1':
                    chars_to_use = advence_chars
                    break
                elif custom_chars == '2':
                    chars_to_use = charsandnumbers
                    break
                elif custom_chars == '3':
                    chars_to_use = chars
                    break
                elif custom_chars == '4':
                    chars_to_use = input(f'{Fore.YELLOW}[ * ] Chars to use >')
                    if chars == "":
                        print(f'{Fore.RED}[ ! ] Invalid chars')
                    else:
                        break
                else:
                    print(f'{Fore.RED}[ ! ] Invalid chars')
            results = bruteforce(filename, type, chars_to_use)
            if "err" in results:
                print(f"{Fore.RED}[ ! ] ERROR: {results.replace('err ', '')}")
        elif method == "wordlist":
            txt = input(f"{Fore.YELLOW}[ * ] Wordlist file name >")
            results = wordlist(filename, type, txt)
            if "err" in results:
                print(f"{Fore.RED}[ ! ] ERROR: {results.replace('err ', '')}")

menu()
run()
