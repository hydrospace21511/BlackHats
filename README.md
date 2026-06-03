# DarkHats


This package contains the game archives and the launch script. Follow the instructions below to start playing.

---

## How to Play

### Prerequisites
*   **OS**: This game is designed for Windows 7/10/11 or Linux Mint/Ubuntu/Fedora/Arch
*   **CPU**: Required CPU: Intel Celeron N3060 / AMD E1-2100 **(Linux recommended for best performance)** |Recommended: Pentium 4
*   **RAM**: Required: 64 MB | Recommended: 128 / 256 MB
*   **GPU**: Required: Intel HD Graphics / AMD Radeon R2 | Recommended: Any dedicated GPU with OpenGL 2.0+ support
*   **Storage**: Required: 100 MB available space | Recommended: 300 MB available space

### Launch Guide

*Windows*

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

*Linux / MacOs*

1.  **Open the Game Folder**:
    Navigate to the directory where you extracted the game files. You should see this main item:
    *   A folder named `game`

2. **Checking the game path**
   After opening the Game folder, you should see those items:
   *    7 folders named `__pycache__, Attacks, Backup, Classes, Items, Main, Sounds
   *    4 Archives with one named requirements.txt
   If you saw those items, then you are in the correct folder. After entering in the correct folder, click on the searchbar and copy the path. It should be like this:
   *    /home/hydro/Workspace/DarkHats-1/Game (example)
   Copy it.

3. **Downloading the requirements**
   After copying the game path, open your Terminal and type:
*  $ sudo dnf install python3-pip
*  $ cd Workspace/DarkHats-1/Game (example)
*  $ python3 -m  pip install -r requirements.txt

4. **Executing the game**
   After downloading the requirements, type:
*  $ cd Main
*  $ python3 Menu.py

5.  **Play**:
*   Once the command is execute, the game should start

*It's so easy to run on Windows...*

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

---

# Developer Side

## Modding Guide

> **Important:** Always back up your original game files before editing the files

---

### How to Make Mods

1. Inside the Game main folder, will have folders named such as Main, Classes, Items, etc. Inside them, will have all the archives that make the game works. (These folders contain the actual game logic **.py files**)

2. To modify them, you can simply alterate the name, damage or attack itself, Example:

    class ExampleClass:        
    def __init__(self):  
        self.raceName = "Example Name"
        self.Integrity = 85  
        etc...    
        self.Attacks = {  
            "Example Attack": 40, 
            etc... 
        }   
        self.active_cooldowns = {
            "Example Attack": 1  
        }    

* *Note:* Never modify the ClassName (class ExampleClass) without changing or adding it on the Menu archive.
* The same repeats for SpecialAttacks

3. Have fun modding your game, it's pretty easy to modify!

*For any issue or question you have, fell free to call me in Discord! **Discord: marley21511***



