import ctypes
import math
import os
import time
from contextlib import suppress
from random import randint

name = "Friend code generator"
ver = "2.0.5"
titles = [
    "3ds and Wii-U Friend Code Generator",
    "Switch Friend Code Generator",
    "Steam Friend Code Generator"
]


def menu():
    ctypes.windll.kernel32.SetConsoleTitleW("[{}] {}".format(ver, name))
    while True:
        try:
            selection = int(input(
                """
            ----------------------
            1 - 3ds/Wii-U friend code generator
            2 - Switch friend code generator
            3 - Steam friend code generator
            4 - Clear Codes.txt
            -----------------------
            Type 1, 2, 3 or 4 then press ENTER
            """))
            os.system('cls')
            if not 1 <= selection <= 4:
                raise ValueError

            if os.path.exists("Codes.txt"):
                os.remove("Codes.txt")

            if selection != 4:
                generate_codes(selection)
                break
            else:
                print("Deleted codes!")
                time.sleep(1)
                continue
        except (ValueError, IndexError):
            print("Wrong input. Choose 1 to 4.")
            time.sleep(1.0)
            continue

    with suppress(Exception):
        ctypes.windll.kernel32.SetConsoleTitleW("[{}] {}".format(ver, name))
        input("Press any key to close.")
    exit()


def generate_codes(selection):
    amount = int(input("{}\nHow many codes to generate:\n".format(titles[selection - 1])))
    print("Generating...")
    with open("Codes.txt", "w") as file:
        for counter in range(amount):
            if selection != 3:
                friend_code = "{}-{}-{}\n".format(
                    randint(1000, 9999), randint(1000, 9999), randint(1000, 9999)
                )
                if selection == 2:
                    friend_code = "SW-" + friend_code
                file.write(friend_code)
            else:
                file.write(f'{randint(0, 999999999)}\n')
            ctypes.windll.kernel32.SetConsoleTitleW(
                "{} - {:.2f}% completed".format(name, (counter + 1) * 100 / amount)
            )
    os.system('cls')
    print("Completed! Generated {} {}!".format(amount, 'codes' if amount != 1 else 'code'))


if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        exit(1)
