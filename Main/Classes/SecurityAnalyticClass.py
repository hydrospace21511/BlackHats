class SecurityAnalyticClass:
     
    def __init__(self):
        self.raceName = "Security Analytic"
        self.Integrity = 125
        self.Defense = 0
        self.Regen = 0
        self.Attacks = {
            "Firewall": self.Defense + 30,
            "Security Patch": self.Regen + 30,
            "Weakness View": 30,
            "Punch": 50,
            "God's Hand": 50000000,
        #    "God's Wrath": Regen + 100000000,
        "Pneumoultramicroscopicsilicovolcanoconiotic": 'ball cancer'
        }

        self.Cooldowns = {
            "Firewall": 8,
            "Security Patch": 3, 
            "Weakness View": 3,
            "God's Hand": 999999   
        }
        
    def RaceName(self):
        return self.raceName
    
    def MostraVida(self):
        return self.Integrity

    #calculadora de dano (com a defesa)(tenho medo da conta q faz)
    def Damage(self, D, Defense) :
       # print("Available attacks:", list(self.Attacks.keys()))
        return D * (1 - Defense / 100)

    def Firewall(self):
        return 1
    
    def MostraAtaques(self):
        return list(self.Attacks.keys())