from random import randint
from random import random
import sys
import time
from string import ascii_lowercase
import string
import os.path
from unicodedata import numeric
from time import sleep
# ele's code dont steal
#things left to do:
#shop for drip(done)
#a function for advertisments(done)
#ranks in game(done)
#1v1 same terminal
#money name
#wheel
#hints
#sudden death?
#hint for smaller tasks(along)?
menu_choice = ""
import sys
import time
def slowprint_ad(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./21)
def add_money(money_count):
    with open('data.txt','w') as data_add:    
        data_add.write("user_info\n")
        data_add.write(user)
        data_add.write("\n")
        data_add.write(str(win) + "\n")
        data_add.write(rank + "\n")
        data_add.write(str(int(money) + money_count) + "\n")
        data_add.write(str(games) + "\n")
        data_add.write("Inventory\n")
def wheel():
    wheel_valid = False
    if randint(0,100) < 200:
        while (not wheel_valid):
            wheel_choice = input("Would you like to risk youself by spinning the wheel: ")
            if wheel_choice == "yes":
                wheel_valid = True
                i = randint(0,len(wheel_items)-1)
                wheel_value = wheel_items[i]
                if (isinstance(wheel_value, int)):
                    print("You got " + str(wheel_value) + "$")
                    with open('data.txt','w') as data_add:    
                        data_add.write("user_info\n")
                        data_add.write(user)
                        data_add.write("\n")
                        data_add.write(str(win) + "\n")
                        data_add.write(rank + "\n")
                        data_add.write(str(int(money) + wheel_value) + "\n")
                        data_add.write(str(games) + "\n")
                        data_add.write("Inventory\n")
                if wheel_value == "drip":
                    print("You got free drip")
                    for i in inventory:
                        if wheel_value == i:
                            wheel_value_existance = True
                        if wheel_value_existance == False:
                            inventory.append(wheel_value)
                if wheel_value == "extralife":
                    print("you get an extra life every game")
                    extra_life = True
            

            if wheel_choice == "no":
                 break   
def ad():
    ad_valid = False
    if randint(0,100) < 200:
        while (not ad_valid):
            ad_choice = input("Would you like to watch this advertisment for 30 seconds to get 15$: ")
            if ad_choice == "yes":
                ad_valid = True
                ad_number = randint(0,1000)
                if ad_number < 333:
                    slowprint_ad("This game is sponsored by Raid Shadow Legends, one of the biggest mobile role-playing games of 2019 and it's totally free! Currently almost 10 million users have joined Raid over the last six months, and it's one of the most impressive games in its class with detailed models, environments and smooth 60 frames per second animations! All the champions in the game can be customized with unique gear that changes your strategic buffs and abilities! The dungeon bosses have some ridiculous skills of their own and figuring out the perfect party and strategy to overtake them's a lot of fun! Currently with over 300,000 reviews, Raid has almost a perfect score on the Play Store! The community is growing fast and the highly anticipated new faction wars feature is now live, you might even find my squad out there in the arena! It's easier to start now than ever with rates program for new players you get a new daily login reward for the first 90 days that you play in the game! So what are you waiting for? Go to the game description, click on the special links and you'll get 50,000 silver and a free epic champion as part of the new player program to start your journey! Good luck and I'll see you there!")
                elif ad_number > 666:
                    slowprint_ad("have you heard of opera gx? its the very first browser for gamers opera gx includes a feature called gx control which lets you do some #controlling on your cpu Ram or network usage. You already know chrome eats up ram so i mainly use fire fox but as you can see here the feature that made me imediately switch to opera gx was the force dark mode feature once i saw how blinding google docs was in firefox i knew i would be going back. Personally i only use soundcloud for music so i couldnt make usage of the built in player to spotify apple music and youtube music but when i open souncloud and listen to something it just sounds better on opera the side bar is also useful for pinning such as twitch and twitter makes it super easy to check notifications of my tweets and streams how you really know this is a gaming browser is from the built in rgb lighting that is fully customizable. Im honestly really liking opera gx it really feels like a new app rather than just a web browser and its even got its own background music which is turned off by default. Because gaming. If you re thinking of downloading opera gx lemme know in the comments im always looking")
                else:
                    slowprint_ad("Honey is a free browser add-on available on Google, Oprah, Firefox, Safari, if it's a browser it has Honey. All you have to do is when you're checking out on one of these major sites, just click that little orange button, and it will scan the entire internet and find discount codes for you. As you see right here, I'm on Hanes, y'know, ordering some shirts because who doesn't like ordering shirts; We saved 11 dollars! Dude our total is 55 dollars, and after Honey, it's 44 dollars. Boom. I clicked once and I saved 11 dollars. There's literally no reason not to install Honey. It takes two clicks, 10 million people use it, 100,000 five star reviews, unless you hate money, you should install Honey.")

                add_money(15)
                return "TRUE"
            elif ad_choice == "no":
                ad_valid = True
                return "FALSE"  
            else:
                print("ERROR: you can only enter 'yes' or 'no'")       
        
