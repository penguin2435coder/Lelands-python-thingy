questions = ["What is the name of this horror game that has the initials g.o.b.b.? ",
             "What game is that you have the ability to be different charecters? ",
             "What was minecraft origianally called? ",
             "What does the yellow pikmin do? ",
             "What is the name of the game about a cat that was recently released? ",
             "How much money does the dlc in mariocart cost? ",
             "What other mario game has cappy in it? ",
             "What color is the top half of a poke ball? "
             ]
answers = [
    "garten of ban ban",
    "super mario odyssey",
    "cave game",
    "electricity electrifies",
    "little kitty big city",
    "25$ twenty five dollers",
    "super smash bros",
    "Red"]

score = 0

for i in range (len(questions)):
    print(questions[i])
    guess = input("Answer:")
    answer = answers [i]
    if guess.lower() in answer.lower():
        print("YOU DID IT YOU ARE GOOOD!!!")
        score += 1
    else:
        print("womp womp")
    print("the answer was " + answers[i] + "\n")

print("You got " + str(score) + " out of " + str(len(questions)) + "!")




































