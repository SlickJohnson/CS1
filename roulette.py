import random
random.seed(1)

bank_account = 1000
bet_amount = 0
bet_color = None
bet_number = None

green = [0, 37]
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]


def take_bet(color, number, amount):
    bet_color = color
    bet_number = number
    bet_amount = amount

    return [bet_color, bet_number, bet_amount]


def roll_ball():
    '''returns a random number between 0 and 37'''

    return random.randint(0, 38)


def check_results(ball_roll, bet_info):
    '''Compares bet_color to color rolled.  Compares
    bet_number to number_rolled.'''

    print("The ball number is " + str(bet_info[2]) + "...\n")
    payout(ball_roll == bet_info[2], bet_info)


def payout(did_win, bet_info):
    '''returns total amount won or lost by user based on results of roll. '''

    if did_win:
        print("YOU WON! Your now have $", str(bank_account + bet_info[2]))

    else:
        print("YOU LOST!!! HAHAHA! You now have $", str(bank_account - bet_info[2]))


def play_game():
    """This is the main function for the game.
    When this function is called, one full iteration of roulette,
    including:

    Take the user's bet.
    Roll the ball.
    Determine if the user won or lost.
    Pay or deduct money from the user accordingly.
    """
    color = input("Choose color\n")
    number = 0

    if color == "green":
        number = input("Choose a number from this list: " + str(green) + "\n")

    elif color == "red":
        number = input("Choose a number from this list: " + str(red) + "\n")

    elif color == "black":
        number = input("Choose a number from this list: " + str(black) + "\n")

    else:
        print("Whoops! That's not a color supported by this game. Try again..")
        play_game()

    check_results(roll_ball(), take_bet(color, int(number), int(input("Bet amount?\n"))))


play_game()
