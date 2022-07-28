#IMPORTS
from calendar import prmonth
from random import randint
from threading import Timer
import sys,time,os



#GAME OVER
def game_over():
    print("  _____                         ____                 \n"
            " / ____|                       / __ \                \n"
            "| |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ \n"
            "| | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|\n"
            "| |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   \n"
            " \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   \n")
    quit() #COULD ADD WAY TO GET BACK TO MAIN MENU


#TITLE SCREEN ART
def ascii():
    print("      ___                       ___           ___           ___     ")
    print("     /\__\          ___        /\  \         /\  \         /\__\  ")
    print("    /:/ _/_        /\  \       \:\  \       /::\  \       /:/  /")
    print("   /:/ /\__\       \:\  \       \:\  \     /:/\:\  \     /:/__/")
    print("  /:/ /:/ _/_      /::\__\      /::\  \   /:/  \:\  \   /::\  \ ___")
    print(" /:/_/:/ /\__\  __/:/\/__/     /:/\:\__\ /:/__/ \:\__\ /:/\:\  /\__\ ")
    print(" \:\/:/ /:/  / /\/:/  /       /:/  \/__/ \:\  \  \/__/ \/__\:\/:/  /")
    print("  \::/_/:/  /  \::/__/       /:/  /       \:\  \            \::/  /")
    print("   \:\/:/  /    \:\__\       \/__/         \:\  \           /:/  /")
    print("    \::/  /      \/__/                      \:\__\         /:/  /")
    print("     \/__/                                   \/__/         \/__/")
    print("                  ___           ___           ___")
    print("                 /\__\         /\  \         |\__\ ")
    print("                /:/ _/_       /::\  \        |:|  |")
    print("               /:/ /\__\     /:/\:\  \       |:|  |")
    print("              /:/ /:/ _/_   /::\ \:\  \      |:|__|____")
    print("             /:/_/:/ /\__\ /:/\:\ \:\__\     /::::\____\ ")
    print("             \:\/:/ /:/  / \/__\:\/:/  /    /:/  / ")
    print("              \::/_/:/  /       \::/  /    /:/  /")
    print("               \:\/:/  /        /:/  /    /:/  /  ")
    print("                \::/  /        /:/  /    /:/  /")
    print("                 \/__/         \/__/     \/__/")
    print()
    print()

#GAME START
# def start_game():
    
#     for i in range(3):  # Change to control no. of 'blinks'
#             print("                     PRESS ENTER TO BEGIN", end='\r')
#             time.sleep(1)  # To create the blinking effect
#             sys.stdout.write('\033[2K\r')  # Clears the entire line and carriage returns
#             time.sleep(1)
    
#---------------------- Intro narration
def intro_narration():
    print("You regain consciousness in a dimly lit and run down room, you're tied to a chair and an inquisitor is asking you questions. You are in fact a witch, but a good witch. But you don't want to fall victim to the false crimes levied against you.")
    print()
    time.sleep(6)
    print("Before you stands a grizzled man, in his mid forties. On his face a permanent scowl. Down the left side of his face is a large deep scar, clearly he has seen his fair share of combat. His build is strong and burley. Grey patches litter his stubble and moustache. If you listen carefully you can hear him grinding his teeth. Yet around his neck is a religious symbol: This must be none other than the feared 'Inquisitor'.")
    print()
    time.sleep(8)


#---------------------- inquisitor_dialog_1
def inquisitor_dialog_1():
    print("Inquisitor:\"What is your name, rat?\" ")
    # inquisitor_dialog_1=("Inquisitor:\"What is your name, rat?\" ")
    # for char in inquisitor_dialog_1:
    #     sys.stdout.write(char)
    #     sys.stdout.flush()
    #     time.sleep(0.1)


#---------------------- Enter Player Name

def enter_player_name():
    global player_name
    player_name=input("> ") #make so you can't enter nothing, format it properly too
    print()
    

#---------------------- inquisitor_dialog_2

def inquisitor_dialog_2():
    print(f"Inquisitor:\"Aye... so we have the right one then. So {player_name}, if you confess to your foul acts of witchcraft this will all be over. Renounce your sins and ascend into the heavens! Your soul can yet be saved. All you need to do is confess.\"")
    # inquisitor_dialog_2=(f"Inquisitor:\"Aye... so we have the right one then. So {player_name}, if you confess to your foul acts of witchcraft this will all be over. Renounce your sins and ascend into the heavens! Your soul can yet be saved. All you need to do is confess.\"")
    # for char in inquisitor_dialog_2:
    #     sys.stdout.write(char)
    #     sys.stdout.flush()
    #     time.sleep(0.1)


