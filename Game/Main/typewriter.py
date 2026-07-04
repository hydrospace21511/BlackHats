import sys, time, pygame, os
from colorama import Fore, Style, init
from time import sleep
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

pygame.mixer.init()
attack_archive = os.path.dirname(os.path.abspath(__file__))
root_archive = os.path.dirname(attack_archive)
Talk = os.path.join(root_archive, "Sounds", "artificiallyinspired-alien-high-pitch-312010.mp3")

init()

MASC_FRAMES = [
    ["█ █           █ █","████ ▄▄▄▄▄▄▄ ████","█████████████████","█████  ███  █████","█████████████████"," ▀█████████████▀ ","  ██         ██  ","▄▄█           █▄▄"],
    ["█ █           █ █","████ ▄▄▄▄▄▄▄ ████","█████████████████","█████  ███  █████","███████▀▀▀███████"," ▀█████████████▀ ","  ██         ██  ","▄▄█           █▄▄"],
    ["█ █           █ █","████ ▄▄▄▄▄▄▄ █░██","███████████████░█","█████  ███  █████","████████▀████████"," ▀█████████████▀ ","  ██         ██  ","▄▄█           █▄▄"],
    ["█ █           █ █","████ ▄▄▄▄▄▄▄ ████","█████████████████","█████  ███  █████","███████ ▀ ███████"," ▀█████████████▀ ","  ▄█▀         ██  ","▄█▀           █▄▄"]
]

SOUND_DURATION = 8.0   
FADE_OUT_MS    = 2000 

def typewriter(text, speed=0.05, anim_speed=2.0):
    #pygame.mixer.music.load(Talk)
    #pygame.mixer.music.play(loops=-1) 

    GREEN = Fore.GREEN
    RESET = Style.RESET_ALL
    print()

    lines = text.split('\n')
    length = max(len(l) for l in lines)

    text_size = len(lines) + 2
    size_mascot = len(MASC_FRAMES[0])
    total_size = max(text_size, size_mascot)

    column_mascot = length + 12

    total_chars = sum(len(l) for l in lines)
    total_duration = total_chars * speed

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
    fade_triggered = False

    for i, v in enumerate(lines):
        sys.stdout.write(f"{GREEN}║  ")
        for char in v:
            elapsed = time.time() - start_time
            if not fade_triggered and elapsed >= total_duration - (FADE_OUT_MS / 1000):
               # pygame.mixer.music.fadeout(FADE_OUT_MS)
                fade_triggered = True

            frame = int(elapsed / anim_speed) % len(MASC_FRAMES)

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

      #  pygame.mixer.music.fadeout(FADE_OUT_MS)

    sys.stdout.write(RESET)
    print()

import unicodedata

def visual_len(s):
    total = 0
    for ch in s:
        w = unicodedata.east_asian_width(ch)
        total += 2 if w in ('W', 'F') else 1
    return total

import shutil

def text(text, border_color_name, text_color_name=None, speed=0.05, max_width=100):
    if text_color_name is None:
        text_color_name = border_color_name

    border_color = getattr(Fore, border_color_name.upper(), Fore.WHITE)
    text_color   = getattr(Fore, text_color_name.upper(), Fore.WHITE)

    terminal_w = min(max_width, shutil.get_terminal_size().columns - 6)

    raw_lines = text.split('\n')
    lines = []
    for line in raw_lines:
        while visual_len(line) > terminal_w:
            lines.append(line[:terminal_w])
            line = line[terminal_w:]
        lines.append(line)

    length = max(visual_len(l) for l in lines)

    print(f"{border_color}╔{'═' * (length + 4)}╗")
    for _ in lines:
        print(f"{border_color}║{' ' * (length + 4)}║")
    print(f"{border_color}╚{'═' * (length + 4)}╝")

    sys.stdout.write(f"\033[{len(lines) + 1}A")

    for line in lines:
        sys.stdout.write(f"{border_color}║  ")

        for letter in line:
            sys.stdout.write(f"{text_color}{letter}")
            sys.stdout.flush()
            time.sleep(speed)

        padding = length - visual_len(line)
        sys.stdout.write(f"{' ' * padding}\033[{length + 4}G\n")

#text("Bao? so teu bagui ai, trabalhe blablablablablablablablabla", "GREEN", "GREEN")
# input("Press enter to continue")
# typewriter("bom?", speed=0.06, anim_speed=3)