import random
response = input("R to roll the dice or press S to stop playing:")
no = random.randint(1,6)

def dice(response):
    if(response == "r"):
        if(no == 1):
            print("---")
            print("[0]")
            print("---")
        if(no == 2):
            print("-----")
            print("[0 0]")
            print("-----")
        if(no == 3):
            print("-------")
            print("[0 0 0]")
            print("-------")
        if(no == 4):
            print("-----")
            print("[0 0]")
            print("[0 0]")
            print("-----")
        if(no == 5):
            print("-----")
            print("[0 0]")
            print("[ 0 ]")
            print("[0 0]")
            print("-----")
        if(no == 6):
            print("-------")
            print("[0 0 0]")
            print("[0 0 0]")
            print("-------")
    elif(response == "s"):
        print("THANKS FOR PLAYING WITH OUR DICE.HOPE YOU ENJOYED!!")
dice(str(response))