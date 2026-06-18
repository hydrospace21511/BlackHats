import sys, time
from colorama import Fore, init

init(autoreset=True)

def typewrite(text, border_color_name, text_color_name=None, speed=0.05):
    if text_color_name is None:
        text_color_name = border_color_name

    border_color = getattr(Fore, border_color_name.upper(), Fore.WHITE)
    text_color = getattr(Fore, text_color_name.upper(), Fore.WHITE)
    
    lines = text.split('\n')
    length = max(len(l) for l in lines)

    print(f"{border_color}╔{'═' * (length + 4)}╗\n" + "".join(f"║{' ' * (length + 4)}║\n" for _ in lines) + f"╚{'═' * (length + 4)}╝")
    
    sys.stdout.write(f"\033[{len(lines) + 1}A")
    
    for line in lines:
        sys.stdout.write(f"{border_color}║  ") 
        
        for letter in line:
            sys.stdout.write(f"{text_color}{letter}") 
            sys.stdout.flush()
            time.sleep(speed)
        
        sys.stdout.write(f"\033[{length + 4}G\n")

#1 cor e 2 cor

