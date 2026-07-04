class RimuruClass:
    def __init__(self):
        self.raceName = "Rimuru"
        self.Integrity = 999
        self.Regen = 0
        self.Defense = 75
        self.Attacks = {
            "Desintegration": "nan",
            "Tell Your World": 75,
            "Miku Miku Beam": 80,
            "Miku Iwa Koi": 46
        }

    def RaceName(self):
        return self.raceName
    
    def MostraVida(self):
        return self.Integrity
    
    def Damage(self, D, Defense) :
        return D * (1 - Defense / 100)
    
    def MostraAtaques(self):
        return list(self.Attacks.keys())
