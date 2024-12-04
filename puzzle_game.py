"""
Brandan Yong
CS 5001 SP 2024
Dr. Bagley
Final Project
"""
from Resources import gameboard, splashscreen
import tile_creator
import turtle
import random
import math
import time
import os

def puzzle_maker(puz_file: str, moves: int, user: str):
    """
    Fxn takes in puz_file (str), moves (int), and user (str) and calls on
    add_gifs fxn in tile_creator module to utilize data for puzzle, and add
    puzzle's gifs as shapes.
    Parameters: puz_file (str), moves (int), name (str)
    Return: turtles (dict), solved_turtles(dict)
    """
    global screen

    turtles = {} # this dict will contain the current tile instance coordinates
    solved_turtles = {} # this will contain the winning configuration

    # create instance for moves line to be updated/reset
    moves_line = turtle.Turtle()
    moves_line.shape("turtle")
    moves_line.hideturtle()

    # call add_gifs function to take in needed variables
    list_of_gifs, name, pieces, size, tnail = tile_creator.add_gifs(puz_file)

    # fix tile size for visual clarity
    size = 100 

    # add thumbnail to screen
    thumbnail = turtle.Turtle()
    thumbnail.teleport(300, 300)
    thumbnail.shape(tnail)
    
    # create copies of list of gifs to not alter data
    copy = list_of_gifs.copy()
    solved_copy = list_of_gifs.copy()

    # define the number of rows and columns by taking sqrt of total pieces
    rows = int(math.sqrt(pieces))
    cols = int(math.sqrt(pieces))
    if (rows * cols) != pieces:
        raise ValueError

    # assemble puzzle
    for col in range(cols):
        for row in range(rows):

            # create a tile instance
            tile = turtle.Turtle()
            tile.speed(0)
            tile.penup()

            # calculate start position of current tile
            start_x = -350 + row * size
            start_y = 200 - col * size

            # move instance to corner of square
            tile.goto(start_x, start_y)
            tile.pendown()

            # draw square then move to middle of it
            for _ in range(4):
                tile.forward(100)
                tile.left(90)
            x = start_x + size / 2
            y = start_y + size / 2
            tile.teleport(x, y)

            # take random gif choice and make tile shape the gif
            gif = random.choice(copy)
            copy.remove(gif)
            tile.shape(gif)

            # iterate through input list to create dict with correct values
            right_gif = list_of_gifs[0]
            list_of_gifs.remove(right_gif)

            # add tile for key and coordinates as the value
            turtles[f"{tile.shape()}"] = (x, y)
            solved_turtles[f"{right_gif}"] = (x, y)

            # keep track/update number of moves
            i = 0
            line = f"Player moves: {i}"
            moves_line.teleport(-325, -300)
            moves_line.write(line, font=('Arial', 30, 'normal'))

            def callback(x, y, moves= int(moves), user= str(user), tile= tile):
                """
                Fxn will take in x, y coordinates, moves, user, and tile. Fxn
                then will call next_to to check if tile instance is adjacent to
                the blank tile instance, if True, will update counter, and will
                check if counter is less than moves, prompting the fxn you_lose
                from the gameboard module if counter is greater than moves. If
                within bounds, fxn will update moves on screen, and uitilize
                swap_tile function to switch the two tiles, and finally will
                update the turtles dictionary, and check if the turtles dict
                has the same key/value as the solved_turtles dictionary, which
                prompts the you_win fxn, and will append the winners name, and
                number of moves taken to solve the puzzle to the winners.txt
                file.
                Parameters: x, y (float), moves (int), user (str),
                            tile (turtle instance)
                Return: you_lose (function) if i>moves, you_win (function) if
                        tiles are in winning configuration, or i (int),
                        turtles (dict), and solved_turtles (dict) if user has
                        more moves to play.
                """
                # call upon i, moves_line, turtles, solved_turtles from higher
                # order function.
                nonlocal i, moves_line, turtles, solved_turtles

                try:

                    # clear previous move number to update
                    moves_line.clear()

                    # conditional to update move counter
                    if next_to(tile) == True:
                        i += 1
                    else:
                        pass
                    # conditional to prompt lose screen if user goes over limit
                    if i > moves:
                        return gameboard.GameBoard.you_lose()

                    line = f"Player moves: {i}"
                    moves_line.write(line, font=('Arial', 30, 'normal'))
                    b_x, b_y, b_tile, b_turtle, swap = swap_tiles(tile)

                    # conditional to update coords if tile is swapped
                    if swap == True:
                        turtles[f"{tile.shape()}"] = (tile.xcor(),tile.ycor()) 
                        turtles[f"{b_tile}"] = (b_x, b_y)
    ##                    print(turtles[f"{tile.shape()}"])
    ##                    print(turtles[f"{b_tile}"])
                    else:
                        pass

                    # conditional to check if puzzle was solved
                    if turtles == solved_turtles:
    ##                    print('you win')
    ##                    turtle.done()
                        with open('winners.txt', 'a+') as winners:
                            winners.write(f"{i} {user}\n")
                        return gameboard.GameBoard.you_win()
                    return i, turtles, solved_turtles                    

                except TypeError:
                    error = "TypeError"
                    splashscreen.error_logging(error)
                    pass
            tile.onclick(callback)
