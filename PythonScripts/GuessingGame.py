import time
import datetime


class GuessingGame(object):

    def __init__(self):
        self.guesses = 0
        self.number = 0


    def start_game(self):
        try:
            return "Guess a number between 1 and 10"
        except Exception as ex:
            print("error")

    def make_guess(self, value):
        self.guesses = self.guesses + 1
        if value == self.number:
            print("From Script: winner")
            return "winner"
        else:
            print("From Script: guess again")
            return "guess again"

    def clear_list(self):
        self.guesses = 0


    def set_number_to_guess(self, value):
       self.number = value
        

#start server if not imported as module
if __name__ == '__main__':
    print("game is running as a program")
    game = GuessingGame()
    response = game.start_game
    print(respone)

else:
    print("game imported as a module")

