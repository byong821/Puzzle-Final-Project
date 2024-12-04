"""
Brandan Yong
CS 5001 SP2024
Dr. Bagley
Final Project

    This module is made to handle all functions needed to initiate the
    splash screen at the start of the game to take in player name and
    requested number of moves.
"""
import turtle
import time
import datetime
class SplashScreen:
    def your_name():
        """
        Fxn prompts user to input name, and will return inputted name for
        later use.
        Return: name (str)
        """
        try:
            name = turtle.textinput("CS5001 Puzzle Game", "Your Name: ")

            # protective coding to ensure type for name
            if type(name) != str:
                raise TypeError
            return name
        except TypeError:
            error = "TypeError"
            error_logging(error)
            name = SplashScreen.your_name()
            return name
    def number_of_moves():
        """
        Fxn prompts user to input number of moves that they request, and
        returns moves for later use.
        Return: moves (int)
        """
        try:
            moves = turtle.textinput("5001 Puzzle Slide - Moves",
            "Enter the number of moves (chances) you want (5-200)?")
            moves = int(moves)
            
            # protective coding for bad data
            if int(moves) < 5 or int(moves) > 200: 
                raise ValueError
            elif type(moves) != int:
                raise TypeError
            return moves
        except TypeError:
            error = "TypeError"
            error_logging(error)
            moves = SplashScreen.number_of_moves()
            return moves
        except ValueError:
            error = "ValueError"
            error_logging(error)
            moves = SplashScreen.number_of_moves()
            return moves

    def load_in():
        """
        Fxn presents the splashscreen, then delays program for 3 seconds,
        then clears the splashscreen from the screen.
        """
        turtle.bgpic("Resources/splash_screen.gif")
        turtle.update()
        time.sleep(3)
        turtle.clearscreen()
    
def error_logging(error):
    """
    fxn takes in an error and appends it to the error log.
    parameter: error (str)
    """
    
    with open('5001_puzzle.err', 'a+') as error_log:
        current_date_time = datetime.datetime.now()
        error_log.write(f"{current_date_time} : {error}\n")
        

