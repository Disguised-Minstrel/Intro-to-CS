# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = str.split(line)
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!

def game():
    word = choose_word(wordlist)
    print("I am thinking of %d letter word." % len(word))
    guesses = 8
    lst = list()
    while guesses > 0:
        print("You have %d guesses left." % guesses)
        print("Letters you already used are:", end='')
        for letter in lst:
            print(letter, end='')
        print("\n----------------")
        guess = input("Please guess a letter: ")
        lst.append(guess)
        if guess in word:
            print("Good guess.")
        else:
            print("Happens to the best.")
            guesses -= 1
        misses = 0
        for letter in word:
            if letter in lst:
                print(letter, end='')
            else:
                print("_", end='')
                misses += 1
        if misses == 0:
            print("Congratulations you won!")
            break
    print("The word was:", word)


while True:
    print("Welcome to the game of hangman!")
    game()
    another = input("Do you want to play another game: ")
    if another != 'y':
        break