#---------------------- Confession - "Escape Choices"

def confession():
        confession_options=["(1) Confess", "(2) Deny", "(3) Laugh"]
        for options in confession_options:
            print(options)

        option_chosen=input().lower() #add flavor text ("> ")
        
        if option_chosen == ("confess") or option_chosen == ("1"):
            print("You confess to your crimes, which in this case you actually DID commit.")
            time.sleep(3)
            print()
            print(f"\"Ah ha! Thank you {player_name}. Come, let us pray for the sanctity of your soul, soon you will be with god!\"")
            print()
            print("As you might expect, soon you are taken to the gallows, you ascend the gibbet and the noose is tied around your throat. Looking to the heavens you feel the trap door beneath your feet drop and a loud sharp crack...")
            # inq_confess_dia=(f"\"Ah ha! Thank you {player_name}. Come, let us pray for the sanctity of your soul, soon you will be with god!\"")
            # for char in inq_confess_dia:
            #     sys.stdout.write(char)
            #     sys.stdout.flush()
            #     time.sleep(0.1)
            print()
            time.sleep(3)
            game_over()

        elif option_chosen == ("deny") or option_chosen == ("2"):
            print("You deny your crimes. The witch hunter doesn't believe you.")
            print()
            time.sleep(3)
            print(f"So that's the way of it, is it {player_name}? A mighty shame, I had thought to spare you a trial, but it is clear the devil has clouded your judgement and only through pain may I wrench his terrible grasp of you and bring your soul salvation once again… Now, I need to fetch my tools.")
            print()
            time.sleep(5)
            escape_1_setup()

        elif option_chosen == ("laugh") or option_chosen == ("3"):
            print("You laugh in the witch hunter's face. He's taken by suprise, only breifly until his anger returns.")
            print()
            time.sleep(3)
            print(f"So that's the way of it, is it {player_name}? A mighty shame, I had thought to spare you a trial, but it is clear the devil has clouded your judgement and only through pain may I wrench his terrible grasp of you and bring your soul salvation once again… Now, I need to fetch my tools.")
            time.sleep(5)
            escape_1_setup()

        else:
            print ("Try again")
            time.sleep(1)
            confession()


#---------------------- Escape 1 - "Escape Choices"


def escape_1_setup():
    print("Unhappy with the answers you gave him, the inquisitor turns and leaves pulling his face into a contorted frown, his brow sunk ever lower in both rage and frustration one might think that his brow might slink over his face if it could sink any lower. He wanted answers and he would do everything that he could to get them. Fortunately for you however, the inquisitor's ire is taken away by both a sudden calling for him down the corridor and the fetching of his instruments of pain. Now you are left alone in your bindings")
    print()
    time.sleep(8)
    escape_1()

def escape_1():
    escape_1_options=["(1) Wait", "(2) Wriggle", "(3) Torch"]
    for options in escape_1_options:
        print(options)

    option_chosen=input().lower()
    
    global wriggle_done
    if option_chosen == ("wait") or option_chosen == ("1"):
        print("you wait and die")
        game_over()
    elif option_chosen == ("wriggle") or option_chosen == ("2"):
        if wriggle_done==False:
            print("You wriggle. No use.")
            wriggle_done=True
            escape_1()
        elif wriggle_done==True:
            print("You already tried that")
            escape_1()
    elif option_chosen == ("torch") or option_chosen == ("3"):
        print("You carefully lift the torch with your mind, burning the rope bindings. You're free to move!")
        escape_2_setup()
    else:
        print ("Try again")
        time.sleep(1)
        escape_1()


#---------------------- Escape 2 - "Escaping the intterogation room"


def escape_2_setup():
    print("You hear thunderous footfalls growing fainter as the inquisitor is drawn away to whatever business it may be that he had to attend. Poking your head out of the door you see two branching corridors, one to your left and the other to your right")
    escape_2()

