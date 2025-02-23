import time
from colorama import Fore, Back


def countdown(t: int) -> str:
    minutes, seconds = divmod(t, 60)
    timer = f'{minutes:02d}:{seconds:02d}'
    return f"\r{timer}"


def main():
    time_in_seconds = int(input(Fore.CYAN + "Enter time in seconds: "))

    while time_in_seconds >= 0:
        print(Back.BLACK + Fore.MAGENTA + f"\r{countdown(time_in_seconds)}", end = "")
        time.sleep(1)
        time_in_seconds -= 1

    print()
    print("Time is over!!!")


main()