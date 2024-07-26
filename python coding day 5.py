import random

def pacman():
    print("You are in a hallway that is blue with yellow dots. a yellow chompy guy comes around the corner.")
    choice = input("What do you do? \n1. Talk To Him. \n2. give him some cake. \nChoice:")
    if choice == "1":
        print("He says, Countinue the video game inside a video game part 2 coming out soon. THE END")
        print("He says, Thank you for this gift. Now I will eat YOU!!! THE END")





def donkeykong():
    print("You are in a giant room that looks like a construction site. You also hear a monkey above you.")
    choice = input("What do you do? \n1. Check out the monkey. \n2. Try to get out. \nChoice:")
    if choice == "1":
            print("You start running up the construction site and soon become face to face with a giant gorrilla!")
            print("He starts CHUCKING BARRELS AT YOU!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("THE END")
    elif choice == "2":
        print("You smack your body into the wall trying to get out! Then all of a sudden, a man with a red hat walks up to you and gives you some advise. He tells you to say the words next game very clearly. ")           
        choice = input("What do you do? \n1. Say next game. \n2. Say next game super slowly. \n3. DONT say next game. \nChoice:")
        if choice == "1":
            print("You get launched into another arcade game")
            pacman()
        elif choice == "2":
            print("The guy with a red hat says, You have to say it just a little slow. not SUPER slow.")
            donkeykong()
        elif choice == "3":
            print("You get trapped forever")
            print("THE END")


def dont_check():
    print("You think it is just one of those portal games.")
    print("Then you hear another sound and think that that portal arcade game must be pretty fun! so you go to check it out.")
    go_to_sound()


   
def go_to_sound():
    luck = random.randint(1,2)
    if luck == 1:
        print("You see the portal right in front of you. it looks like its on the screen but its not. YOU GET SUCKED IN.")
        donkeykong()
    elif luck == 2:
        print("The portal closes.\nTHE END")


def start():
    print("You are in the most famous arcade in the world. You sit on a bench inside the arcade and start eating popcorn.")
    print("While you are eating popcorn you hear something that sounded like a portal swooshing")
    choice = input("What do you do? \n1. Stop eating popcorn and go to where the sound came from.\n2. Think the noise is an arcade game. \nChoice:")    
    if choice == "1":
        print("You Follow the sound coming from the back of the arcade")
        go_to_sound()
    elif choice == "2":
        dont_check()
    else:
        print("THATS NOT AN OPTION. ARE YOU TRYING TO BREAK THE GAME???")
        start()



def main():
    print("Welcome to the olny video game inside a video game! \nPress enter to start!")
    input()
    start()

main()
