from time import sleep
import sys

def move_cursor_up(lines):
    sys.stdout.write(f'\033[{lines}A')
    sys.stdout.flush()

def print_frame(frame):
    sys.stdout.write(frame)
    sys.stdout.flush()

frames = [
    """
                 
              
           
          
        . 
        . 
    """,
    """
              
           . 
          . 
        . .
        . .
      """,
    """
           . . 
          . . 
        . . .
        . . 
    """,
    """
              . 
           . . 
          . . .
        . . .   
        . .              
      """,
    """
                 . 
              . . 
           . . . 
          . . .               
        . . .                   
        . .                     
      """,
    """
                 . . 
              . . .    
           . . . . 
          . . .                
        . . .                  
        . .                     
      """,
    """
                 . . . 
              . . . .    
           . . . . .
          . . .             
        . . .                
        . .                    
      """,
    """
                 . . . . 
              . . . . .  
           . . . . . . 
          . . .                
        . . .                 
        . .                      
      """,
    """
                 . . . . .
              . . . . . .   
           . . . . . . . 
          . . .               
        . . .                
        . .                     
      """,
    """
                 . . . . .
              . . . . . . .   
           . . . . . . . . 
          . . .                
        . . .                  
        . .                    
      """,
    """
                 . . . . .
              . . . . . . . .   
           . . . . . . . . . 
          . . .              .   
        . . .                   
        . .                     
      """,
    """
                 . . . . .
              . . . . . . . .   
           . . . . . . . . . . 
          . . .              . .  
        . . .                  .   
        . .                     
      """,
    """
                 . . . . .
              . . . . . . . .   
           . . . . . . . . . . . 
          . . .              . . .  
        . . .                  . . 
        . .                      . 
      """,
    """
                 . . . . .
              . . . . . . . .   
           . . . . . . . . . . . 
          . . .              . . .  
        . . .                  . . . 
        . .                      . .
      """,
]

LINE_COUNT = 8  # número de linhas por frame

def slash_animation():
    # Imprime o primeiro frame
    print_frame(frames[0])

    for frame in frames[1:]:
        sleep(0.04)  # mais suave que 0.01
        move_cursor_up(LINE_COUNT)
        print_frame(frame)

    sleep(2)

slash_animation()