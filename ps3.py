# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : Ann Latuil
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
WILDCARD="*"
GAME_OVER="!!"

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = r"C:\Users\User\Desktop\ann\labs\DKR2\words.txt"  

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    #print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    word_list = []
    for line in inFile:
        word_list.append(line.strip().lower())
    #print("  ", len(word_list), "words loaded.")
    return word_list

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word


def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    word=str.lower(word)
    part1=[]
    word_length=len(word)

    for lttr in word:
        try:
            points=SCRABBLE_LETTER_VALUES[lttr]
            part1.append(points)
        except KeyError:
            pass

    part1=sum(part1)
    part2=(7*word_length)-3*(n-word_length)
    
    if part2<1:
        score=part1*1

    elif part2>=1:
        score=part1*part2
    n=score

    return n

#
# Make sure you understand how this function works and what it does!
#

def display_hand(hand, n):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
            if hand[letter]=="*":
                range("*")==1
            display_hand=print(letter, end=' ')    # print all on the same line
    print()                                        # print an empty line
    return display_hand

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#

def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    n-=1
    hand={WILDCARD:1}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1

    return hand
#
# Problem #2: Update a hand by removing letters
#


def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """

    new_hand={}
    word=str(word).lower()
    for el in hand.keys():
        if el in word:
            amount=hand[el]-word.count(el)
            if amount>0:
                new_hand[el]=amount
        else:
            new_hand[el]=hand[el]
    return new_hand


#
# Problem #3: Test word validity
#


def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    word = word.lower()
    word_lttr = set(word)
    if set(hand.keys()).intersection(word_lttr) == word_lttr:

        for letter in word_lttr:
            if hand[letter] < word.count(letter):
                return False

        for letter in VOWELS:
            if word.replace(WILDCARD, letter) in word_list:
                return True
    return False

        

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    handlist=list(hand)
    handlen=len(handlist)
    return handlen


def play_hand(hand, word_list, total_score):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    score=0
    word=input("Enter word, or “!!” to indicate that you are finished: ")

    if word != "!!":

        if is_valid_word(word, hand, word_list) == True:
            print ("Great! You earned", get_word_score(word, n), "points!")
            total_score+=get_word_score(word, n)
            
        else:
            print ("Oops! You used unavailable letters or the word does not exist!")
            total_score+=0

        print ("Total score: ", total_score)
        print("-"*30)
        
        new_hand=update_hand(hand, word)
        

        if calculate_handlen(new_hand) > 0:
            try:
                print("Current hand:", end=" ") 
                display_hand(new_hand, n)
            except UnboundLocalError:
                pass
            
            play_hand(new_hand, word_list, total_score)
            

        elif calculate_handlen(hand) < 2:
            print("Game over!")
            print ("Total score: ", total_score)
            print("-"*30)
    else:
        print("Game over!")
        print ("Total score: ", total_score)
        print("-"*30)
    score+=total_score
    return score

#play_hand(hand, word_list, total_score)


#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    hand=dict(hand)
    if not letter in hand.keys():
        return hand
    else:
        alphabet=CONSONANTS+VOWELS
        random_letter=random.choice(alphabet)
        while random_letter in hand.keys():
            random_letter=random.choice(alphabet)

        modified_hand=hand.copy()
        modified_hand[random_letter]=modified_hand[letter]
        del modified_hand[letter]

    return modified_hand



def int_check(n):
    try:
        n=int(input())
    except:
        print("That is not a number!")
        int_check(n)
    return n
 

def play_game(word_list,times):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    
    total_score=0
    Total_total=0
    

    print ("Okay, let's start!")

    while times>0:
        hand = deal_hand(n)
        print("Current hand:", end=" ") 
        display_hand(hand, n)
        ans=input("Would you like to substitute any letter? ")
        if ans=="yes":
            letter=input("Which one? ")
            modified_hand=substitute_hand(hand, letter)
            print("Current hand:", end=" ") 
            display_hand(modified_hand, n)
            score=play_hand(modified_hand, word_list, total_score)
        else:
            score=play_hand(hand, word_list, total_score)
        replay=input("Would you like to replay the hand? ")
        if replay=="yes":
            print("Current hand:", end=" ") 
            display_hand(hand, n)
            play_hand(hand, word_list, total_score)
        Total_total+=score
        times-=1
    
       
    print("Total score of all hands:", Total_total)
    return Total_total


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    print("Yoohooo, it's time to play!")
    print ("But firstly some settings..")
    num=int
    print("Number of letters in hand:", end=" ")
    n=int_check(num)
    print("Enter total number of hands:", end=" ")
    times=int_check(num)  
    play_game(word_list,times)
