import os
from time import sleep
from colorama import Fore, Style, init
import getpass

init(autoreset=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class COBALT:
    def __init__(self):
        pass

    def _neofetch(self):
        clear()
        #ta linha por linha pq poor algum motivo as 3 aspa la nn tava funcionando e tava retornando erro
        DarkHat_raw = [
            r"                                     .--.                                  ",
            r"                      .-------.   .-+*%%*+----.                            ",
            r"                     -*%%%%%%%*+-+*%%%%%%%%%%%*+--.                        ",
            r"                    .*%%%%%%%%%%%%%%%%%%%%%%%%%%%%*+--.                    ",
            r"                    +%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*+.                  ",
            r"                   -*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*#                 ",
            r"                  .*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@* ",
            r"                  +%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%+                ",
            r"                 .*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*.               ",
            r"                @.*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%+               ",
            r"                @@.+*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*.              ",
            r"      .------- @@@@@.+*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%+              ",
            r"   .-+*%%%%%%%-@@@@@@@.-+*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*:             ",
            r" @+*%%%%%%%%%%+@@@@@@@@@@.-=*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%-             ",
            r" @%%%%%%%%%%%%*+:@@@@@@@@@@@----+*%%%%%%%%%%%%%%%%%%%%%%%%%%*.             ",
            r"@@%%%%%%%%%%%%%%*-@@@@@@@@@@@@@@@.----+*%%%%%%%%%%%%%%%%%*+-.@@ .          ",
            r" +%%%%%%%%%%%%%%%*+.@@@@@@@@@@@@@@@@@@@.-----------------.@@@@@-*+-.       ",
            r" .*%%%%%%%%%%%%%%%%*+-.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-%%%*+.     ",
            r"  .+*%%%%%%%%%%%%%%%%%*+-.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+%%%%%*+.   ",
            r"    @@@%%%%%%%%%%%%%%%%%%*+--.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.+*%%%%%%%*-  ",
            r"      @+*%%%%%%%%%%%%%%%%%%%%*+----.@@@@@@@@@@@@@@@@@@@@@@@:+*%%%%%%%%%%*- ",
            r"        .+*%%%%%%%%%%%%%%%%%%%%%%%%*+---------------------+#%%%%%%%%%%%%%*.",
            r"          .-+*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*.",
            r"             .-+*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%+ ",
            r"                .--+*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*. ",
            r"                    .--+*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*-  ",
            r"                        .---+*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*+.   ",
            r"                             .----+*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*+-.     ",
            r"                                   .-------+*%%%%%%%%%%%%%%*+-----         ",
            r"                                            .--------------:               "
        ]

        DarkHat = [line.ljust(75) for line in DarkHat_raw]
        
        #infos
        C_GREEN = Fore.GREEN
        C_WHITE = Fore.WHITE
        C_CYAN = Fore.CYAN

        info_sis = [  
            f"{C_GREEN}DarkHats@{getpass.getuser()}{Style.RESET_ALL}", 
            f"{C_WHITE}---------------------------------------{Style.RESET_ALL}",
            "",
            f"{C_GREEN}OS:{C_WHITE}         Cobalt OS (Fedora Edition) x86_64", 
            "",
            f"{C_GREEN}Host:{C_WHITE}       COBALT Terminal v1.0.0",
            "",
            f"{C_GREEN}Kernel:{C_WHITE}     6.5.0-secure-core",
            "",
            f"{C_GREEN}Uptime:{C_WHITE}     2 hours, 31 minutes",
            "",
            f"{C_GREEN}Packages:{C_WHITE}   2400 (rpm)",
            "",
            f"{C_GREEN}Shell:{C_WHITE}      bash 5.1.8",
            "",
            f"{C_GREEN}Resolution:{C_WHITE} 1920x1080",
            "",
            f"{C_GREEN}Terminal:{C_WHITE}   cobalt-term",
            "",
            f"{C_GREEN}CPU:{C_WHITE}        Cobalt Core X-12 (8/24) 4.200GHz 120W",
            "",
            f"{C_GREEN}Memory:{C_WHITE}     7266MiB / 32768MiB",
            "", "", "", "", 
            f"            {C_CYAN}[ PRESS SPACE TO HACK ]{Style.RESET_ALL}", 
        ]

        max_lenght = max(len(DarkHat), len(info_sis))
        #acho q o certo seria length mas enfim, é a quantidade de linhas do neofetch, pra garantir q o loop vai ler todas as linhas
        #print("\n" * 4) 
        
        for i in range(max_lenght):
            l_l = DarkHat[i] if i < len(DarkHat) else " " * 75
            l_r = info_sis[i] if i < len(info_sis) else ""
            
            print(f"  {Fore.GREEN}{l_l}{Style.RESET_ALL}        {l_r}")
        
        #print("\n" * 3)


game = COBALT()
game._neofetch()