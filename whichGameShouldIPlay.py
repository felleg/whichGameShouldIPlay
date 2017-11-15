import random
import argparse
import sys
import time

def generateList(mFile):
    return mFile.read().splitlines()

normalGames = open("main_gamelist.txt", "r")
longGames = open("long_gamelist.txt", "r")
twoPGames = open("2P_gamelist.txt", "r")

gamelist_1P_normal = generateList(normalGames)
gamelist_1P_long = generateList(longGames)        
gamelist_2P = generateList(twoPGames)

gamelist = []

# Parsing user arguments
parser = argparse.ArgumentParser()
parser.add_argument('-med', help='Use this flag to suggest games average in completion time', action="store_true")
parser.add_argument('-long', help='Use this flag to suggest long games only', action="store_true")
parser.add_argument('-one', help='Use this flag to suggest one-player games only', action="store_true")
parser.add_argument('-two', help='Use this flag to suggest two-player games only', action="store_true")
parser.add_argument('-unl', help='Use this flag to enable unlimited suggestions (instead of 3)', action="store_true")
args = parser.parse_args()

if   args.med:
    print ("You selected medium length games.")
    gamelist = [gamelist_1P_normal]
elif args.long:
    print ("You selected long games.")
    gamelist = [gamelist_1P_long]
elif args.one:
    print("You selected 1P games.")
    gamelist = [gamelist_1P_normal, gamelist_1P_long]
elif args.two:
    print("You selected 2P games.")
    gamelist = gamelist_2P
else:
    print("You selected all games.")
    gamelist = [gamelist_1P_normal, gamelist_1P_long, gamelist_2P]

gamelist = [item for sublist in gamelist for item in sublist]
random.shuffle(gamelist)
counter = 0
limit = 3 if args.unl == None else len(gamelist)
while (counter < limit): 
    print ("Generating your game suggestion out of "+str(len(gamelist)-counter)+ " games", end=" ")
    c=0
    while (c<5):
        print("... ", end=" ", flush=True),
        c += 1
        time.sleep(1)
    print ("\n\n\t"+gamelist[counter])
    counter += 1
    choice = input("\nDo you accept this challenge? You still have "+str(limit - counter) +" suggestions left. (y/n): ")
    while(True):
        choice = choice.lower()
        if choice == 'y':
            print("THE GAME HAS BEEN SELECTED! ENJOY!")
            sys.exit()
        elif choice == 'n':
            if counter < limit:
                print("A new suggestion will be generated.\n")
                break
            else:
                print("You have no suggestions left! You are not very open minded.")
                sys.exit()
        else:
            choice = input("You must answer with either 'y' or 'n'. Try again: ")
