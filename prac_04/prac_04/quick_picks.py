"""
CP1404/CP5632 Practical
"Quick Pick" Lottery Ticket Generator
"""

import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6


def main():
    # Generate quick pick lottery tickets.
    number_of_picks = int(input("How many quick picks? "))
    for _ in range(number_of_picks):
        pick = generate_pick()
        print_pick(pick)


def generate_pick():
    # Generate a single quick pick with no repeated numbers, sorted ascending.
    pick = []
    while len(pick) < NUMBERS_PER_PICK:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in pick:
            pick.append(number)
    pick.sort()
    return pick


def print_pick(pick):
    # Print a quick pick with numbers aligned neatly.
    print(" ".join(f"{num:2}" for num in pick))


main()