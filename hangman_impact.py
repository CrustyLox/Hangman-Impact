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
#rank updater
menu_choice = ""
import sys
import time
def slowprint_ad(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./21)
def add_inventory(inventory_earnt):
    if inventory_earnt not in inventory:
        inventory.append(inventory_earnt)
        with open('data.txt','w') as data_add:
            data_add.write("user_info\n")
            data_add.write(user)
            data_add.write("\n")
            data_add.write(str(win) + "\n")
            data_add.write(rank + "\n")
            data_add.write(str(money) + "\n")
            data_add.write(str(games) + "\n")
            data_add.write("Inventory\n")
            for i in inventory:
                data_add.write(i)        
def add_money(money_to_be_added):
    global money
    money = money + money_to_be_added
    if money < 0:
        money = 0
    with open('data.txt','w') as data_add:    
        data_add.write("user_info\n")
        data_add.write(user)
        data_add.write("\n")
        data_add.write(str(win) + "\n")
        data_add.write(rank + "\n")
        data_add.write(str(money) + "\n")
        data_add.write(str(games) + "\n")
        data_add.write("Inventory\n")
def change_rank(rank_to_be_changed_to):
    global rank
    with open('data.txt','w')as data_add:
        rank = rank_to_be_changed_to
        data_add.write("user_info\n")
        data_add.write(user)
        data_add.write("\n")
        data_add.write(str(win) + "\n")
        data_add.write(rank + "\n")
        data_add.write(str(money) + "\n")
        data_add.write(str(games) + "\n")
        data_add.write("Inventory\n")
def add_win():
    global win,games,money
    win = win + 1
    money = money + 5
    games = games + 1
    with open('data.txt','w')as data_add:
        data_add.write("user_info\n")
        data_add.write(user)
        data_add.write("\n")
        data_add.write(str(win) + "\n")
        data_add.write(rank + "\n")
        data_add.write(str(money) + "\n")
        data_add.write(str(games) + "\n")
        data_add.write("Inventory\n")
def add_loss():
    global games
    games = games + 1
    with open('data.txt','w')as data_add:
        data_add.write("user_info\n")
        data_add.write(user)
        data_add.write("\n")
        data_add.write(str(win) + "\n")
        data_add.write(rank + "\n")
        data_add.write(str(money) + "\n")
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
                    add_money(wheel_value)
                if wheel_value == "drip":
                    print("You got free drip")
                    add_inventory(wheel_value)
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
            win = int(profile_contents[2].strip())
            rank = profile_contents[3].strip()
            money = int(profile_contents[4].strip())
            games = int(profile_contents[5].strip())
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
            add_win()
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
            add_loss()
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
        print("Name: ",user )
        print("Wins: ",win,)
        print("Rank: ",rank, )
        print("Money: ",money,"$",)
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
            crate_number = int(crate_number)
            crate_cost = crate_number * 20
            if money >= crate_cost:
                add_money(-crate_cost)
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
                    data_add.write(str(money) + "\n")
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
mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
import os
from pathlib import Path
#money,wins,games
def add_win(winner):
    global win1,games1,win2,games2
    if winner == 1:
        win1 = win1 + 1
        games1 = games1 + 1
        games2 = games2 + 1
        with open(username_1 + '_profile.txt','w')as data_add:
            data_add.write("user_info\n")
            data_add.write(username_1)
            data_add.write("\n")
            data_add.write(str(win1) + "\n")
            data_add.write(str(games1) + "\n")
        with open(username_2 + '_profile.txt','w')as data_add:
            data_add.write("user_info\n")
            data_add.write(username_2)
            data_add.write("\n")
            data_add.write(str(win2) + "\n")
            data_add.write(str(games2) + "\n")
    elif winner == 2:
        win2 = win2 + 1
        games1 = games1 + 1
        games2 = games2 + 1
        with open(username_1 + '_profile.txt','w')as data_add:
            data_add.write("user_info\n")
            data_add.write(username_1)
            data_add.write("\n")
            data_add.write(str(win1) + "\n")
            data_add.write(str(games1) + "\n")
        with open(username_2 + '_profile.txt','w')as data_add:
            data_add.write("user_info\n")
            data_add.write(username_2)
            data_add.write("\n")
            data_add.write(str(win2) + "\n")
            data_add.write(str(games2) + "\n")
def clear_console(): 
    os.system('cls')
def game_board_formation():
    print(board[1] + "|" + board[2] + "|" + board[3])
    print(board[4] + "|" + board[5] + "|" + board[6])
    print(board[7] + "|" + board[8] + "|" + board[9])
def game_draw_check():
    global games1, games2
    if " " not in board:
        games1 = games1 + 1
        games2 = games2 + 1
        with open(username_1 + '_profile.txt','w')as data_add:
            data_add.write("user_info\n")
            data_add.write(username_1)
            data_add.write("\n")
            data_add.write(str(win1) + "\n")
            data_add.write(str(games1) + "\n")
        with open(username_2 + '_profile.txt','w')as data_add:
            data_add.write("user_info\n")
            data_add.write(username_2)
            data_add.write("\n")
            data_add.write(str(win2) + "\n")
            data_add.write(str(games2) + "\n")
        return True
