from Classes.SecurityAnalyticClass import SecurityAnalyticClass
from Classes.HackerClass import HackerClass
from Classes.SocialEngineerClass import SocialEngineerClass
from colorama import Fore, Style
class Classes:


    def __init__(self):
        pass
    def _Classes(self):
            # Paleta de cores do Mainframe
            C_B = Fore.GREEN       # Borda
            C_T = Fore.YELLOW     # Título
            C_C = Fore.CYAN       # Nome das Classes
            C_D = Fore.WHITE                     # Descrição
            R = Style.RESET_ALL                  # Reset
            C_R = Fore.RED

            # Construção milimétrica para não quebrar a largura de 56 caracteres
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
            
            print(f"{C_B}╚{'═'*56}╝{R}")
            
    def ClassesAttacks(self):
        return {
        print(f""")
   > 1. "Hacker": {HackerClass().MostraAtaques()}\n
   > 2. "Security Analytic": {SecurityAnalyticClass().MostraAtaques()}\n
   > 3. "Social Engineer": {SocialEngineerClass().MostraAtaques()}\n
              """)
        }
