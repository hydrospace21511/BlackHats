class SocialEngineerClass:
    def __init__(self):
        self.raceName = "Social Engineer"
        self.Integrity = 50
        self.Defense = 45
        self.Regen = 0
        self.stun = 0

        self.Attacks = {
            "Internal Access": 5,
            "Phishing": 30,
            "Pretexting": 50,
            "Baiting": 5,
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
    