def escape_2():
    global item_knife

    escape_1_options=["(1) Go right", "(2) Go left"]
    for options in escape_1_options:
        print(options)

    option_chosen=input().lower()
    
    if option_chosen == ("right") or option_chosen == ("1") or option_chosen == ("go right"):
        roll=randint(1,20)
        print(roll) #FOR TESTING SHIV ROLL
        if roll>=15:
            print("You go right. Dead end. Turn around and head the only other way out")
            print("Along the way you find a shiv, this could come in handy!")
            item_knife=True
            guard_setup()
        elif roll<15:
            print("You go right. Dead end. Turn around and head the only other way out")
            guard_setup()
    elif option_chosen == ("left") or option_chosen == ("2") or option_chosen == ("go left"):
        print("You go left. This is the way out")
        guard_setup()
    else:
        print ("Try again")
        time.sleep(1)
        escape_2()

#---------------------- Guard - "Escaping the intterogation room"

def guard_setup():
    print("Creeping down the path you hear the squeak of rats and mice beneath the floorboards. But soon a sharp snoring snatches your attention and you're put back in the moment: As you creep ever closer you see a guard passed out in his chair with an unlocked door next to him. Should you try and sneak past or dispatch the guard, that's the question...")
    guard_choices()

def guard_choices():
    global item_knife

    guard_choices_options=["(1) Sneak past", "(2) Kill the guard"]
    for options in guard_choices_options:
        print(options)

    option_chosen=input().lower()

    if option_chosen == ("sneak") or option_chosen == ("1") or option_chosen == ("sneak past"):
        roll=randint(1,20)
        print(roll) #SET FOR TESTING
        if roll>=10: #CHANGE TO HIGHER, SET TO 1 FOR TESTING
            print("You sneak past the guard")
            courtyard_1_setup()
        else:
            print("You failed to sneak past the guard")
            print("The guard wakes up and attacks you")
            qte_dodge_sleeping_guard()
    elif option_chosen == ("kill") or option_chosen == ("2") or option_chosen == ("kill guard" or option_chosen == ("kill the guard")):
        if item_knife==True:
            print("You kill the guard using the shiv you found earlier, the handle snaps and you can't recover it from the guard's body")
            courtyard_1_setup()
        else:
            print("You attempt to kill the SLEEPING guard")
            qte_kill_sleeping_guard()
    else:
        print ("Try again")
        time.sleep(1)
        guard_choices()

def qte_kill_sleeping_guard():
    timeout = 2
    t = Timer(timeout, print, ["Failed to kill the guard"],)
    t.start()
    start_time = time.time()
    prompt = f"You have {timeout} seconds to kill the guard, press enter...\n"
    answer = input(prompt)
    t.cancel()
    end_time = time.time()
    reaction_time = end_time - start_time
    if reaction_time > timeout:
        dodge = False
        qte_dodge_sleeping_guard()
    else:
        print("You kill the guard")
        dodge = True
        courtyard_1_setup()

def qte_dodge_sleeping_guard():
    timeout = 3
    t = Timer(timeout, print, ["Failed to dodge the guard's attack, you died"],)
    t.start()
    start_time = time.time()
    prompt = f"You have {timeout} seconds to dodge the guards attack, press enter...\n"
    answer = input(prompt)
    t.cancel()
    end_time = time.time()
    reaction_time = end_time - start_time
    if reaction_time > timeout:
        dodge = False
        game_over()
    else:
        print("You dodged the guard's attack!")
        dodge = True
        qte_counter_sleeping_guard()

def qte_counter_sleeping_guard():
    timeout = 3
    t = Timer(timeout, print, ["Failed to kill the guard, you died"],)
    t.start()
    start_time = time.time()
    prompt = f"You have {timeout} seconds to counter and kill the guard, press enter...\n"
    answer = input(prompt)
    t.cancel()
    end_time = time.time()
    reaction_time = end_time - start_time
    if reaction_time > timeout:
        dodge = False
        game_over()
    else:
        print("You kill the guard")
        dodge = True
        courtyard_1_setup()


#---------------------- Escaping the courtyard

def courtyard_1_setup():
    print()
    print ("Past the guard, you soon enter a courtyard. Within the courtyard are patrolling guards with dogs held on thick leather leashes. You finally see the outside world and note that it is a cloudy night concealing the moon behind their grey guard. Fortunately for you that means the guards have difficulty seeing beyond their candle light")
    courtyard_1()

