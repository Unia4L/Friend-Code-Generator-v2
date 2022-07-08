import ctypes
import os
from random import randint

clear = lambda: os.system('cls')
title = ctypes.windll.kernel32.SetConsoleTitleW
ver = "2.0.5"

def generator(amount, type):
    file = open("codes.txt","w")
    total = 0
    for i in range(total, amount):
        total += 1
        match type:
            case 0:
                friendcode = f"{str(randint(1000,9999))}-{str(randint(1000,9999))}-{str(randint(1000,9999))}"
                title(f"Codes generated: {total}")
            case 1:
                friendcode = f"SW-{str(randint(1000,9999))}-{str(randint(1000,9999))}-{str(randint(1000,9999))}"
                title(f"Codes generated: {total}")
            case 2:
                friendcode = str(randint(1,999999999))
                title(f"Codes generated: {total}")
        file.write(f"{friendcode}\n")
    file.close()
    input("Generation finished! Press enter to close")


def menu():
    clear()
    title(f"Friend Code Generator {ver}")
    while True:
        try:
            amount = int(input("Codes to generate: "))
            break
        except Exception:
            print("Put a valid number.")
    clear()
    print("What type of code do you want to generate?")
    print(" 1 - 3ds/Wii-U friend code generator")
    print(" 2 - Switch friend code generator")
    print(" 3 - Steam friend code generator")
    print("")
    print(f"Generating - {amount} codes.")
    print("Type 1, 2 or 3 then press ENTER")
    while True:
        x = input("")
        if x.isnumeric():
            x = int(x)
            match x:
                case 1:
                    clear()
                    generator(amount, 0)
                case 2:
                    clear()
                    generator(amount, 1)
                case 3:
                    clear()
                    generator(amount, 2)
                case _:
                    print("Put a number between 1-3")
                    continue
        else:
            print("Put a number")
            continue
menu()
