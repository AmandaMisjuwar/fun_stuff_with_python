import random

#player variables
points = 0
wrong = []
guessed = ""

# list of possible words
words = ["doggo","pupper","candy", "waffles", "toronto", "vancouver", "pancake"]


def init_game():
    global points
    global guessed
    #getting random new word
    index = random.randint(0,6)
    word = words[index]
    #init player variables
    if points != 0:
        points -= points
    # ----------------start game---------------------------
    print("START THE GAME!")
    print_status("", word)
    while (won(word) == False) and (len(wrong) < 10):
        guess = input("\nGuess a letter: ")
        if guess in word:
            points += 1
            guessed += guess
        else:
            wrong.append(guess)
            print(wrong)
        print_status(guess, word)
    if won(word) == False:
        print("TOO BAD, YOU LOST THE GAME")
        print("THE WORD WAS '" + word + "'.")
    elif won(word) == True:
        print("CONGRATS! YOU WON THE GAME")


def print_status(guess, word):
    print ("***********************")
    print("Score: %d" % points)
    print("Wrong guesses: ")
    print(wrong)
    print("Word:")
    for x in word:
        if x in guessed:
            print(" " + x, end = '')
        else:
            print(" _", end = '')
    print("")

def won(word):
    global guessed
    for x in word:
        if x not in guessed:
            return False
    
    return True
    

init_game()