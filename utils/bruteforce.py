from colorama import Fore
import colorama, os
colorama.init(autoreset=True)

from zipfile import ZipFile
from rarfile import RarFile

def wordlist(filename=None, type=None, txt=None):
    if filename == None:
        print(f"{Fore.RED}")
        return "err INVALID FILE NAME"
    if type == None:
        return "err INVALID FILE TYPE"
    if txt == None:
        return "err INVALID WORDLIST NAME"


    if type == "rar":
        try:
            zip = RarFile(filename, 'r')
        except:
            return "err Failed to open the rar file"
    elif type == "zip":
        try:
            zip = ZipFile(filename, 'r')
        except:
            return "err Failed to open the zip file"
    else:
        return 'err invalid file type'
    try:
        txt = open(txt, "r").readlines()
    except:
        return "err INVALID WORDLIST NAME"
    attemps = 0
    for password in txt:
        attemps += 1
        try:
            zip.extractall(pwd=password.replace("\n", "").encode(), path="output")
        except Exception as e:
            print(f"{Fore.RED}[ - ] {attemps}/{len(txt)} invalid password: {Fore.LIGHTRED_EX}{password} | {Fore.LIGHTRED_EX}Error str: {e}")
        else:
            print(f"{Fore.GREEN}[ + ] Password found: {password} | extracted in {os.getcwd()}\\output | attempts: {attemps}")
            input(f"{Fore.YELLOW}[ * ]press enter to exit")
            break
    print(f"{Fore.RED}[ ! ] 0 passwords are valid")
    return "done"

def bruteforce(filename=None, type=None, chars=None):
    if filename == None:
        print(f"{Fore.RED}")
        return "err INVALID FILE NAME"
    if type == None:
        return "err INVALID FILE TYPE"
    if chars == None:
        return "err INVALID CHARS LIST"
    print(f'{Fore.YELLOW}[ * ] Chars: {Fore.LIGHTBLUE_EX}{chars}')
    passwords = []
    attemps = 0
    for current in range(10):
        a = [i for i in chars]
        for y in range(current):
            a = [x + i for i in chars for x in a]
        passwords = passwords + a

        if type == "rar":
            try:
                zip = RarFile(filename, 'r')
            except:
                return "err Failed to open the rar file"
        elif type == "zip":
            try:
                zip = ZipFile(filename, 'r')
            except:
                return "err Failed to open the zip file"
        else:
            return 'err invalid file type'
        
        for password in passwords:
            attemps += 1
            try:
                zip.extractall(pwd=password.encode(), path="output")
            except Exception as e:
                print(f"{Fore.RED}[ - ] {attemps} invalid password: {Fore.LIGHTRED_EX}{password} | {Fore.LIGHTRED_EX}Error str: {e}")
            else:
                print(f"{Fore.GREEN}[ + ] Password found: {password} | extracted in {os.getcwd()}\\output | attempts: {attemps}")
                input("press enter to exit") #fra poco devo testarlo, prepara una wordlist in cui ci sono password a caso e dopo un po' c'è "ab"
                return "done"
    return "done"