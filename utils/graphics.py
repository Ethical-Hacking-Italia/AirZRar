import platform, shutil, os
from colorama import Fore
import colorama
colorama.init(autoreset=True)

def cls():
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux":
        os.system("clear")
    else:
        os.system("clear")

def print_center(text):
    print(text.center(shutil.get_terminal_size().columns))

def menu():
    cls()
    print_center(f"{Fore.LIGHTBLACK_EX} █████╗ ██╗██████╗ {Fore.LIGHTRED_EX}███████╗{Fore.YELLOW}██████╗  █████╗ ██████╗ ")
    print_center(f"{Fore.LIGHTBLACK_EX}██╔══██╗██║██╔══██╗{Fore.LIGHTRED_EX}╚══███╔╝{Fore.YELLOW}██╔══██╗██╔══██╗██╔══██╗")
    print_center(f"{Fore.LIGHTBLACK_EX}███████║██║██████╔╝{Fore.LIGHTRED_EX}  ███╔╝ {Fore.YELLOW}██████╔╝███████║██████╔╝")
    print_center(f"{Fore.LIGHTBLACK_EX}██╔══██║██║██╔══██╗{Fore.LIGHTRED_EX} ███╔╝  {Fore.YELLOW}██╔══██╗██╔══██║██╔══██╗")
    print_center(f"{Fore.LIGHTBLACK_EX}██║  ██║██║██║  ██║{Fore.LIGHTRED_EX}███████╗{Fore.YELLOW}██║  ██║██║  ██║██║  ██║")
    print_center(f"{Fore.LIGHTBLACK_EX}╚═╝  ╚═╝╚═╝╚═╝  ╚═╝{Fore.LIGHTRED_EX}╚══════╝{Fore.YELLOW}╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝")
