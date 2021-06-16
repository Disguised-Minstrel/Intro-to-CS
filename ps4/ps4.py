#6.00 Problem Set 4
#
# Caesar Cipher Skeleton
#
import string
import random

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: stri
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

wordlist = load_words()

def is_word(wordlist, word):
    """
    Determines if word is a valid word.

    wordlist: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordlist.

    Example:
    >>> is_word(wordlist, 'bat') returns
    True
    >>> is_word(wordlist, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in wordlist

def random_word(wordlist):
    """
    Returns a random word.

    wordlist: list of words  
    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

def random_string(wordlist, n):
    """
    Returns a string containing n random words from wordlist

    wordlist: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([random_word(wordlist) for _ in range(n)])

def random_scrambled(wordlist, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordlist: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words


    NOTE:
    This function will ONLY work once you have completed your
    implementation of apply_shifts!
    """
    s = random_string(wordlist, n) + " "
    shifts = [(i, random.randint(0, 26)) for i in range(len(s)) if s[i-1] == ' ']
    return apply_shifts(s, shifts)[:-1]

def get_fable_string():
    """
    Returns a fable in encrypted text.
    """
    f = open("fable.txt", "r")
    fable = str(f.read())
    f.close()
    return fable


# (end of helper code)
# -----------------------------------

#
# Problem 1: Encryption
#
def build_coder(shift):
    coder = dict()
    if shift >= 0:
        for letter in string.ascii_letters:
            if ord(letter) > 96:
                if ord(letter) + shift <= 123:
                    if ord(letter) + shift == 123:
                        coder[letter] = ' '
                    else:
                        coder[letter] = chr(ord(letter) + shift)
                else:
                    coder[letter] = chr(ord(letter) - (27-shift))
            else:
                if ord(letter) + shift < 91:
                    coder[letter] = chr(ord(letter) + shift)
                else:
                    coder[letter] = chr(ord(letter) - (26-shift))
        if shift == 0:
            coder[' '] = ' '
        else:
            coder[' '] = chr(97 + shift - 1)
    else:
        for letter in string.ascii_letters:
            if ord(letter) > 96:
                if ord(letter) + shift >= 96:
                    if ord(letter) + shift == 96:
                        coder[letter] = ' '
                    else:
                        coder[letter] = chr(ord(letter) + shift)
                else:
                    coder[letter] = chr(ord(letter) + 27 + shift)
            else:
                if ord(letter) + shift > 64:
                    coder[letter] = chr(ord(letter) + shift)
                else:
                    coder[letter] = chr(ord(letter) + (26+shift))
        coder[' '] = chr(123 + shift)
    return coder

def build_encoder(shift):
    return build_coder(shift)

def build_decoder(shift):
    return build_coder(-shift)

def apply_coder(text, coder):
    lst = list()
    for letter in text:
        lst.append(coder.get(letter, letter))
    return ''.join(lst)

def apply_shift(text, shift):
    return apply_coder(text, build_encoder(shift)) if shift >= 0 else apply_coder(text, build_decoder(-shift))

def find_best_shift(wordlist, text):
    best_shift = 0
    highest_words = 0
    for i in range(27):
        no_of_words = 0
        decoded = apply_shift(text, -i)
        lst = decoded.split()
        for j in range(len(lst)):
            if is_word(wordlist, lst[j]):
                no_of_words += 1
        if no_of_words > highest_words:
            best_shift = -i
        print("Shift:", i, "highest_words:", highest_words, "Number of words:", no_of_words, "best shift:", best_shift)
    return best_shift

def apply_shifts(text, shifts):
    new_text = text
    for shift in shifts:
        new_text = new_text[:shift[0]] + apply_shift(new_text[shift[0]:],
                                                     shift[1])
    return new_text

#
# Problem 4: Multi-level decryption.
#


def find_best_shifts(wordlist, text):
    """
    Given a scrambled string, returns a shift key that will decode the text to
    words in wordlist, or None if there is no such key.

    Hint: Make use of the recursive function
    find_best_shifts_rec(wordlist, text, start)

    wordlist: list of words
    text: scambled text to try to find the words for
    returns: list of tuples.  each tuple is (position in text, amount of shift)
    
    Examples:
    >>> s = random_scrambled(wordlist, 3)
    >>> s
    'eqorqukvqtbmultiform wyy ion'
    >>> shifts = find_best_shifts(wordlist, s)
    >>> shifts
    [(0, 25), (11, 2), (21, 5)]
    >>> apply_shifts(s, shifts)
    'compositor multiform accents'
    >>> s = apply_shifts("Do Androids Dream of Electric Sheep?", [(0,6), (3, 18), (12, 16)])
    >>> s
    'JufYkaolfapxQdrnzmasmRyrpfdvpmEurrb?'
    >>> shifts = find_best_shifts(wordlist, s)
    >>> print apply_shifts(s, shifts)
    Do Androids Dream of Electric Sheep?
    """

def find_best_shifts_rec(wordlist, text, start):
    final = list()
    for i in range(27):
        decoded = apply_shift(text, -i)
        #print(decoded[start:])
        s = start
        space = decoded.find(" ", start+1)
        if start == 643:
            print(decoded[start:space])
        #print("word", decoded[s:space], start, i, s, space)
        if space == -1:
            if is_word(wordlist, decoded[s:]):
                print("Partially decrypted: ", decoded[start:s], s)
                return [(start, -i)]
        if is_word(wordlist, decoded[s:space]):
            s = space
            #print("test s", s)
            #print("test space", space)
            s += 1
        if i == 26 and space == -1:
            return None
        if s == start:
            continue
        print("Partially decrypted: ", decoded[start:s], start, s, i)
        result = (find_best_shifts_rec(wordlist, decoded, s))
        #print("result", result)
        if result == None:
            continue
        #print("testing:", result)
        for shift in result:
            final.append(shift)
        print(final)
        final.append((start, -i))
        print(final)
        return final

def decrypt_fable():
    crypt_fable = get_fable_string()
    print(len(crypt_fable))
    print(crypt_fable)
    dec_shift = find_best_shifts_rec(wordlist, crypt_fable, 0)
    print(dec_shift)
    return apply_shifts(crypt_fable, dec_shift)


#What is the moral of the story?
#

text = "I really want, to test how exactly this works"
shift = 5
#code = apply_shift(text, shift)
#print(code)
#dec_shift = find_best_shift(wordlist, code)
#print(dec_shift, apply_shift(code, dec_shift))
multi_shifted = apply_shifts(text, [(0,2), (2,15), (18,7)])
print(decrypt_fable())
#print(multi_shifted)
#shifts = find_best_shifts_rec(wordlist, multi_shifted, 0)
#print(type(shifts), shifts)
#decoded = apply_shifts(multi_shifted, shifts)
#print(decoded)