def courtyard_1():

    courtyard_1_options=["(1) Sneak in the shadows", "(2) Make a run for it"]
    for options in courtyard_1_options:
        print(options)

    option_chosen=input().lower()

    if option_chosen == ("sneak") or option_chosen == ("1") or option_chosen == ("sneak in the shadows") or option_chosen == ("sneak in shadows"):
            print("Weaving magic to blend in with the shadows you pass undetected...")
            eavesdropping_setup()
    elif option_chosen == ("run") or option_chosen == ("2") or option_chosen == ("make a run for it"):
        print("Are you sure? Those dogs don't look too friendly, but they do look fast")
        run_or_sneak()
    else:
        print ("Try again")
        time.sleep(1)
        courtyard_1()

def run_or_sneak():

    courtyard_1_options=["(1) Yes", "(2) No"]
    for options in courtyard_1_options:
        print(options)

    option_chosen=input().lower()

    if option_chosen == ("yes") or option_chosen == ("1") or option_chosen == ("y"):
        print()
        print("You were spotted by an eagle-eyed guard in a tower. His arrow hits you square in the chest")
        game_over()
    elif option_chosen == ("no") or option_chosen == ("2") or option_chosen == ("n"):
        print()
        print("after some hesitation you decided to sneak past")
        eavesdropping_setup()
    else:
        print ("Try again")
        time.sleep(1)
        run_or_sneak()

#---------------------- Eavesdropping

def eavesdropping_setup():
    print()
    #narration
    print("Overhearing a conversation between two guards on break, you decide to creep ever closer, remaining out of sight and keeping magic to a minimum...")
    print()
    #dialog
    print("Gaurd 1: He keeps bangin' on about how the north gate isn't checked enough. I told him \"I'm not doin' extra shifts again. I've done my bit, he can do it 'imself if he wants it done so badly!\"")
    print()
    print("Guard 2: \"I can't believe you said that to 'is face!")
    print()
    print("Both the guards laugh")
    print()
    #narration
    print("You have the information you need, but perhaps listening a little longer could yield more details? Do you choose to chance fate and stay?")
    print()
    eavesdropping()

def eavesdropping():

    eavesdropping_options=["(1) Listen more", "(2) Leave"]
    for options in eavesdropping_options:
        print(options)

    option_chosen=input().lower()

    if option_chosen == ("listen") or option_chosen == ("1") or option_chosen == ("listen more"):
        print()
        # print("'Did you hear about that prisoner that went mad? I heard the boss tortured \'em so much, by the end the guy was rockin\' back and forth sayin' \"beans\" over and over again...'") #EASTER EGG
        easter_egg=(f"'Did you hear about that prisoner that went mad? I heard the boss tortured \'em so much, by the end the guy was rockin\' back and forth sayin' \"beans\" over and over again...'")
        for char in easter_egg:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
        eavesdropping_longer()
        #add scrolling text to this
    elif option_chosen == ("leave") or option_chosen == ("2"):
        print()
        print("You skulk past the chatty guards, making sure to avoid areas of torchlight")
        north_gate_setup()
    else:
        print ("Try again")
        time.sleep(1)
        eavesdropping()

def eavesdropping_longer():
    print()
    eavesdropping_longer_options=["(1) Listen even longer", "(2) Leave"]
    for options in eavesdropping_longer_options:
        print(options)

    option_chosen=input().lower()

    if option_chosen == ("listen") or option_chosen == ("1") or option_chosen == ("listen longer") or option_chosen == ("listen even longer"):
        print()
        print("You listen even longer, but you overstay your welcome. One of the guards starts to turn around")
        eavesdropping_roll=randint(1,20)
        if eavesdropping_roll>=10:
            print()
            print(f"You rolled: {eavesdropping_roll}/20. You quickly press yourself up against a shadowy wall, just out of the torchlight's distance. Close one.")
            north_gate_setup()
        elif eavesdropping_roll<10:
            print()
            print(f"You rolled: {eavesdropping_roll}/20. You see the guard turning towards you but you freeze. The guard's eyes widen with shock. He nudges the other guard as you both stare at each other frozen. The second guard has more sense and quickly hits you with the hilt of his sword, knocking you unconscious")
            game_over()
    elif option_chosen == ("leave") or option_chosen == ("2"):
        print()
        print("You leave and make your way to the north gate")
        north_gate_setup()
    else:
        print ("Try again")
        time.sleep(1)
        eavesdropping()


#---------------------- North Gate - "Escape plans"

