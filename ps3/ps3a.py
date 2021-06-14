# 6.00 Problem Set 3A Solutions
#
# The 6.00 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
#

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():

#   Returns a list of valid words. Words are strings of lowercase letters. 
#   Depending on the size of the word list, this function may
#   take a while to finish.

    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):

#   Returns a dictionary where the keys are elements of the sequence
#   and the values are integer counts, for the number of times that
#   an element is repeated in the sequence.
#   sequence: string or list
#   return: dictionary

    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

def get_word_score(word, n):
    total = 0
    for letter in word: total = total + SCRABBLE_LETTER_VALUES[letter]
    total = total * len(word)
    return total + 50 if len(word) == n else total

#   Returns the score for a word. Assumes the word is a
#   valid word.

#	The score for a word is the sum of the points for letters
#	in the word multiplied by the length of the word, plus 50
#	points if all n letters are used on the first go.

#	Letters are scored as in Scrabble; A is worth 1, B is
#	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

#   word: string (lowercase letters)
#   returns: int >= 0

def display_hand(hand):
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end='')
    print()

def deal_hand(n):

#   Returns a random hand containing n lowercase letters.
#   At least n/3 the letters in the hand should be VOWELS.

#   Hands are represented as dictionaries. The keys are
#   letters and the values are the number of times the
#   particular letter is repeated in that hand.

#   n: int >= 0
#   returns: dictionary (string -> int)

    hand = dict()
    num_vowels = random.randint(int(n/3), int(n/2))

    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels, n):
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1

    return hand

def update_hand(hand, word):
    new_hand = hand
    for letter in word:
        try:
            if hand[letter] == 1: del hand[letter]
            else: hand[letter] -= 1
        except:
            print("Invalid word for this hand.")
    return new_hand
#   Assumes that 'hand' has all the letters in word.
#   In other words, this assumes that however many times
#   a letter appears in 'word', 'hand' has at least as
#   many of that letter in it. 

#   Updates the hand: uses up the letters in the given word
#   and returns the new hand, without those letters in it.

#   Has no side effects: does not modify hand.

#   word: string
#   hand: dictionary (string -> int)    
#   returns: dictionary (string -> int)

    # TO DO ...

def is_valid_word(word, hand, word_list):
    letters = dict()
    for letter in set(word): letters[letter] = 0
    for letter in letters:
        for sign in word:
            if letter == sign:
                letters[letter] += 1
    for letter in letters:
        if letters[letter] > hand.get(letter, 0):
            print("Not enough letter %s in hand." % letter)
            return False
    if word not in word_list: return False
    return True
#   Returns True if word is in the word_list and is entirely
#   composed of letters in the hand. Otherwise, returns False.
#   Does not mutate hand or word_list.

#   word: string
#   hand: dictionary (string -> int)
#   word_list: list of lowercase strings

    # TO DO...

def calculate_handlen(hand):
    handlen = 0
    for v in hand.values():
        handlen += v
    return handlen

def play_hand(hand, word_list):
    total = 0
    while True:
        display_hand(hand)
        word = input("Enter a world or '.' if you want to end.")
        if word == '.':
            print("Total:", total)
            break
        if is_valid_word(word, hand, word_list) == False:
            print("Not a vaild word for this hand.")
            continue
        word_score = get_word_score(word, HAND_SIZE)
        print("%s earned %d points." % (word, word_score))
        total = total + word_score
        hand = update_hand(hand, word)
        if calculate_handlen(hand) == 0:
            print("Total:", total)
            break
    return

#   Allows the user to play the given hand, as follows:

#   * The hand is displayed.

#   * The user may input a word.

#   * An invalid word is rejected, and a message is displayed asking
#     the user to choose another word.

#   * When a valid word is entered, it uses up letters from the hand.

#   * After every valid word: the score for that word is displayed,
#     the remaining letters in the hand are displayed, and the user
#     is asked to input another word.

#   * The sum of the word scores is displayed when the hand finishes.

#   * The hand finishes when there are no more unused letters.
#     The user can also finish playing the hand by inputing a single
#     period (the string '.') instead of a word.

#     hand: dictionary (string -> int)
#     word_list: list of lowercase strings


    # TO DO ... 

def play_game(word_list):
    while True:
        menu = ''
        while True:
            menu = input("New game, restart hand or end? n/r/e")
            if menu == 'n' or menu == 'r' or menu == 'e': break
        if menu == 'n':
            hand = deal_hand(HAND_SIZE)
            play_hand(hand, word_list)
        elif menu == 'r':
            play_hand(hand, word_list)
        elif menu == 'e':
            break
    return
#   Allow the user to play an arbitrary number of hands.

#   * Asks the user to input 'n' or 'r' or 'e'.

#   * If the user inputs 'n', let the user play a new (random) hand.
#     When done playing the hand, ask the 'n' or 'e' question again.

#   * If the user inputs 'r', let the user play the last hand again.

#   * If the user inputs 'e', exit the game.

#   * If the user inputs anything else, ask them again.

    # TO DO...

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