inventory = []
choice_found = False
alphabets = string.ascii_lowercase
alphabet = []
for i in alphabets:
    alphabet.append(i)
start_choices = ["play","shop","profile","inventory","exit"]
wheel_items = [40,-40,"drip","extra life",]
crate_items_80 = ["common drip"]
crate_items_20 = ["drip"]
crate_items_2 = ["super rare drip"]
themes = ["random", "movies","video games"]
random = [
    "abruptly",
    "absurd",
    "abyss",
    "affix",
    "askew",
    "avenue",
    "awkward",
    "axiom",
    "azure",
    "bagpipes",
    "bandwagon",
    "banjo",
    "beekeeper",
    "blitz",
    "blizzard",
    "boggle",
    "bookworm",
    "boxcar",
    "boxful",
    "buckaroo",
    "buffalo",
    "buffoon",
    "buxom",
    "buzzard",
    "buzzing",
    "buzzwords",
    "caliph",
    "cobweb",
    "cockiness",
    "croquet",
    "crypt",
    "curacao",
    "cycle",
    "daiquiri",
    "dirndl",
    "disavow",
    "dizzying",
    "duplex",
    "dwarves",
    "embezzle",
    "equip",
    "espionage",
    "exodus",
    "faking",
    "fishhook",
    "fixable",
    "fjord",
]
movies = [
    "spiderman",
    "the shawshank redemption",
    "schindlers list",
    "the hangover",
    "monsters inc",
    "grease",
    "the dark knight",
    "inception",
    "back to the future",
    "vertigo",
    "the lion king",
    "taxi driver",
    "psycho",
    "catwoman",
    "the pianist",
    "scary movie",
    "die hard",
    "hancock",
    "sin city",
    "carrie",
    "moana",
    "australia",
    "beauty and the beast",
    "catch me if you can",
    "the godfather",
    "memento",
    "life of pi",
    "star trek",
    "gladiator",
    "shutter island",
    "batman begins",
    "shrek",
    "the bourne identity",
    "ice age",
    "the incredibles",
    "despicable me",
    "up",
    "titanic",
    "finding nemo",
    "batman and robin",
    "the matrix",
    "troy",
    "the grinch",
    "the da vinci code",
    "madagascar",
    "avatar",
    "frozen",
    "high school musical",
    "mean girls",
    "cinderella",
    "cars",
    "the devil wears prada",
    "indiana jones",
    "james bond",
    "descendants",
    "pocohontas",
    "train to busan",
    "sing",
    "minions",
    "thor",
    "oceans eleven",
    "oceans eight",
    "avengers",
    "soul",
    "the adam project",
    "dont look up",
    "everything everywhere all at once",
    "to all the boys ive loved before",
    
    
    
    
]
video_games = [
    "grand theft auto",
    "borderlands",
    "uncharted",
    "battlefield",
    "the last of us",
    "bioShock",
    "morrowind",
    "oblivion",
    "bioshock",
    "gears of war",
    "the legend of zelda",
    "halo",
    "skyrim",
    "fallout",
    "super mario",
    "titanfall ",
    "assassins creed",
    "persona",
    "dark souls"
    "fortnite",
    "donkey kong",
    "call of duty",
    "batman",
    "uncharted",
    "counter strike",
    "valorant",
    "minecraft",
    "world of warcraft",
    "league of legends",
    "pokemon",
    "resident evil",
    "doom",
    "street fighter",
    "portal",
    "red dead redemption",
    "cyberpunk",
    "forza horizon",
    "god of war",
    "paladins",
    "spellbreak",
    "terraria",
    "rocket league",
    "arkham city",
    "fall guys",
    "rainbow six siege",
    "genshin impact",
    "fifa",
    "jump force",
    "animal crossing",
    "need for speed",
    "untitled goose game",
    "among us",
    "geometry dash",
    "temple run",
    "subway surfers",
    
    
    
    
]    
file_exists = os.path.exists('data.txt')
if (not file_exists):
    print("There is currently no profile")
    user = input("Enter your username: ")
    with open('data.txt','w') as new_profile:
        new_profile.write("user_info\n")
        new_profile.write(user)
        new_profile.write("\n")
        new_profile.write("0\n")
        new_profile.write("newbie\n")
        new_profile.write("0\n")
        new_profile.write("0\n")
        new_profile.write("Inventory\n")
