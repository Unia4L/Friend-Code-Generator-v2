import math
import ctypes
import time
import os
from random import randint
clear = lambda: os.system('cls')
ctypes.windll.kernel32.SetConsoleTitleW("Friend Code Generator - 2.0.0")

def menu():
    print("Last Update 4th January 2020")
    print("----------------------")
    print(" 1 - 3ds/WiiU Friend Code Generator")
    print(" 2 - Switch Friend Code Generator")
    print(" 3 - Clear Codes.txt")
    print(" 4 - Settings")
    print("-----------------------")
    print("")
    print("Type 1, 2, 3 or 4 then press ENTER")
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
        print("Done! Closing in 1 second...")
        time.sleep(1)
        exit()
    if choicemenu == "4":
        clear()
        input("Feature coming soon")
    else:
    	print("Wrong input. Choose 1 to 4.")
    	input()


def wiiu():
    time.sleep(0.2)
    os.remove("Codes.txt")
    file = open("Codes.txt","w")
    clear()
    print("3ds and Wii-U Friend Code Generator")
    print("")
    print("How many codes do you want to generate")
    amt = int(input())
    print("Press enter to generate " + str(amt) + " 3ds/Wii-U friend codes.")
    total = 0
    file = open("codes.txt","w") 
    while total < amt:
        fcpt1 = randint(1000, 9999)
        fcpt2 = randint(1000, 9999)
        fcpt3 = randint(1000, 9999)
        total = total+1
        code = str(fcpt1)+"-"+str(fcpt2)+"-"+str(fcpt3)
        file.write(code+"\n")
        ctypes.windll.kernel32.SetConsoleTitleW("Friend Code Generator - 2.0.0 "+ str(total) +" generated")
    clear
    print("Completed! Generated "+ str(total) +" codes!")
    ctypes.windll.kernel32.SetConsoleTitleW("Friend Code Generator - 2.0.0")
    a = input("Press enter to close! Thanks for using!")
    close()

def switch():
    time.sleep(0.2)
    os.remove("Codes.txt")
    file = open("Codes.txt","w")
    clear()
    print("Switch Friend Code Generator")
    print("")
    print("How many codes do you want to generate")
    amt = int(input())
    print("Press enter to generate " + str(amt) + " 3ds/Wii-U friend codes.")
    total = 0
    file = open("codes.txt","w") 
    while total < amt:
        fcpt1 = randint(1000, 9999)
        fcpt2 = randint(1000, 9999)
        fcpt3 = randint(1000, 9999)
        total = total+1
        code = "SW-"+str(fcpt1)+"-"+str(fcpt2)+"-"+str(fcpt3)
        file.write(code+"\n")
        ctypes.windll.kernel32.SetConsoleTitleW("Friend Code Generator - 2.0.0 "+ str(total) +" generated")
    clear()
    print("Completed! Generated "+ str(total) +" codes!")
    ctypes.windll.kernel32.SetConsoleTitleW("Friend Code Generator - 2.0.0")
    a = input("Press enter to close! Thanks for using!")
    close()
        

menu()
