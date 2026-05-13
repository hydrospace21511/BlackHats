import keyboard
class COBALT:
    def __init__(self):
        pass

    def Start(self):
        print("""
    ---------------------------------------------------------          
    ||                Welcome to DarkHats!                 ||
    ||                                                     ||         
    ||                                                     ||     
    ||                                                     ||
    ||               Press SPACE to start                  ||  
    ||                                                     ||    
    ||                                                     ||             
    ||                                                     ||                 
    ||                                                     ||                 
    ---------------------------------------------------------                                                  
    """)
        while True:
            if keyboard.is_pressed('space'):
                print("Starting COBALT...")
                break