def north_gate_setup():
    print()
    print("Those guards let slip that the north gate is very lightly patrolled. You carefully make your way to the north of the gate, trending lightly as you masterfully evade patrols, look-outs and guard dogs")
    print("You're here. The final stretch")
    print("Just like the guards said, there seems to be only one man stationed at the gate")
    print("You scan your surrounding the best you can given the only lightsources are the moon and some scarcely places torches")
    print("You spot a ways out of this retched place. Some 'better' than others...")
    escape_plan()

def escape_plan():
    
    escape_plan_options=["(1) Enter the sewers", "(2) Use a pebble to cause a distraction (distract)"] # (3) Subdue guard
    for options in escape_plan_options:
        print(options)

    option_chosen=input().lower()

    if option_chosen == ("sewer") or option_chosen == ("1"): #add extra confirm to sewer maybe with joke about not wanting to go in
        print()
        #Narration
        print("While in the guard's perifery, you slowly make your way over to the small manhole and pop the hatch.")
        sewer_chosen()
    elif option_chosen == ("pebble") or option_chosen == ("2") or option_chosen == ("distract"):
        print()
        #narration about the pebbles
        print("You see pile of pebbles")
        pebble_chosen()
    else:
        print ("Try again")
        time.sleep(1)
        escape_plan()

def sewer_chosen():
    print()
    #more narration description of walking through the sewer
    print("You wade through the sewers")

    sewer_ending_roll=randint(1,20)
    if sewer_ending_roll<=5:
        print()
        print(f"You rolled: {sewer_ending_roll}/20. Slogging along through the faeces and water you begin to lose your footing, the stench burning your throat, you find that it becomes hard to breath. Falling face first you hit your head against the quarried stone, passing out face down in sewage. A horrible end, but at least you died fighting your fate.")
        game_over()
        quit()
    elif sewer_ending_roll>5:
        print()
        print(f"You rolled: {sewer_ending_roll}/20.  The stench immediately rises, burning your nostrils with its foul and offensive odour. How disgusting, the stench alone would make even the most steeled stomached soldier keel, but it's this or death...")
        congrats()
        #ending stuff
        quit()
    

def pebble_chosen():
    #narration about causing the distraction

    # "The pebbles fly true, be it magic or luck it matters not. The pebbles land with a loud thud, catching the guard's attention"

    print("Swiftly yet almost floating, you take your chance with fate")
    pebble_ending_roll=randint(1,20)
    if pebble_ending_roll<=5:
        print()
        print(f"You rolled: {pebble_ending_roll}/20. Feeling the wind as you try to dash past, the guard turns and kills you before you can escape")
        game_over()
        #ending stuff
    elif pebble_ending_roll>5:
        print()
        print(f"You rolled: {pebble_ending_roll}/20. With the guard's back turned you dash past and through the gate to freedom")
        congrats()
        #ending stuff


    
def congrats():
    print("╔═══╗─────────────╔╗───╔╗───╔╗\n"
    "║╔═╗║────────────╔╝╚╗──║║──╔╝╚╗\n"
    "║║─╚╬══╦═╗╔══╦═╦═╩╗╔╬╗╔╣║╔═╩╗╔╬╦══╦═╗╔══╗\n"
    "║║─╔╣╔╗║╔╗╣╔╗║╔╣╔╗║║║║║║║║╔╗║║╠╣╔╗║╔╗╣══╣\n"
    "║╚═╝║╚╝║║║║╚╝║║║╔╗║╚╣╚╝║╚╣╔╗║╚╣║╚╝║║║╠══║\n"
    "╚═══╩══╩╝╚╩═╗╠╝╚╝╚╩═╩══╩═╩╝╚╩═╩╩══╩╝╚╩══╝\n"
    "──────────╔═╝║\n"
    "──────────╚══╝\n")
    print()
    time.sleep(1)
    print("Escaping into the night, you run from your old life and begin anew, forever holding the scars of your past and burying a secret deep within. You remind yourself that this must never come to pass again...") #add flavour text about winning
    print()
    time.sleep(1)
    print("Thank you for playing!")
    quit()









#NOTES
#add str only and str length cap and capital first letter to name input



#PLAYER NAME
player_name=""

#Escape 1 bool
wriggle_done=False

#ITEMS
item_knife=False


# MAIN CODE (EXECUTIONS)


ascii()
intro_narration()
inquisitor_dialog_1()
enter_player_name()
inquisitor_dialog_2()
print()
confession()