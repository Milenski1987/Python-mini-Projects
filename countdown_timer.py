import time
from colorama import Fore, Back

def countdown(t):

    while t >= 0:
        mins, secs = divmod(t, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(Back.BLACK + Fore.MAGENTA + f"\r{timer}", end="")
        time.sleep(1)
        t -= 1
    print(f"\nTime is over")

t = int(input(Fore.CYAN + "Enter time in seconds: "))

countdown(t)