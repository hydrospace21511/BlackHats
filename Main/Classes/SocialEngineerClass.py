class SocialEngineerClass:
    def __init__(self):
        self.raceName = "Social Engineer"
        self.Integrity = 50
        self.Defense = 45
        self.Regen = 0
        self.stun = 0

        self.Attacks = {
            "Internal Access": self.Defense + 40,
            "Phishing": self.Defense + 20,
            "Pretexting": 50,
            "Baiting": self.Defense + 20,
            "God's Hand": 50000000,
        #   "God's Wrath": [Regen + 100000000, 1]
        }
    
    def RaceName(self):
        return self.raceName
    
    def MostraAtaques(self):
        return list(self.Attacks.keys())
    
    def Damage(self, D, Defense) :
        # print("Available attacks:", list(self.Attacks.keys()))
        return D * (1 - Defense / 100)
    