##    print(turtles)
##    print(solved_turtles)
    return turtles, solved_turtles
                
def find_blank_tile():
    """
    Fxn will find position of blank tile instance on the screen, and will
    return blank_x, blank_y, blank_tile, and blank_instance.
    Returns: blank_x (float), blank_y (float), blank_tile (str),
             blank_instance (turtle instance)
    """
    global screen

    # iterate through turtles on screen to find the blank tile via shape name
    for turtle in screen.turtles():
        if "blank" in turtle.shape():
##            print(turtle.xcor())
##            print(turtle.ycor())
            blank_x = turtle.xcor()
            blank_y = turtle.ycor()
            blank_tile = turtle.shape()
            blank_instance = turtle
    return blank_x, blank_y, blank_tile, blank_instance

def next_to(tile):
    """
    Fxn will take in tile instance in question, and will return true if
    instance is next to blank tile, false if not.
    Parameters: tile (turtle instance)
    Return: True if tile instance is adjacent to blank tile, False if not.
    """
    global screen
##    print(tile.xcor())
##    print(tile.ycor())
    tile_x = tile.xcor()
    tile_y = tile.ycor()
    blank_x, blank_y, blank_tile, blank_instance = find_blank_tile()
##    print(blank_x)
##    print(blank_y)
    
    if abs(blank_x - tile_x) == 0 and abs(blank_y - tile_y) == 100:
##        print("true")
        return True
    elif abs(blank_x - tile_x) == 100 and abs(blank_y - tile_y) == 0:
##        print("true")
        return True   
    else:
##        print("false")
        return False

def swap_tiles(tile):
    """
    Fxn will take in the tile instance, and utilize function next_to, and
    find_blank_tile to see if the selected tile is adjacent to the blank
    tile instance. If next_to returns True, then the tile will switch
    coordinates with the blank tile instance, and will return the new
    x and y for the blank tile, the instance itself, and "swapped", a boolean
    where value is True if the tiles have swapped places.
    Parameters: Tile
    Return: b_x (float), b_y (float), blank_tile (turtle instance), swapped (bool)
    """
    global screen

    try:
        # call find_blank_tile to locate blank tile instance
        blank_x, blank_y, blank_tile, blank_instance = find_blank_tile()

        # true if tile instance next to blank tile
        if next_to(tile) == True: 

            # store tile x and y to move blank tile instance
            holder_x = tile.xcor()
            holder_y = tile.ycor()

            # teleport tile instance to blank_instance, vice versa
            blank_instance.teleport(holder_x, holder_y)
            tile.teleport(blank_x, blank_y)

            # store and return new coordinates for blank tile
    ##        print(blank_instance.xcor())
    ##        print(blank_instance.ycor())
            b_x = blank_instance.xcor()
            b_y = blank_instance.ycor()
        
            # store variable as true for later use
            swapped = True
        
        return b_x, b_y, blank_tile, blank_instance, swapped

    except UnboundLocalError:
        error = "UnboundLocalError"
        splashscreen.error_logging(error)
        pass
    except TypeError:
        error = "TypeError"
        splashscreen.error_logging(error)
        pass
    
