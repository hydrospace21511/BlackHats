from colorama import Fore, Back, Style, init

init(autoreset=True)

def color(message, type="info"):
    match type:
        case "red":
            print(f"{Fore.RED}[!] {message}")
        case "yellow":
            print(f"{Fore.Yellow}[!]{message}")
color("OI", "red")
print("OIE 2")
