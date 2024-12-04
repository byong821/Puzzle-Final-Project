"""
Brandan Yong
CS 5001 SP2024
Dr. Bagley
Final Project

    This module will create the gameboard, along with its functions
"""
import turtle
import puzzle_game
import tile_creator
import time

class GameBoard:
    def leaderboard():
        """
        Fxn will construct the leaderboard by creating a turtle instance,
        then it will call winners to write out any previous winners.
        """
        global screen
        # instance for leaderboard
        leaderboard_instance = turtle.Turtle() 
        leaderboard_instance.teleport(300, -200)
        leaderboard_instance.color('purple')
        leaderboard_instance.pensize(5)
        leaderboard_instance.speed(0)
        leaderboard_instance.left(90)
        leaderboard_instance.hideturtle()
        turtle.pendown()

        # loop for creating outline
        for _ in range(2): 
            leaderboard_instance.forward(500)
            leaderboard_instance.left(90)
            leaderboard_instance.forward(175)
            leaderboard_instance.left(90)
        leaderboard_instance.teleport(135, 250)

        # protective coding to ensure valid file is inputted
        try:
            GameBoard.winners(leaderboard_instance)
        except FileNotFoundError:
            t = turtle.Turtle()
            turtle.addshape("Resources/leaderboard_error.gif")
            t.shape("Resources/leaderboard_error.gif")
            time.sleep(3)
            t.hideturtle()
            pass

    def winners(leaderboard_instance):
        """
        Fxn will take in leaderboard instance, and go into winners.txt file
        and print onto screen historical winners.
        Parameters: leaderboard_instance (turtle instance)
        """
        global screen
        winner_dict = {}
        with open('winners.txt', 'r') as winners:
            for line in winners:
                line = line.strip().split()
##                print(line[0])
##                print(line[-1]) 
                winner_dict[f"{line[-1]}"] = line[0]
        leaderboard_instance.write("Leaders:", font=('Arial', 20, 'normal'))
        y = 230
        for i, j in winner_dict.items():
            leaderboard_instance.teleport(135, y)
            leaderboard_instance.write(
                f"{j}: {i}", font=('Arial', 20, 'normal'))
            y -= 20

        
    def play_area():
        """
        Fxn will create a turtle instance to construct the play area where
        tiles will be located.
        """
        # instance for play area
        play_area_instance = turtle.Turtle() 
        play_area_instance.teleport(100, -200)
        play_area_instance.pensize(5)
        play_area_instance.speed(0) # max speed

        # loop to create outline
        for _ in range(2): 
            play_area_instance.left(90)
            play_area_instance.forward(500)
            play_area_instance.left(90)
            play_area_instance.forward(450)
            
    def status_area():
        """
        Fxn will create a turtle instance to construct the status area where
        buttons will be located.
        """
        # instance for status area
        status_area_instance = turtle.Turtle() 
        status_area_instance.teleport(-350, -250)
        status_area_instance.pensize(5)
        status_area_instance.speed(0)

        # loop to create outline
        for _ in range(2):
            status_area_instance.forward(650)
            status_area_instance.right(90)
            status_area_instance.forward(100)
            status_area_instance.right(90)
        
    def create_gameboard():
        """
        Fxn will call on leaderboard, play_area, and status_area functions
        """
        GameBoard.leaderboard()
        GameBoard.play_area()
        GameBoard.status_area()
                            
    def credit_gif():
        """
        Fxn will create a turtle instance to present the credits gif
        """
        # create turtle instance
        creds = turtle.Turtle()
        turtle.addshape("Resources/credits.gif")
        creds.shape("Resources/credits.gif")

        # disable any interaction with screen
        turtle.onscreenclick(None)
        turtle.ontimer(turtle.bye, t= 5000)

    def click_to_quit(x, y):
        """
        Fxn will create a turtle instance to present the quit gif message,
        taking in the x,y coordinates of the user click when they click on
        the quit_button instance.
        Parameters: x, y (float)
        """
        # instance to show quit message
        show_message = turtle.Turtle() 
        turtle.addshape("Resources/quitmsg.gif")
        show_message.shape("Resources/quitmsg.gif")

        # disable any interaction with screen
        turtle.onscreenclick(None) 
        turtle.ontimer(turtle.bye, t=5000)

    def you_win():
        """
        Fxn will create a turtle instance to present the winner gif, then
        call the credit_gif function.
        """
        # create turtle instance
        message = turtle.Turtle()
        turtle.addshape("Resources/winner.gif")
        message.shape("Resources/winner.gif")
        turtle.ontimer(GameBoard.credit_gif, t = 3000)

    def you_lose():
        """
        Fxn will create a turtle instance to present the lose gif, then call
        the credit_gif function.
        """
        # create turtle instance
        message = turtle.Turtle()
        turtle.addshape("Resources/Lose.gif")
        message.shape("Resources/Lose.gif")
        turtle.ontimer(GameBoard.credit_gif, t = 3000)