# Gameboard functions
def reset_button(solved_turtles, turtles):
    """
    Fxn will create a turtle instance, and turn the instance into the reset
    button gif. Upon clicking on instance, each respective instance will
    teleport to the coordinates to create the winning configuration.
    Parameters: solved_turtles (dict), turtles (dict)
    Returns: solved_turtles (dict), turtles (dict)
    """
    global screen
    
    # creating instance for reset button
    reset_instance = turtle.Turtle() 
    reset_instance.teleport(50, -300)
    reset = "Resources/resetbutton.gif"
    turtle.addshape(reset)
    reset_instance.shape(reset)

    # create handler function for onclick instance
    def handler(x, y, reset_instance= reset_instance):
        """
        Fxn will handle onclick pass to solved_puzzle fxn
        Parameters: x, y (float), reset_instance (turtle instance)
        """
        global screen
        for i, t in enumerate(turtle.turtles()):
            for gif, coord in solved_turtles.items():
                if t.shape() == gif:
                    t.teleport(coord[0], coord[-1])
                    turtles[gif] = (coord[0], coord[-1])
                    
    reset_instance.onclick(handler)
    return turtles, solved_turtles

##    return reset_instance

def load_button(moves: int, user: str):
    """
    Fxn will create load button instance, and upon clicking on this instance,
    will prompt user to select a puzzle to load and attempt to solve, while
    resetting the move counter.
    Parameters: Moves (int), User (str)
    """
    load_instance = turtle.Turtle()
    load_instance.teleport(150, -300)
    load = "Resources/loadbutton.gif"
    turtle.addshape(load)
    load_instance.shape(load)

    def handler(x, y, moves= int(moves)):
        """
        Fxn will take in x, y coordinates, and moves, and will prompt user to
        input a puz file to attempt to solve.
        Parameters: x, y (float), moves (int)
        """
        try:
            puz_files = tile_creator.get_puz_files()
            choices = "\n".join(puz_files)
            puzzle = turtle.textinput(
                "Load Puzzle", "Enter the puzzle you wish to load\n"
                f"Choices are:\n{choices}")

            # conditional for malformed puzzles
            if "malformed" in puzzle:
                raise FileNotFoundError

            # iterate through turtle instances
            for i, t in enumerate(turtle.turtles()):

                # remove old puzzle pieces
                if "Images" in t.shape():
                    t.clear()
                    t.hideturtle()

                # reset moves counter
                if "turtle" in t.shape():
                    t.clear()
                    t.hideturtle()
            turtles, solved_turtles = puzzle_maker(
                str(puzzle), int(moves), str(user))
            reset_button(solved_turtles, turtles)

        except FileNotFoundError:
            j = turtle.Turtle()
            turtle.addshape("Resources/file_error.gif")
            j.shape("Resources/file_error.gif")
            turtle.ontimer(j.clear, 3000)
            with open('5001_puzzle.err', 'a+') as error_log:
                error = "FileNotFoundError"
                splashscreen.error_logging(error)
            time.sleep(3)
            j.hideturtle()
            return handler(x, y, moves= int(moves))
            
    load_instance.onclick(handler)
##    return load_instance

def quit_button():
    """
    Fxn will create quit button instance, upon clicking on the instance,
    will prompt the quit gif, then after a few seconds will close the program.
    """
    quit_instance = turtle.Turtle()
    quit_instance.teleport(250, -300)
    button = "Resources/quitbutton.gif"
    turtle.addshape(button)
    quit_instance.shape(button)

    def handler(x, y):
        return gameboard.GameBoard.click_to_quit(x, y)

    quit_instance.onclick(handler)
##    return quit_instance
    
def main():
    global screen
    # set up screen and buttons
    screen = turtle.Screen()

    # splash screen and names/moves prompt    
    splashscreen.SplashScreen.load_in()
    user = splashscreen.SplashScreen.your_name()
    moves = splashscreen.SplashScreen.number_of_moves()
    gameboard.GameBoard.create_gameboard()
    
    # default puzzle at start is mario puzzle
    default = "mario.puz"
    turtles, solved_turtles = puzzle_maker(default, int(moves), str(user))

    # buttons
    reset_button(solved_turtles, turtles)
    load_button(int(moves), str(user))
    quit_button()

    find_blank_tile()

    turtle.mainloop()

if __name__ == "__main__":
    main()