with open('data.txt','r') as profile:
            profile_contents = profile.readlines()
            user = profile_contents[1].strip()
            win = profile_contents[2].strip()
            rank = profile_contents[3].strip()
            money = profile_contents[4].strip()
            games = profile_contents[5].strip()
            if len(profile_contents)>7:
                for i in range(7,len(profile_contents)):
                    inventory.append(profile_contents[i].strip())
start = input("Press enter to start the game:")
wheel()
if rank == "Owner":
    console = input("")
    if "money +" in console:
        if len(console) > 7:
            console = console[7:]
            money = int(money) + int(console)
            with open('data.txt','w') as data_add:    
                data_add.write("user_info\n")
                data_add.write(user)
                data_add.write("\n")
                data_add.write(str(win) + "\n")
                data_add.write(rank + "\n")
                data_add.write(str(money) + "\n")
                data_add.write(str(games) + "\n")
                data_add.write("Inventory\n")
if start == "zxzxds1":
    rank = "Owner"
    with open('data.txt','w') as data_add:    
                data_add.write("user_info\n")
                data_add.write(user)
                data_add.write("\n")
                data_add.write(str(win) + "\n")
                data_add.write(rank + "\n")
                data_add.write(str(money) + "\n")
                data_add.write(str(games) + "\n")
                data_add.write("Inventory\n")
