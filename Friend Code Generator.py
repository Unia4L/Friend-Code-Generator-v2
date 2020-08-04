import math
import ctypes
import time
import os
from random import randint
clear = lambda: os.system('cls')
title = ctypes.windll.kernel32.SetConsoleTitleW
name = "Friend code generator"
ver = "2.0.5"

def menu():
    print("")
    print("----------------------")
    print(" 1 - 3ds/Wii-U friend code generator")
    print(" 2 - Switch friend code generator")
    print(" 3 - Steam friend code generator")
    print(" 4 - Clear Codes.txt")
    print("-----------------------")
    print("")
    print("Type 1, 2, 3 or 4 then press ENTER")
    title("[" + str(ver) + "] " + str(name))
    x = input("")
    if x == "1":
        clear()
        wiiu()
    if x == "2":
        clear()
        switch()
    if x == "3":
        clear()
        steam()
    if x == "4":
        time.sleep(0.2)
        os.remove("Codes.txt")
        file = open("Codes.txt","w") 
        print("Deleted!")
        file.close()
        time.sleep(1)
        clear()
        menu()
    else:
        print("Wrong input. Choose 1 to 4.")
        time.sleep(0.5)
        clear()
        menu()


def wiiu():
    global total
    time.sleep(0.2)
    os.remove("Codes.txt")
    file = open("Codes.txt","w")
    clear()
    print("3ds and Wii-U Friend Code Generator")
    print("")
    print("How many codes to generate: ")
    amt = int(input())
    print("Generating...")
    total = 0
    total1 = 0
    file = open("codes.txt","w") 
    while total < amt:
        pc = 200/(int(amt)+(int(total)))
        total1 + 1
        fc = str(randint(1000, 9999)) + "-" + str(randint(1000, 9999)) + "-" + str(randint(1000,9999))
        total = total+1
        if total % 1000 == 0:
            title(str(name) + " - " + str(round(total*pc)) + "% completed")
        file.write(str(fc)+"\n")
    clear()
    file.close()
    if total == 1:
        print("Completed! Generated "+ str(total) +" code!")
    else:
        print("Completed! Generated "+ str(total) +" codes!")
    title("Friend Code Generator - 2.0.4")
    input("Press enter to close! Thanks for using!")
    close()

def switch():
    time.sleep(0.2)
    os.remove("Codes.txt")
    file = open("Codes.txt","w")
    clear()
    print("Switch Friend Code Generator")
    print("")
    print("How many codes to generate: ")
    amt = int(input())
    print("Generating...")
    total = 0
    file = open("Codes.txt","w") 
    while total < amt:
        pc = 200/(int(amt)+(int(total)))
        fc = str(randint(1000, 9999)) + "-" + str(randint(1000, 9999)) + "-" + str(randint(1000,9999))
        total = total+1
        if total % 1000 == 0:
            title(str(name) + " - " + str(round(total*pc)) + "% completed")
        file.write("SW-" + str(fc)+"\n")
    clear()
    file.close()
    finish()


def steam():
    time.sleep(0.2)
    os.remove("Codes.txt")
    file = open("Codes.txt","w")
    clear()
    print("Steam Friend Code Generator")
    print("")
    print("How many codes should be generated? ")
    amt = int(input())
    print("Generating...")
    total = 0
    file = open("Codes.txt","w")
    while total < amt:
        pc = 200/(int(amt)+(int(total)))
        fc = str(randint(0,999999999))
        total = total+1
        if total % 100 == 0:
            title(str(name) + " - " + str(round(total*pc)) + "% completed")
        file.write(str(fc)+"\n")
    clear()
    file.close()
    finish()

def finish():
    print("Completed!")
    title("[" + str(ver) + "] " + str(name))
    input("Press enter to close.")
    exit()

menu()
