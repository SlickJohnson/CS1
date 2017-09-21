"""Hangman Game.
Pick a secret word
Display hint
Take user guess
Check if the guess in word
- If yes, replace correct underscore
- If no, subtract 1 from guesses left
Track user guess/append latest guess
"""

import random
import os

HEAD = "  O"
BODY = "X"
LEFT_LIMB = "/"
RIGHT_LIMB = "\\"

TITLE = """
HH   HH   AAA   NN   NN   GGGG  MM    MM   AAA   NN   NN 
HH   HH  AAAAA  NNN  NN  GG  GG MMM  MMM  AAAAA  NNN  NN 
HHHHHHH AA   AA NN N NN GG      MM MM MM AA   AA NN N NN 
HH   HH AAAAAAA NN  NNN GG   GG MM    MM AAAAAAA NN  NNN 
HH   HH AA   AA NN   NN  GGGGGG MM    MM AA   AA NN   NN 
"""

YOU_WIN = """
YY   YY  OOOOO  UU   UU  WW      WW IIIII NN   NN !!! !!! !!! 
YY   YY OO   OO UU   UU  WW      WW  III  NNN  NN !!! !!! !!! 
 YYYYY  OO   OO UU   UU  WW   W  WW  III  NN N NN !!! !!! !!! 
  YYY   OO   OO UU   UU   WW WWW WW  III  NN  NNN             
  YYY    OOOO0   UUUUU     WW   WW  IIIII NN   NN !!! !!! !!!
"""

GAME_OVER = """  
  GGGG    AAA   MM    MM EEEEEEE 
 GG  GG  AAAAA  MMM  MMM EE      
GG      AA   AA MM MM MM EEEEE   
GG   GG AAAAAAA MM    MM EE      
 GGGGGG AA   AA MM    MM EEEEEEE 
                                 
 OOOOO  VV     VV EEEEEEE RRRRRR  !!! !!! !!! 
OO   OO VV     VV EE      RR   RR !!! !!! !!! 
OO   OO  VV   VV  EEEEE   RRRRRR  !!! !!! !!! 
OO   OO   VV VV   EE      RR  RR              
 OOOO0     VVV    EEEEEEE RR   RR !!! !!! !!!
"""


ORDER_OF_PARTS_ADDED = [HEAD + "\n", " " + LEFT_LIMB, BODY, RIGHT_LIMB + "\n ", LEFT_LIMB, " " + RIGHT_LIMB]


class Player:
    """Player class.
        Keeps track of guesses and prints player body"""

    def __init__(self):
        self.number_of_wrong_guesses = 0
        self.letters_guessed = []
        self.__body__ = ""
        self.is_player_dead = False

    def update(self):
        """Prints stand and player"""

        print("---\n  |\n  |")
        print(self.__body__, "\n\n")

    def add_body_part(self):
        """Adds body parts to player depending on the number of guesses"""

        self.number_of_wrong_guesses += 1

        if self.number_of_wrong_guesses < len(ORDER_OF_PARTS_ADDED):
            self.__body__ = ""

            for i in range(0, self.number_of_wrong_guesses):
                self.__body__ += ORDER_OF_PARTS_ADDED[i]
        else:
            self.__body__ += ORDER_OF_PARTS_ADDED[-1]
            self.is_player_dead = True


def load_word():
    """Retrieves random word from word list"""

    file = open("hangman_words.txt", "r")
    world_list = file.readline()
    file.close()

    world_list = world_list.split(" ")
    secret_word = random.choice(world_list)

    return secret_word


def update(secret_word, message_to_player):
    """Prints game information"""

    clear()

    if is_word_guessed(secret_word):
        game_won()

    elif not player.is_player_dead:
        print(TITLE, "\n\n")
        player.update()
        print(message_to_player)
        print(player_word_progress(secret_word))
        ask_for_guess(secret_word)

    else:
        print(GAME_OVER, "\n\n")
        player.update()
        print("\n\nThe word was", secret_word)


def check_guess(guess, secret_word):
    """Check to see if player guessed the right word or letter"""

    message_to_player = ""
    if len(guess) == len(secret_word) and guess == secret_word:
        message_to_player = "YOU GUESSED THE WORD. IT WAS " + secret_word
        game_won()

    elif secret_word != "" and guess in secret_word:
        message_to_player = "THAT LETTER IS IN THE WORD\n\n"
        player.letters_guessed.append(guess)

    elif guess not in player.letters_guessed:
        message_to_player = "WRONG! TRY AGAIN!\n\n"

        player.add_body_part()
        player.letters_guessed.append(guess)

    else:
        message_to_player = "YOU ALREADY GUESSED THAT LETTER!!!\n\n"

    update(secret_word, message_to_player + "Letters guessed:\n\t" + str(player.letters_guessed) + "\n\n")


def player_word_progress(secret_word):
    return ["_" if i not in player.letters_guessed else i for i in secret_word]


def ask_for_guess(secret_word):
    # print("the 'Secret' word is", secret_word, ". Shhh ;)")
    guess = input("\n\nGuess the word or a letter:\n").lower()

    check_guess(guess, secret_word)


def game_won():
    clear()
    print(YOU_WIN + "\n\n")
    input("Press Enter to start a new game")
    new_game()


def is_word_guessed(secret_word):
    return secret_word == "".join(player_word_progress(secret_word))


def new_game():
    global hint
    global player

    hint = []
    player = Player()

    hangman(load_word())


def hangman(secret_word):
    clear()
    print(TITLE, "\n\n")
    input("Press ENTER to start")
    clear()
    print(TITLE, "\n\n")
    print(player_word_progress(secret_word))
    ask_for_guess(secret_word)


clear = lambda: os.system('clear')

hint = []
player = Player()
new_game()

