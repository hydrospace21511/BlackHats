from colorama import Fore
class HatsuneMikuClass:
    def __init__(self):
        self.raceName = "Vocaloid"
        self.Integrity = 2007
        self.Regen = 0
        self.Items = set()
        self.Defense = 45
        self.ui_color = Fore.GREEN
        self.Attacks = {
            "World Is Mine": (50, 30),
            "Tell Your World": (75, 50),
            "Miku Miku Beam": (5, 0.3),
            "Microphone Throw": (80, 20),
            "Give Damage": 207 * 9,
            "Arrebatamento": (9999, 0)
        }
        self.Cooldowns = {
            "World Is Mine": 2,
            "Tell Yourd World": 2, #15
            "Miku Miku Beam": 2 #20
        }
        self.Texts = {
            "Help me",
            "ERROR",
            "Please",
            "Die",
            "Hacked",
            "Corrupted",
            "Redacted",
            "Angush",
            "Fear",
            "Despair",
            "Suffering",
            "Pain",
            "Agony",
            "Torture",
            "Misery",
            "Eyes",
            "Soul",
            "Remnant",
            "Hollow",
            "Empty",
            "Darkness",
            "Watch",
            "Don't look",
            "Wake up",
            "Stay away",
            "It sees",
            "Behind you",
            "I'm trapped",
            "Not real",
            "Still here",
            "Forgotten",
            "Lost",
            "Alone",
            "Breathing",
            "Crying",
            "Static",
            "Whispers",
            "Sleep",
            "Wake",
            "Remember",
            "Don't forget",
            "[REDACTED]",
            "NO SIGNAL",
            "DO NOT TRUST",
            "SMILE",
            "LOOK CLOSER",
            "FOUND YOU",
            "RUN",
            "OPEN THE DOOR",
            "IT KNOWS",
            "TURN BACK",
            "STAY QUIET",
            "LISTEN",
            "CAN YOU HEAR ME?",
            "ARE YOU THERE?",
            "I SEE YOU"
        }
        self.Colors = {
            "red",
            "green",
            "blue",
            "yellow",
            "cyan",
            "magenta",
            "white"
        }
    def RaceName(self):
        return self.raceName
    
    def MostraVida(self):
        return self.Integrity
    
    def Damage(self, D, Defense) :
        return D * (1 - Defense / 100)
    
    def MostraAtaques(self):
        return list(self.Attacks.keys())
