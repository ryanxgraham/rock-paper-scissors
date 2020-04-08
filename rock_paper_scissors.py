
"""This program plays a game of Rock, Paper, Scissors between two Players."""

import sys
import os
import time
import random
moves = ['rock', 'paper', 'scissors']



def print_pause(text, length=1):
    """Print a peice of text and waits."""
    print(text)
    time.sleep(length)

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
            move = input('Rock, Paper, Scissors? "x" to Exit>  ').lower()
            if move == 'x':
                print_pause('Goodbye!')
                os.system('clear')
                sys.exit()
            elif move not in moves:
                print_pause("Please pick 'rock', 'paper' or 'scissors',"
                " or 'x' to Exit")
            else:
                break
        return move

class RandomPlayer(Player):
    """Player class that randomly picks moves."""

    def __init__(self):
        """Initialize RandomPlayer."""
        print_pause("\nYou'll never guess!")
    def move(self):
        """Define moveset for RandomPlayer."""
        return (random.choice(moves))


class CyclePlayer(Player):
    """Player class that cycles through moves."""

    def __init__(self):
        """Initialize CyclePlayer."""
        self.my_move = None

        print_pause("\nThere's a method to the madness!")
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
        print_pause("\nI know you are but what am I?")
    def move(self):
        """Define moveset for ReflectPlayer."""
        if self.their_move == None:
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
        print_pause('You won the round!\n')
    elif beats(move2, move1):
        self.loss += 1
        print_pause('You lost the round!\n')
    else:
        self.tie += 1
        print_pause("Tie!\n")

class Game:
    """Parent class for Game functions."""

    def __init__(self, p1, p2):
        """Initialize Game."""
        self.round= 1
        self.p1 = p1
        self.p2 = p2
        self.win = 0
        self.loss = 0
        self.tie = 0


    def play_round(self):
        """Establish round mechanics."""
        move1 = self.p1.move()
        move2 = self.p2.move()
        print_pause(f"\nPlayer 1: {move1}  Player 2: {move2}\n")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        keep_score(self, move1, move2)
        print_pause(f"Wins: {self.win}\nLosses: {self.loss}\nTies: {self.tie}")
        self.round += 1


    def play_game(self):
        """Play the game."""
        print("\nGame start!")
        for round in range(1,6):
            if self.tie == 3:
               print_pause("\nLet's just call it a tie!\n\n")
               break
            elif self.win == 2:
                print_pause('\nYou win! Hooray!\n\n')
                break
            elif self.loss == 2:
                print_pause('\nYou Lose! Boo!\n\n')
                break
            elif self.win < 2 and self.loss < 2:
                print(f"\nRound {round}:\n")
                self.play_round()




if __name__ == '__main__':
    opponents = [Player, RandomPlayer, CyclePlayer, ReflectPlayer]
    os.system('clear')
    game = Game(HumanPlayer(), random.choice(opponents)())
    game.play_game()
