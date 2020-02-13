import math
import ctypes
import time
import os
from random import randint
clear = lambda: os.system('cls')
ctypes.windll.kernel32.SetConsoleTitleW("Friend Code Generator - 2.0.3")

def menu():
    choicemenu = 0
    print("Last Update - 13th February 2020")
    print("----------------------")
    print(" 1 - 3ds/Wii-U Friend Code Generator")
    print(" 2 - Switch Friend Code Generator")
    print(" 3 - Clear Codes.txt")
    print("-----------------------")
    print("")
    print("Type 1, 2 or 3 then press ENTER")
    choicemenu = input("")
    if choicemenu == "1":
        clear()
        wiiu()
    if choicemenu == "2":
        clear()
        switch()
    if choicemenu == "3":
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
    time.sleep(0.2)
    track = 100000
    os.remove("Codes.txt")
    file = open("Codes.txt","w")
    clear()
    print("3ds and Wii-U Friend Code Generator")
    print("")
    print("How many codes to generate: ")
    amt = int(input())
    print("Generating...")
    total = 0
    file = open("codes.txt","w") 
    while total < amt:
        fcpt1 = str(randint(1000, 9999)) + "-" + str(randint(1000, 9999)) + "-" + str(randint(1000,9999))
        total = total+1
        if total == track:
            print(str(total) + " generated.")
            track = track + 100000
        file.write(str(fcpt1)+"\n")
    clear()
    file.close()
    if total == 1:
        print("Completed! Generated "+ str(total) +" code!")
    else:
        print("Completed! Generated "+ str(total) +" codes!")
    ctypes.windll.kernel32.SetConsoleTitleW("Friend Code Generator - 2.0.2")
    a = input("Press enter to close! Thanks for using!")
    close()

def switch():
    time.sleep(0.2)
    track = 100000
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
        fcpt1 = str(randint(1000, 9999)) + "-" + str(randint(1000, 9999)) + "-" + str(randint(1000,9999))
        total = total+1
        if total == track:
            print(str(total) + " generated.")
            track = track + 100000
        file.write("SW-" + str(fcpt1)+"\n")
    clear()
    file.close()
    if total == 1:
        print("Completed! Generated "+ str(total) +" code!")
    else:
        print("Completed! Generated "+ str(total) +" codes!")
    ctypes.windll.kernel32.SetConsoleTitleW("Friend Code Generator - 2.0.2")
    a = input("Press enter to close! Thanks for using!")
    close()
        

menu()
