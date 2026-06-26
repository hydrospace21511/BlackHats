import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from Game.Main.COBALT import COBALT, COBALT_FS
from colorama import init
init(autoreset=True)

sistema = COBALT()
sistema._check_space()
explorer = COBALT_FS()
explorer.run()
sistema.start()

