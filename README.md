# DarkHats


This package contains the game archives and the launch script. Follow the instructions below to start playing.

---

## How to Play

### Prerequisites
*   **OS**: This game is designed for Windows 10/11 or Linux Mint/Ubuntu/Fedora
*   **CPU**: Required CPU: Intel Celeron N3060 or AMD E1-2100, Recommended: Pentium 4
*   **RAM**: Required RAM: DDR 512MB, Recommended: DDR2 2GB
*   **GPU**: Required GPU: Integrated Graphics, Recommended: GeForce 210
*   **Storage**: Required Storage: 100MB, Recommended: 300MB

### Launch Guide

1.  **Open the Game Folder**:
    Navigate to the directory where you extracted the game files. You should see two main items:
    *   A folder named `game`
    *   A file named `Game.bat`

2.  **Run the File**:
    *   **Double-click** on the `Game.bat` file
    *   *Note:* A black command window might appear briefly. **Do not close it immediately.** If it closes too fast, an error occurred

3.  **Play**:
    *   Once the command window download all the requirements, the game should launch automatically

4. **Executing it again**
    *   Once all requirements are downloaded, it will not install again

---

##  Troubleshooting

### "The game window opens and return No module named pygame"
This usually means the script cannot find the `pygame` module
*   **Check**: Ensure you are in the newest version and all the files are correctly inside in game folder
*   **Check**: Make sure you didn't changed the main folder name (As Darkhats or Game)

### "Access Denied" or "Permission Error"
If you see an error about permissions:
1.  Right-click the `Game.bat` file
2.  Select **Run as administrator**

---

## Developer Notes
*   **Folder Structure**: The launcher expects the `Game` folder to exist in the root directory, moving files around may break the path
*   **Antivirus**: Some security suites might flag `Game.bat` files or bundled executables, if the game is blocked, add an exception for the game folder

---

**Enjoy the game!**

-- Developer Side

# Modding Guide

> **Important:** Always back up your original game files before editing the files

---

## How to Make Mods

1. Inside the Game main folder, will have folders named such as Main, Classes, Items, etc. Inside them, will have all the archives that make the game works. (These folders contain the actual game logic **.py files**)

2. To modify them, you can simply alterate the name, damage or attack itself, Example:

    class ExampleClass:                                 class ExampleClass:    
    def __init__(self):                                 def __init__(self):
        self.raceName = "Example Name"                      self.raceName = "Modded Class"
        self.Integrity = 85                                 self.Integrity = 201
        etc...                                              etc...
        self.Attacks = {                     --->           self.Attacks = {   
            "Example Attack": 40,                                "Modded Attack": 90,
            etc...                                               etc...
        }                                                   }
        self.active_cooldowns = {                           self.active_cooldowns = {
            "Example Attack": 1                                 "Modded Attack": 4    -- in rounds      
        }                                                   }    

* *Note:* Never modify the ClassName (class ExampleClass) without changing or adding it on the Menu archive.
* The same repeats for SpecialAttacks

3. Have fun modding your game, it's pretty easy to modify!

*For any issue or question you have, fell free to call me in Discord! **Discord: marley21511***



