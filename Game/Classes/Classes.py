from Game.Classes.SecurityAnalyticClass import SecurityAnalyticClass
from Game.Classes.HackerClass import HackerClass
from Game.Classes.SocialEngineerClass import SocialEngineerClass
from colorama import Fore, Style
class Classes:


    def __init__(self):
        pass
    def _Classes(self):
            C_B = Fore.GREEN      
            C_T = Fore.YELLOW
            C_C = Fore.CYAN      
            C_D = Fore.WHITE                  
            R = Style.RESET_ALL                
            C_R = Fore.RED


            print(f"{C_B}╔{'═'*56}╗{R}")          
                                                                                       
            print(f"{C_B}║{C_D}{f'                         Classes                      {C_R}X ':^56}{C_B}║{R}")
            print(f"{C_B}╠{'═'*56}╣{R}")
            print(f"{C_B}║{' '*56}║{R}")
            
            # HACKER
            print(f"{C_B}║  {C_B}▶ [1] HACKER{R}{C_B}{' '*42}║{R}")
            print(f"{C_B}║      {C_D}> Focus: Raw damage & system exploitation.{R}{C_B}{' '*8}║{R}")
            print(f"{C_B}║{' '*56}║{R}")
            
            # SECURITY ANALYTIC
            print(f"{C_B}║  {C_B}▶ [2] SECURITY ANALYTIC{R}{C_B}{' '*31}║{R}")
            print(f"{C_B}║      {C_D}> Focus: Ironclad defense & node integrity.{R}{C_B}{' '*7}║{R}")
            print(f"{C_B}║{' '*56}║{R}")
            
            # SOCIAL ENGINEER
            print(f"{C_B}║  {C_B}▶ [3] SOCIAL ENGINEER{R}{C_B}{' '*33}║{R}")
            print(f"{C_B}║      {C_D}> Focus: Manipulation, regen & bypass.{R}{C_B}{' '*12}║{R}")
            print(f"{C_B}║{' '*56}║{R}")
            print(f"{C_B}║{'  << Previous':<18}{'1':^20}{'Next >>  ':>18}║{R}")
            print(f"{C_B}╚{'═'*56}╝{R}")

    
    def _Classes2(self):
            C_B = Fore.GREEN      
            C_T = Fore.YELLOW
            C_C = Fore.CYAN      
            C_D = Fore.WHITE                  
            R = Style.RESET_ALL                
            C_R = Fore.RED


            print(f"{C_B}╔{'═'*56}╗{R}")          
                                                                                       
            print(f"{C_B}║{C_D}{f'                         Classes                      {C_R}X ':^56}{C_B}║{R}")
            print(f"{C_B}╠{'═'*56}╣{R}")
            print(f"{C_B}║{' '*56}║{R}")
            
            #REVERSE ENGINEER
            print(f"{C_B}║  {C_B}▶ [4] REVERSE ENGINEER{R}{C_B}{' '*32}║{R}")
            print(f"{C_B}║      {C_D}> Focus: Decompilation & adaptive attacks.{R}{C_B}{' '*8}║{R}")
            print(f"{C_B}║{' '*56}║{R}")

            #HARDWARE SPECIALIST
            print(f"{C_B}║  {C_B}▶ [5] HARDWARE SPECIALIST{R}{C_B}{' '*29}║{R}")
            print(f"{C_B}║      {C_D}> Focus: Hardware manipulation & optimization.{R}{C_B}{' '*4}║{R}")
            print(f"{C_B}║{' '*56}║{R}")

            #SECURITY BYPASSER
            print(f"{C_B}║  {C_B}▶ [6] SECURITY BYPASSER{R}{C_B}{' '*31}║{R}")
            print(f"{C_B}║      {C_D}> Focus: Bypassing security measures & stealth.{R}{C_B}{' '*3}║{R}")
            print(f"{C_B}║{' '*56}║{R}")
            print(f"{C_B}║{'  << Previous':<18}{'2':^20}{'Next >>  ':>18}║{R}")
            print(f"{C_B}╚{'═'*56}╝{R}")  
    
    def _Classes3(self):
            C_B = Fore.GREEN      
            C_T = Fore.YELLOW
            C_C = Fore.CYAN      
            C_D = Fore.WHITE                  
            R = Style.RESET_ALL                
            C_R = Fore.RED


            print(f"{C_B}╔{'═'*56}╗{R}")          
                                                                                       
            print(f"{C_B}║{C_D}{f'                         Classes                      {C_R}X ':^56}{C_B}║{R}")
            print(f"{C_B}╠{'═'*56}╣{R}")
            print(f"{C_B}║{' '*56}║{R}")
            
            #PLACE HOLDER~~CHAN 
            print(f"{C_B}║  {C_B}▶ [0] Placeholder{R}{C_B}{' '*37}║{R}")
            print(f"{C_B}║      {C_D}> Focus: Just an useless placeholder{R}{C_B}{' '*14}║{R}")
            print(f"{C_B}║{' '*56}║{R}")
            print(f"{C_B}║{'  << Previous':<18}{'3':^20}{'Next >>  ':>18}║{R}")
            print(f"{C_B}╚{'═'*56}╝{R}")   

    def ClassesAttacks(self):
        return {
        print(f""")
   > 1. "Hacker": {HackerClass().MostraAtaques()}\n
   > 2. "Security Analytic": {SecurityAnalyticClass().MostraAtaques()}\n
   > 3. "Social Engineer": {SocialEngineerClass().MostraAtaques()}\n
              """)
        }
