import random
import argparse
import sys
import time

gamelist_1P_normal = ["3-D Worldrunner",
        "Abadox",
        "Air Fortress",
        "Battle Kid Fortress of Peril",
        "Battle Kid 2: Mountain of Torment",
        "Castlevania III Dracula's Curse",
        "Cheetahmen II: The Lost Levels",
        "Contra",
        "Double Dragon II",
        "Dr Jekyll and Mr Hyde",
        "DuckTales",
        "Gun-Nac",
        "Gun.Smoke",
        "Gyruss",
        "Jackal",
        "Kid Icarus",
        "Kings of the Beach",
        "Low G Man",
        "Marble Madness",
        "Mario Invisible",
        "Mega Man 2",
        "Mike Tyson's Punch-Out!!",
        "Milon's Secret Castle",
        "Mystery Quest",
        "NES Open",
        "Ninja Gaiden",
        "Ninja Gaiden II",
        "Platoon",
        "R.C. Pro-AM",
        "Rad Racer",
        "Rollergames",
        "Sky Shark",
        "Solstice",
        "Strider",
        "Super C",
        "Super Mario Bros. 2",
        "Super Spike V' Ball",
        "Teenage Mutant Ninja Turtles",
        "Teenage Mutant Ninja Turtles 2 The Arcade Game",
        "Axelay",
        "Donkey Kong Country 2",
        "Donkey Kong Country 3",
        "Prince of Persia",
        "R-Type III",
        "StarFox",
        "Super Castlevania IV",
        "Super Ghouls 'n Ghosts",
        "Super Punch-Out!!",
        "StarFox 64",
        "Sin & Punishment Star Successor",
        "Donkey Kong Country Tropical Freeze",
        "Gunstar Super Heroes",
        "Project X Zone",
        "Atomic Runner",
        "Castlevania Bloodlines",
        "Contra Hard Corps",
        "Dynamite Headdy",
        "Elemental Master",
        "Gaiares",
        "Kid Chameleon",
        "Lightening Force Quest for the Darkstar",
        "Mighty Morphin Power Rangers The Movie",
        "MUSHA",
        "Quackshot Starring Donald Duck",
        "Ranger X",
        "Rocket Knight Adventures",
        "Shinobi III Return of the Ninja Master",
        "Ren & Stimpy Show Presents: Stimpy's Invention",
        "Thunder Force III",
        "Wings of Wor",
        "Zero Wing",
        "Cho Aniki ~ Kyukyoku...Otokonogyakushu",
        "Darius Gaiden",
        "DoDonPachi",
        "Elevator Action -Returns-",
        "Galactic Attack",
        "Guardian Heroes",
        "Metal Black",
        "Radiant Silvergun",
        "Sexy Parodius",
        "Soukyugururentai Otokuyo",
        "Road Blaster",
        "Thunder Storm",
        "Virtua Cop",
        "Ape Escape",
        "Beyblade",
        "Einhander",
        "R-Type Delta",
        "Raystorm",
        "Raycrisis: Series Termination",
        "Raiden (Raiden Project)",
        "Raiden 2 (Raiden Project)",
        "Thunder Force V",
        "Crimzon Clover",
        "Tetris GrandMaster, LOOOOOOOOOOOL",
        "F-Zero GX"
]

gamelist_1P_long = ["The Legend of Zelda: A Link to the Past",
        "Yoshi's Island",
        "The Legend of Zelda Link's Awakening (with strategy guide)",
        "Final Fantasy III",
        "Chrono Trigger",
        "The Legend of Zelda (with strategy guide)",
        "Zelda II The Adventure of Link (with strategy guide)",
        "Kirby's Adventure",
        "Faxanadu",
        "Conker's Bad Fur Day",
        "Glover",
        "The Legend of Zelda Majora's Mask (with strategy guide)",
        "Pandora's Tower",
        "Rayman Origins",
        "The Last Story",
        "Xenoblade Chronicles",
        "Zack & Wiki Quest for Barbaros' Treasure",
        "Bayonetta",
        "Bayonetta 2",
        "The Legend of Zelda Wind Waker HD",
        "Zombi U",
        "The Legend of Zelda A Link Between Worlds",
        "Chrono Cross",
        "Final Fantasy IX",
        "Final Fantasy Tactics",
        "Front Mission 3",
        "Parasite Eve",
        "Resident Evil 2",
        "Xenogears",
        "Syberia"
]
        
gamelist_2P = ["Twinkle Star Sprites",
        "Super Puzzle Fighter 2 Turbo",
        "Magical Drop III",
        "Super Smash Bros. Wii U",
        "Puzzle Bobble 2",
        "Puzzle Bobble 3",
]


gamelist = []

# Parsing user arguments
parser = argparse.ArgumentParser()
parser.add_argument('-med', help='Use this flag to suggest games average in completion time', action="store_true")
parser.add_argument('-long', help='Use this flag to suggest long games only', action="store_true")
parser.add_argument('-one', help='Use this flag to suggest one-player games only', action="store_true")
parser.add_argument('-two', help='Use this flag to suggest two-player games only', action="store_true")
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
limit = 3
while (counter < limit): 
    print ("Generating your game suggestion ", end=" ")
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