def game_win_check():
    Game = False
    if(board[1] == board[2] and board[2] == board[3] and board[1] != ' '):    
        Game = True    
    elif(board[4] == board[5] and board[5] == board[6] and board[4] != ' '):    
        Game = True    
    elif(board[7] == board[8] and board[8] == board[9] and board[7] != ' '):    
        Game = True       
    elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):    
        Game = True    
    elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):    
        Game = True    
    elif(board[3] == board[6] and board[6] == board[9] and board[3] != ' '):    
        Game= True        
    elif(board[1] == board[5] and board[5] == board[9] and board[5] != ' '):    
        Game = True    
    elif(board[3] == board[5] and board[5] == board[7] and board[5] != ' '):    
        Game= True
    if Game == True:
        return True
def Get_profiles():
    global Profile_List
    Folder = Path.cwd()
    File_List = os.listdir(Folder)
    Profile_List = []
    for i in File_List:
        if "profile" in i:
            Profile_List.append(i)

start = input("Press Enter to start")
Game_over = False
Profile_List = []
new_profile_confirmation = False
board = [" "," "," "," "," "," "," "," "," "," "]
print("1|2|3")
print("4|5|6")
print("7|8|9")
print("Rules***")
Get_profiles()
print(Profile_List)
while not new_profile_confirmation:
    username_1 = input("Player 1, Enter you're username: ")
    if username_1 + "_profile.txt" not in Profile_List:
        print("The Username is not in any of the profiles made")
        print("If you would like to make a new profile enter yes")
        print("If you would like to re enter you're username enter no")
        profile_confirmation_valid = False
        while not profile_confirmation_valid:
            new_profile_confirmation = input("Enter you're choice: ")
            if new_profile_confirmation == "no":
                new_profile_confirmation = False
                profile_confirmation_valid = True
            elif new_profile_confirmation == "yes":
                new_profile_confirmation = True
                profile_confirmation_valid = True
                file_name = username_1 + "_profile.txt"
                with open (file_name , 'w') as new_profile:
                    new_profile.write("user_info\n")
                    new_profile.write(username_1)
                    new_profile.write("\n")
                    new_profile.write("0\n")
                    new_profile.write("0\n")
            else:
                print("ERROR: you can only enter yes or no")
                                  
    else:
        new_profile_confirmation = True
        with open(username_1 + '_profile.txt','r') as user1_profile:
                    profile_contents = user1_profile.readlines()
                    user1 = profile_contents[1].strip()
                    win1 = int(profile_contents[2].strip())
                    games1 = int(profile_contents[3].strip())  
new_profile_confirmation = False
while not new_profile_confirmation:
    username_2 = input("Player 2, Enter you're username: ")
    if username_2 + "_profile.txt" not in Profile_List:
        print("The Username is not in any of the profiles made")
        print("If you would like to make a new profile enter yes")
        print("If you would like to re enter you're username enter no")
        profile_confirmation_valid = False
        while not profile_confirmation_valid:
            new_profile_confirmation = input("Enter you're choice: ")
            if new_profile_confirmation == "no":
                new_profile_confirmation = False
                profile_confirmation_valid = True
            elif new_profile_confirmation == "yes":
                new_profile_confirmation = True
                profile_confirmation_valid = True
                file_name = username_2 + "_profile.txt"
                with open (file_name , 'w') as new_profile:
                    new_profile.write("user_info\n")
                    new_profile.write(username_2)
                    new_profile.write("\n")
                    new_profile.write("0\n")
                    new_profile.write("0\n")
            else:
                print("ERROR: you can only enter yes or no")
                  
    else:
        new_profile_confirmation = True
        with open(username_2 + '_profile.txt','r') as user2_profile:
                    profile_contents = user2_profile.readlines()
                    user2 = profile_contents[1].strip()
                    win2 = int(profile_contents[2].strip())
                    games2 = int(profile_contents[3].strip())  
while (not Game_over):
    Counter_Valid = False
    while not Counter_Valid:
        clear_console()
        game_board_formation()
        counter = int(input(username_1 + " enter your number: "))
        if board[counter] != " ":
            print("ERROR: there is already a value in that spot")
        else:
            board[counter] = "X"
            Counter_Valid = True
    clear_console()
    game_board_formation()
    if game_win_check():
        print(username_1 + " wins")
        Game_over = True
        add_win(1)
        break
    Counter_Valid = False
    while not Counter_Valid:
        counter = int(input(username_2 + " enter your number: "))
        if board[counter] != " ":
            print("ERROR: there is already a value in that spot")
        else:
            board[counter] = "O"
            Counter_Valid = True
    clear_console()
    game_board_formation()
    if game_win_check():
        print(username_2 + " wins")
        Game_over = True
        add_win(2)
        break
    if (game_draw_check):
        Game_over = True
        print("Draw")
end = input("Press Enter to leave")
