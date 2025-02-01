import time
from colorama import Fore, Back

def countdown(t: int) -> str:
    while t >= 0:
        minutes, seconds = divmod(t, 60)
        timer = f'{minutes:02d}:{seconds:02d}'
        print(Back.BLACK + Fore.MAGENTA + f"\r{timer}", end="")
        time.sleep(1)
        t -= 1
    return f"\nTime is over"

time_in_seconds = int(input(Fore.CYAN + "Enter time in seconds: "))

print(countdown(time_in_seconds))

