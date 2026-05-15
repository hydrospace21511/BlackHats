from colorama import Fore, Back, Style, init

def cText(message, type="info"):
    match type:
         case "red":
             print(f"{Fore.RED}{message}")
         case "yellow":
             print(f"{Fore.YELLOW}{message}")
         case "green":
              print(f"{Fore.GREEN}{message}")
         case "blue":
            print(f"{Fore.BLUE}{message}")
         case "cyan":
            print(f"{Fore.CYAN}{message}")
         case "black":
            print(f"{Fore.BLACK}{message}")
         case "error":
            print(f"{Fore.RED}[!] {message}")
         case "warn":
            print(f"{Fore.YELLOW}[!]{message}")
         case "positive":
            print(f"{Fore.GREEN}[✓]{message}")
        
                
    
