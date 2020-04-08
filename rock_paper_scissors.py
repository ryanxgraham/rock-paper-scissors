"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import sys
import os
import time
import random
moves = ['rock', 'paper', 'scissors']
"""The Player class is the parent class for all of the Players
in this game"""

def print_pause(text, length=1):
    print(text)
    time.sleep(length)

class Player:
    def __init__(self):
        self.win = 0
        self.loss = 0
        self.tie = 0
        self.my_move = None
        self.their_move = None
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move

class HumanPlayer(Player):
    def move(self):
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
    def __init__(self):
        # Player.__init__(self)
        print_pause("\nYou'll never guess!")
    def move(self):
        return (random.choice(moves))


class CyclePlayer(Player):
    def __init__(self):
        # Player.__init__(self)

        print_pause("\nThere's a method to the madness!")
    def move(self):
        if self.my_move == 'rock':
            return moves[1]
        elif self.my_move == 'paper':
            return moves[2]
        else:
            return moves[0]


class ReflectPlayer(Player):
    def __init__(self):
        # Player.__init__(self)

        print_pause("\nI know you are but what am I?")
    def move(self):
        if self.their_move == None:
            return random.choice(moves)
        else:
            return self.their_move

def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:

    def __init__(self, p1, p2):
        self.round= 1
        self.p1 = p1
        self.p2 = p2


    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"\nPlayer 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        self.round += 1


    def play_game(self):
        print("\nGame start!")
        for round in range(1,4):
            print(f"Round {round}:\n")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    opponents = [Player, RandomPlayer, CyclePlayer, ReflectPlayer]
    os.system('clear')
    game = Game(HumanPlayer(), random.choice(opponents)())
    game.play_game()
