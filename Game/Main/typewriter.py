import sys, time
from colorama import Fore, Style, init

init()

MASC_FRAMES = [
    ["█ █           █ █","████ ▄▄▄▄▄▄▄ ████","█████████████████","█████  ███  █████","█████████████████"," ▀█████████████▀ ","  ██         ██  ","▄▄█           █▄▄"],
    ["█ █           █ █","████ ▄▄▄▄▄▄▄ ████","█████████████████","█████  ███  █████","███████▀▀▀███████"," ▀█████████████▀ ","  ██         ██  ","▄▄█           █▄▄"],
    ["█ █           █ █","████ ▄▄▄▄▄▄▄ █░██","███████████████░█","█████  ███  █████","████████▀████████"," ▀█████████████▀ ","  ██         ██  ","▄▄█           █▄▄"],
    ["█ █           █ █","████ ▄▄▄▄▄▄▄ ████","█████████████████","█████  ███  █████","███████ ▀ ███████"," ▀█████████████▀ ","  ▄█▀         ██  ","▄█▀           █▄▄"]
]

def typewriter(text, speed=0.05, anim_speed=2.0):
    GREEN = Fore.GREEN
    RESET = Style.RESET_ALL
    print()

    lines = text.split('\n')
    length = max(len(l) for l in lines)

    text_size = len(lines) + 2
    size_mascot = len(MASC_FRAMES[0])
    total_size = max(text_size, size_mascot)

    column_mascot = length + 12

    print('\n' * total_size, end="")
    sys.stdout.write(f"\033[{total_size}A")

    for i in range(total_size):
        sys.stdout.write("\r")

        if i == 0:
            sys.stdout.write(f"{GREEN}╔{'═' * (length + 4)}╗")
        elif i == text_size - 1:
            sys.stdout.write(f"{GREEN}╚{'═' * (length + 4)}╝")
        elif 0 < i < text_size - 1:
            sys.stdout.write(f"{GREEN}║{' ' * (length + 4)}║")

        if i < size_mascot:
            sys.stdout.write(f"\033[{column_mascot}G{GREEN}{MASC_FRAMES[0][i]}")

        sys.stdout.write("\n")

    sys.stdout.write(f"\033[{total_size - 1}A")

    start_time = time.time()
    last_frame = 0

    for i, v in enumerate(lines):
        sys.stdout.write(f"{GREEN}║  ")
        for char in v:
            frame = int((time.time() - start_time) / anim_speed) % len(MASC_FRAMES)

            if frame != last_frame:
                sys.stdout.write("\033[s")
                if i + 1 > 0:
                    sys.stdout.write(f"\033[{i + 1}A")
                for x in MASC_FRAMES[frame]:
                    sys.stdout.write(f"\033[{column_mascot}G{GREEN}{x}\033[1B")
                sys.stdout.write("\033[u")
                last_frame = frame

            sys.stdout.write(f"{GREEN}{char}")
            sys.stdout.flush()
            time.sleep(speed)

        sys.stdout.write(f"{GREEN}\033[{length + 6}G║\n")

    lines_left = total_size - text_size
    if lines_left > 0:
        sys.stdout.write(f"\033[{lines_left}B")

    sys.stdout.write(RESET)
    print()

#typewriter("thalles", speed=0.06, anim_speed=3)