"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import time
import random




"""The Player class is the parent class for all of the Players
in this game"""

def print_pause(text, length=1):
    print(text)
    time.sleep(length)


def valid_input(prompt, moves):
    while True:
        response = input(prompt).lower()
        for move in moves:
            if move in response:
                return response
            else:
                print_pause("Please pick 'rock', 'paper' or 'scissors'")

class Player:
    def __init__(self, moves):
        moves = ['rock', 'paper', 'scissors']

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move

class HumanPlayer(Player):
    move1 = valid_input('Rock, Paper, Scissors?>  ', moves)


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

class CyclePlayer(Player):
    def move(self):
        for i in range (2):
            if i <= 2:
                return moves[i]
                i += 1
            else:
                i = 0
                return moves[i]

class ReflectPlayer(Player):
    def move(self):
        if self.their_move == None:
            return random.choice(moves)
        else:
            move = self.their_move

def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:


    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score_p1 = 0
        self.score_p2 = 0

    def play_round(self):
        round_count = 0
        print(f"Round:{round_count}")
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        round_count +=1

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    game = Game(Player(), Player())
    game.play_game()
