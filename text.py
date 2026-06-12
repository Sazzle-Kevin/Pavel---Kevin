import time
import sys
import os


def slow_print(
    speaker, text, sleep=0.3, delay=0.05, rows=50, resume="Placeholder", fresh=True
):
    if fresh:
        clear_screen()
    print()
    if speaker:
        print(speaker, ": ", end="")
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(delay)
    time.sleep(sleep)
    while resume != "":
        resume = input("")


def clear(rows):
    print("\n" * (rows - 1))


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
