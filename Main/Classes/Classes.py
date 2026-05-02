from Classes.SecurityAnalyticClass import SecurityAnalyticClass
from Classes.HackerClass import HackerClass
from Classes.SocialEngineerClass import SocialEngineerClass

class Classes:


    def __init__(self):
        pass
    def Classes(self):
        return ("""
    The classes are:
   > 1. Hacker                
   > 2. Security Analytic
   > 3. Social Engineer             
                """)
    def ClassesAttacks(self):
        return {
        print(f""")
   > 1. "Hacker": {HackerClass().MostraAtaques()}\n
   > 2. "Security Analytic": {SecurityAnalyticClass().MostraAtaques()}\n
   > 3. "Social Engineer": {SocialEngineerClass().MostraAtaques()}\n
              """)
        }