
"""This program plays a game of Rock, Paper, Scissors between two Players."""

import sys
import os
import time
import random
moves = ['rock', 'paper', 'scissors']

# TODO: add "match options", eg 2 of 3, 3 of 5, first to 10, etc


def print_pause(text, length=.8):
    """Print a peice of text and wait for some time."""
    print(text)
    time.sleep(length)


def valid_input(prompt, options):
    """Validate input for certain functions."""
    while True:
        response = input(prompt).lower()
        for option in options:
            if option in response:
                return response
        print_pause("That doesn't work, try again.", 1)


class Player:
    """The Player class is the parent class for all of the Players."""

    def __init__(self):
        """Initialize Player class."""
    def move(self):
        """Define moveset for default Player."""
        return 'rock'

    def learn(self, my_move, their_move):
        """Learn opponents moves."""
        self.my_move = my_move
        self.their_move = their_move


class HumanPlayer(Player):
    """Player class controlled by user."""

    def move(self):
        """Define how HumanPlayer selects moves."""
        while True:
            move = input(
                        '\033[1;30;47m'
                        'Rock, Paper, Scissors? "x" to Exit>>>'
                        '\033[0m   '
                        ).lower()
            if move == 'x':
                print_pause(
                            '\n\033[1;32m'
                            'Goodbye!'
                            '\033[0m\n\n'
                            )
                time.sleep(2.5)
                os.system('clear')
                sys.exit()
            elif move not in moves:
                print_pause("Please pick 'rock', 'paper' or 'scissors',"
                            " or 'x' to Exit", .5)
            else:
                break
        return move


class RandomPlayer(Player):
    """Player class that randomly picks moves."""

    def __init__(self):
        """Initialize RandomPlayer."""
        print_pause(
                    "\033[1;34m"
                    "\nYou'll never guess!"
                    "\033[0m\n"
                    )

    def move(self):
        """Define moveset for RandomPlayer."""
        return (random.choice(moves))


class CyclePlayer(Player):
    """Player class that cycles through moves."""

    def __init__(self):
        """Initialize CyclePlayer."""
        self.my_move = None

        print_pause(
                    "\033[1;34m"
                    "\nThere's a method to the madness!"
                    "\033[0m\n"
                    )

    def move(self):
        """Define moveset for CyclePlayer."""
        if self.my_move == 'rock':
            return moves[1]
        elif self.my_move == 'paper':
            return moves[2]
        else:
            return moves[0]


class ReflectPlayer(Player):
    """Player class that copies player moves."""

    def __init__(self):
        """Initialize ReflectPlayer."""
        self.their_move = None
        print_pause(
                    "\033[1;34m"
                    "\nI know you are but what am I?"
                    "\033[0m\n"
                    )

    def move(self):
        """Define moveset for ReflectPlayer."""
        if self.their_move is None:
            return random.choice(moves)
        else:
            return self.their_move


def beats(one, two):
    """Define round results."""
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


def keep_score(self, move1, move2):
    """Keep track of and display game score."""
    if beats(move1, move2):
        self.win += 1
        print_pause(
                    '\033[1;32m'
                    'You won the round!'
                    '\033[0m'
                    )
    elif beats(move2, move1):
        self.loss += 1
        print_pause(
                    '\033[1;31m'
                    'You lost the round!'
                    '\033[0m'
                    )
    else:
        self.tie += 1
        print_pause(
                    "\033[1;34m"
                    "Tie!"
                    "\033[0m"
                    )


class Game:
    """Parent class for Game functions."""

    def __init__(self, p1, p2):
        """Initialize Game."""
        self.round = 1
        self.p1 = p1
        self.p2 = p2
        self.win = 0
        self.loss = 0
        self.tie = 0

    def play_round(self):
        """Establish round mechanics."""
        move1 = self.p1.move()
        move2 = self.p2.move()
        if beats(move1, move2):
            print_pause(
                        "\nPlayer 1:"
                        "\033[1;32m"
                        f"{move1.upper()}"
                        "\033[0m\n"
                        "Player 2:"
                        "\033[1;31m"
                        f"{move2.upper()}"
                        "\033[0m\n"
                        )
        elif beats(move2, move1):
            print_pause(
                        "\nPlayer 1:"
                        "\033[1;31m"
                        f"{move1.upper()}"
                        "\033[0m\n"
                        "Player 2:"
                        "\033[1;32m"
                        f"{move2.upper()}"
                        "\033[0m\n"
                        )
        else:
            print_pause(
                        "\nPlayer 1:"
                        "\033[1;34m"
                        f"{move1.upper()}"
                        "\033[0m\n"
                        "Player 2:"
                        "\033[1;34m"
                        f"{move2.upper()}"
                        "\033[0m\n"
                        )
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        keep_score(self, move1, move2)
        print_pause(
                    "\n\033[1;33;40m"
                    f"Wins:   {self.win}\n"
                    f"Losses: {self.loss}\n"
                    f"Ties:   {self.tie}\n"
                    "\033[0m"
                    )
        self.round += 1

    def play_game(self):
        """Play the game."""
        for round in range(1, 6):
            if self.tie == 3:
                print_pause(
                           "\n\033[5;34m"
                           "Tie Game! Meh!"
                           "\033[0m\n",
                           3)
                replay()
            elif self.win == 2:
                print_pause(
                            '\n\033[5;32m'
                            'You win! Hooray!'
                            '\033[0m\n',
                            3)
                replay()
            elif self.loss == 2:
                print_pause(
                            '\n\033[5;31m'
                            'You Lose! Boo!'
                            '\033[0m\n',
                            3)
                replay()
            elif self.win < 2 and self.loss < 2:
                print_pause(
                            "\033[1;35m"
                            f"Round {round}:"
                            "\033[0m\n"
                            )
                self.play_round()


def replay():
    """Prompt player if they would like to play again."""
    yes_list = ["Yeehaw!", "Oh no not again!", "Lets do this!",
                "One more turn!", "Why does this keep happening to me?"]
    choice = valid_input("\nWould you like to play again? y/n?>>>", ["y", "n"])

    if choice == "y":
        print_pause(random.choice(yes_list))
        os.system('clear')
        game = Game(HumanPlayer(), random.choice(opponents)())
        game.play_game()
    elif choice == "n":
        print_pause(
                    "\033[1;31m"
                    "Get me out of here!"
                    "\n\033[0m", 1.5)
        print_pause(
                    "\033[1;32m"
                    "Thanks for playing!"
                    "\n\033[1:32m", 3)
        os.system('clear')
        sys.exit()


if __name__ == '__main__':

    os.system('clear')
    print_pause(
                "\033[1;36m"
                "Rock, Paper, Scissors..."
                "\n\033[0m",
                3
                )
    print_pause(
                "\033[5;32m"
                "Go!"
                "\033[0m",
                1.5
                )
    opponents = [Player, RandomPlayer, CyclePlayer, ReflectPlayer]
    game = Game(HumanPlayer(), random.choice(opponents)())
    game.play_game()
