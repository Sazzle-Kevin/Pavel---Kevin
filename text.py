import time
import sys


def slow_print(speaker, text, sleep=1, delay=0.05, rows=50):
    print("\n" * (rows - 1))
    if speaker:
        print(speaker, ": ", end="")
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(delay)
    time.sleep(sleep)


def clear(rows):
    print("\n" * (rows - 1))