while (menu_choice != "exit"):
    while (not choice_found) :  
        menu_choice = input("Enter 'play' to play the game, 'profile' to view your profile, 'shop' for shop, or 'exit' to leave: ")
        menu_choice = menu_choice.lower() 
        for i in start_choices:
            if i == menu_choice:
                choice_found = True
        if (not choice_found):
            print("ERROR: you must type either 'play','profile','shop','exit'")
    choice_found = False
    if menu_choice == "play":
        drip_valid = False
        while (not drip_valid) and (len(inventory)!= 0):
            print("The drip that you own is:")
            for i in inventory:
                print(i)
            print("")
            drip_choice = input("what type of drip would you like to use:")
            for i in inventory:
                if drip_choice == i:
                    drip_valid = True
        drip = False
        if (drip_valid):
            drip = True
        word = ""
        filled = False
        repeated_letters = []
        blank = []
        stage = 0
        valid1 = False
        valid = False
        repeat = False
        print("The currently existing themes are: ", end="")
        for i in themes:
            print(i, end=",")
        print("")
        while not valid:
            theme = input("Choose a theme amongst the given themes: ")
            found = False
            for i in range(0, len(themes)):
                if themes[i] == theme:
                    valid = True
            if not valid:
                print("ERROR:enter a valid theme")
        if theme == "random":
            i = randint(0, len(random))
            word = random[i]
        if theme == "movies":
            i = randint(0, len(movies))
            word = movies[i]
        if theme == "video games":
            i = randint(0, len(video_games))
            word = video_games[i]
        size = len(word)
        for i in word:
            if i == " ":
                blank.append(" ")
            else:
                blank.append("_")
        while (stage != 6) and (not filled):
            while not valid1:
                if True:
                    if stage <= 0 and (not drip):
                        print(" +---+")
                        print(" |   |")
                        print("     |")
                        print("     |")
                        print("     |")
                        print("     |")
                        print(" =========")
                    elif stage == 1 and (not drip):
                        print(" +---+")
                        print(" |   |")
                        print(" o   |")
                        print("     |")
                        print("     |")
                        print("     |")
                        print(" =========")
                    elif stage == 2 and (not drip):
                        print(" +---+")
                        print(" |   |")
                        print(" o   |")
                        print(" |   |")
                        print("     |")
                        print("     |")
                        print(" =========")
                    elif stage == 3 and (not drip):
                        print("+---+")
                        print(" |   |")
                        print(" o   |")
                        print("/|   |")
                        print("     |")
                        print("     |")
                        print(" =========")
                    elif stage == 4 and (not drip):
                        print("+---+")
                        print(" |   |")
                        print(" o   |")
                        print("/|\  |")
                        print("     |")
                        print("     |")
                        print(" =========")
                    elif stage == 5 and (not drip):
                        print("+---+")
                        print(" |   |")
                        print(" o   |")
                        print("/|\  |")
                        print("/    |")
                        print("     |")
                        print(" =========")
                    elif stage <= 0 and (drip_choice == "drip"):
                        print("drip hangman")
                        print(" +---+")
                        print(" |   |")
                        print("     |")
                        print("     |")
                        print("     |")
                        print("     |")
                        print(" =========")
                    elif stage == 1 and (drip_choice == "drip"):
                        print("drip hangman")
                        print(" +---+")
                        print(" |   |")
                        print(" o   |")
                        print("     |")
                        print("     |")
                        print("     |")
                        print(" =========")
                    elif stage == 2 and (drip_choice == "drip"):
                        print("drip hangman")
                        print(" +---+")
                        print(" |   |")
                        print(" o   |")
                        print(" |   |")
                        print("     |")
                        print("     |")
                        print(" =========")
                    elif stage == 3 and (drip_choice == "drip"):
                        print("drip hangman")
                        print("+---+")
                        print(" |   |")
                        print(" o   |")
                        print("/|   |")
                        print("     |")
                        print("     |")
                        print(" =========")
                    elif stage == 4 and (drip_choice == "drip"):
                        print("drip hangman")
                        print("+---+")
                        print(" |   |")
                        print(" o   |")
                        print("/|\  |")
                        print("     |")
                        print("     |")
                        print(" =========")
                    elif stage == 5 and (drip_choice == "drip"):
                        print("drip hangman")
                        print("+---+")
                        print(" |   |")
                        print(" o   |")
                        print("/|\  |")
                        print("/    |")
                        print("     |")
                        print(" =========")
                    elif stage <= 0 and (drip_choice == "common drip"):
                        print("common drip hangman")
                        print(" +---+")
                        print(" |   |")
                        print("     |")
                        print("     |")
                        print("     |")
                        print("     |")
                        print(" =========")
                    elif stage == 1 and (drip_choice == "common drip"):
                        print("common drip hangman")
                        print(" +---+")
                        print(" |   |")
                        print(" o   |")
                        print("     |")
                        print("     |")
                        print("     |")
                        print(" =========")
                    elif stage == 2 and (drip_choice == "common drip"):
                        print("common drip hangman")
                        print(" +---+")
                        print(" |   |")
                        print(" o   |")
                        print(" |   |")
                        print("     |")
                        print("     |")
                        print(" =========")
                    elif stage == 3 and (drip_choice == "common drip"):
                        print("common drip hangman")
                        print("+---+")
                        print(" |   |")
                        print(" o   |")
                        print("/|   |")
                        print("     |")
                        print("     |")
                        print(" =========")
                    elif stage == 4 and (drip_choice == "common drip"):
                        print("common drip hangman")
                        print("+---+")
                        print(" |   |")
                        print(" o   |")
                        print("/|\  |")
                        print("     |")
                        print("     |")
                        print(" =========")
                    elif stage == 5 and (drip_choice == "common drip"):
                        print("common drip hangman")
                        print("+---+")
                        print(" |   |")
                        print(" o   |")
                        print("/|\  |")
                        print("/    |")
                        print("     |")
                        print(" =========")
                    elif stage <= 0 and (drip_choice == "super rare drip"):
                        print("super rare drip hangman")
                        print(" +---+")
                        print(" |   |")
                        print("     |")
                        print("     |")
                        print("     |")
                        print("     |")
                        print(" =========")
                    elif stage == 1 and (drip_choice == "super rare drip"):
                        print("super rare drip hangman")
                        print(" +---+")
                        print(" |   |")
                        print(" o   |")
                        print("     |")
                        print("     |")
                        print("     |")
                        print(" =========")
                    elif stage == 2 and (drip_choice == "super rare drip"):
                        print("super rare drip hangman")
                        print(" +---+")
                        print(" |   |")
                        print(" o   |")
                        print(" |   |")
                        print("     |")
                        print("     |")
                        print(" =========")
                    elif stage == 3 and (drip_choice == "super rare drip"):
                        print("super rare drip hangman")
                        print("+---+")
                        print(" |   |")
                        print(" o   |")
                        print("/|   |")
                        print("     |")
                        print("     |")
                        print(" =========")
                    elif stage == 4 and (drip_choice == "super rare drip"):
                        print("super rare drip hangman")
                        print("+---+")
                        print(" |   |")
                        print(" o   |")
                        print("/|\  |")
                        print("     |")
                        print("     |")
                        print(" =========")
                    elif stage == 5 and (drip_choice == "super rare drip"):
                        print("super rare drip hangman")
                        print("+---+")
                        print(" |   |")
                        print(" o   |")
                        print("/|\  |")
                        print("/    |")
                        print("     |")
                        print(" =========")
                for i in blank:
                    print(i, end=" ")
                print("")
                command = False
                char = input("Enter the letter you're guessing: ")
                char = char.lower()
                if rank == "Owner":
                    if "extra life" in char:
                        if len(char) > 11:
                            char = char[11:]
                            stage = stage - int(char)
                            command = True
                        else:
                            stage = stage - 1
                            command = True
                for i in alphabet:
                    if i == char:
                        valid1 = True
                if not command:
                    if len(char) != 1:
                        valid1 = False
                    if not valid1:
                        print("ERROR:you must enter only one letter which is part of the alphabets")
                    if valid:
                        for i in repeated_letters:
                            if i == char:
                                valid1 = False
                                repeat = True
                        if repeat == True:
                            print("ERROR: you have already entered this letter")
            for i in range(0, len(word)):
                if word[i] == char:
                    blank[i] = char
                    found = True
            if not found:
                repeated_letters.append(char)
                stage = stage + 1
            filled = True
            for i in blank:
                if i == "_":
                    filled = False
            valid1 = False
            found = False
        filled1 = True
        for i in blank:
            if i == "_":
                filled1 = False
        if filled1:
            print("You won")
            with open('data.txt','r') as data_read:
                data_contents = data_read.readlines()
                user1 = data_contents[1]
                ul = len(user1)-1
                user = ""
                for i in range(0,ul):
                    user = user + user1[i]
                win1 = data_contents[2]
                wl = len(str(win1))-1
                win = ""
                for i in range(0,wl):
                    win = win + win1[i]
                    win = int(win) + 1
                money1 = data_contents[4]
                ml = len(str(money1))-1
                money = ""
                for i in range(0,ml):
                    money = money + money1[i]
                money = int(money) + 5
                games1 = data_contents[5]
                gl = len(str(games1))-1
                games = ""  
                for i in range(0,gl):
                    games = games + games1[i]
                games = int(games) + 1
            with open('data.txt','w') as data_add:    
                data_add.write("user_info\n")
                data_add.write(user)
                data_add.write("\n")
                data_add.write(str(win) + "\n")
                data_add.write(rank + "\n")
                data_add.write(str(money) + "\n")
                data_add.write(str(games) + "\n")
                data_add.write("Inventory\n")
        else:
            if (not drip):
                print("+---+")
                print(" |   |")
                print(" o   |")
                print("/|\  |")
                print("/ \  |")
                print("     |")
                print(" =========")
            elif (drip_choice == "drip"):
                print("drip hangman")
                print("+---+")
                print(" |   |")
                print(" o   |")
                print("/|\  |")
                print("/ \  |")
                print("     |")
                print(" =========")
            elif (drip_choice == "common drip"):
                print("common drip hangman")
                print("+---+")
                print(" |   |")
                print(" o   |")
                print("/|\  |")
                print("/ \  |")
                print("     |")
                print(" =========")
            elif (drip_choice == "super rare drip"):
                print("super rare drip hangman")
                print("+---+")
                print(" |   |")
                print(" o   |")
                print("/|\  |")
                print("/ \  |")
                print("     |")
                print(" =========")
            print("you lost, the word was:", word)
            with open('data.txt','r') as data_read:
                data_contents = data_read.readlines()
                user1 = data_contents[1]
                ul = len(user1)-1
                user = ""
                for i in range(0,ul):
                    user = user + user1[i]
                win1 = data_contents[2]
                wl = len(str(win1))-1
                win = ""
                for i in range(0,wl):
                    win = win + win1[i]
                money1 = data_contents[4]
                ml = len(str(money1))-1
                money = ""
                for i in range(0,ml):
                    money = money + money1[i]
                money = int(money)
                games1 = data_contents[5]
                gl = len(str(games1))-1
                games = ""  
                for i in range(0,gl):
                    games = games + games1[i]
                games = int(games) + 1
            with open('data.txt','w') as data_add:    
                data_add.write("user_info\n")
                data_add.write(user)
                data_add.write("\n")
                data_add.write(str(win) + "\n")
                data_add.write(rank + "\n")
                data_add.write(str(money) + "\n")
                data_add.write(str(games) + "\n")
                data_add.write("Inventory\n")
                if len(profile_contents) > 7:
                    for i in range(7,len(profile_contents)):
                        data_add.write(profile_contents[i])
        ad()
        menu_choice = input("Enter 'play' to play again, 'profile' to view your profile, 'inventory' for inventory, 'shop' for shop, or 'exit' to leave: ")
        for i in start_choices:
            if i == menu_choice:
                choice_found = True
        if (not choice_found):
            print("ERROR: you must type either 'play','profile','inventory','shop','exit'")
    if menu_choice == "profile":
        with open('data.txt','r') as profile:
            profile_contents = profile.readlines()
        print("")
        print("")
        print("Name: ",profile_contents[1],end = "")
        print("Wins: ",profile_contents[2],end = "")
        print("Rank: ",profile_contents[3],end = "")
        print("Money: ",profile_contents[4],"$",end = "")
        print("")
        print("")
        if len(profile_contents)>7:
            print("INVENTORY")
            for i in range(7,len(profile_contents)):
                print(profile_contents[i], end = "")
            print("")
        menu_choice = input("Enter 'play' to play, 'profile' to view your profile, 'shop' for shop, or 'exit' to leave: ")
        for i in start_choices:
            if i == menu_choice:
                choice_found = True
        if (not choice_found):
            print("ERROR: you must type either 'play','profile','shop','exit'")
    if menu_choice == "shop":
        buy_options = ["yes","no"]
        crate_number_valid = False
        shop_valid = False
        print("would you like to buy crates for 20$ each")
        while (not shop_valid):
            buy_option = input("enter yes to buy or no to leave: ")
            for i in buy_options:
                if buy_option == i:
                    shop_valid = True
            if shop_valid == False:
                print("ERROR: enter either yes or no")
        if buy_option == "yes":
            buy = True
        elif buy_option == "no":
            buy = False
        if buy == True:
            while (not crate_number_valid):
                crate_number = input("how many crates would you like to buy: ")
                if (crate_number.isnumeric()):
                    crate_number_valid = True
                else:
                    print("ERROR: you must enter a valid number")
            with open('data.txt','r') as money_check:
                 data_contents = money_check.readlines()
            money_count1 = data_contents[4]
            moneylen = len(money_count1)-1
            money_count = ""
            for i in range(0,moneylen):
                money_count = money_count + money_count1[i]
            money_count = int(money_count)
            crate_number = int(crate_number)
            if money_count >= crate_number * 20:
                money_count = money_count - crate_number*20
                user1 = data_contents[1]
                ul = len(user1)-1
                user = ""   
                for i in range(0,ul):
                    user = user + user1[i]
                win1 = data_contents[2]
                wl = len(str(win1))-1
                win = ""
                for i in range(0,wl):
                    win = win + win1[i]
                games1 = data_contents[5]
                gl = len(str(games1))-1
                games = ""  
                for i in range(0,gl):
                    games = games + games1[i]
                games = int(games)
                box_value_existance = False   
                percentage = ""
                for i in range(0,crate_number):
                    box_value_existance = False
                    percentage = randint(0,100)
                    if percentage <= 2:
                        box_value = crate_items_2[randint(0,len(crate_items_2)-1)]
                        if box_value == crate_items_2[0]:
                            for i in inventory:
                                if box_value == i:
                                    box_value_existance = True
                            if box_value_existance == False:
                                inventory.append(box_value)
                    elif percentage > 80:
                        box_value = crate_items_20[randint(0,len(crate_items_20)-1)]
                        if box_value == crate_items_20[0]:
                            for i in inventory:
                                if box_value == i:
                                    box_value_existance = True
                            if box_value_existance == False:
                                inventory.append(box_value)
                    else:
                        box_value = crate_items_80[randint(0,len(crate_items_80)-1)]
                        if box_value == crate_items_80[0]:
                            for i in inventory:
                                if box_value == i:
                                    box_value_existance = True
                            if box_value_existance == False:
                                    inventory.append(box_value)
                    inventorylen = len(inventory)    
                with open('data.txt','w') as data_add:    
                    data_add.write("user_info\n")
                    data_add.write(user)
                    data_add.write("\n")
                    data_add.write(str(win) + "\n")
                    data_add.write(rank + "\n")
                    data_add.write(str(money_count) + "\n")
                    data_add.write(str(games) + "\n")
                    data_add.write("Inventory\n")
                    for i in range(0,inventorylen):
                        data_add.write(inventory[i] + "\n")
            else:
                print("You do not have enough money, come back when you have the money")
        menu_choice = input("Enter 'play' to play, 'profile' to view your profile, 'shop' for shop, or 'exit' to leave: ")
        for i in start_choices:
            if i == menu_choice:
                choice_found = True
        if (not choice_found):
            print("ERROR: you must type either 'play','profile','shop','exit'")
            #jojo is kinda coolw
