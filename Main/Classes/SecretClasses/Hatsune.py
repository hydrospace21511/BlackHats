class HatsuneMikuClass:
    def __init__(self):
        self.raceName = "Vocaloid"
        self.Integrity = 2007
        self.Regen = 0
        self.Defense = 45
        self.Attacks = {
            "World Is Mine": 201,
            "Tell Your World": 75,
            "Miku Miku Beam": 80,
            "Microphone Throw": 80
        }

    def RaceName(self):
        return self.raceName
    
    def MostraVida(self):
        return self.Integrity
    
    def Damage(self, D, Defense) :
        return D * (1 - Defense / 100)
    
    def MostraAtaques(self):
        return list(self.Attacks.keys())
