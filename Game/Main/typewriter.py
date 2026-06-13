import sys, time
from colorama import Fore, init

# Inicializa o colorama
init(autoreset=True)

def typewrite(text, border_color_name, text_color_name=None, speed=0.05):
    # Se você não passar uma cor para o texto, ele usa a mesma cor da borda
    if text_color_name is None:
        text_color_name = border_color_name
        
    # Transforma as strings nos códigos de cor reais do Colorama
    border_color = getattr(Fore, border_color_name.upper(), Fore.WHITE)
    text_color = getattr(Fore, text_color_name.upper(), Fore.WHITE)
    
    lines = text.split('\n')
    length = max(len(l) for l in lines)

    # Imprime a caixa de texto usando a cor da borda
    print(f"{border_color}╔{'═' * (length + 4)}╗\n" + "".join(f"║{' ' * (length + 4)}║\n" for _ in lines) + f"╚{'═' * (length + 4)}╝")
    
    # Move o cursor para cima para começar a digitar dentro da caixa
    sys.stdout.write(f"\033[{len(lines) + 1}A")
    
    for line in lines:
        sys.stdout.write(f"{border_color}║  ") # Borda da esquerda
        
        for letter in line:
            # AQUI ESTÁ O SEGREDO: Pintamos a letra exatamente antes de escrevê-la
            sys.stdout.write(f"{text_color}{letter}") 
            sys.stdout.flush()
            time.sleep(speed)
        
        # Move o cursor para a direita para pular a borda final e desce uma linha
        sys.stdout.write(f"\033[{length + 4}G\n")

#1 cor e 2 cor

