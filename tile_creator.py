"""
Brandan Yong
CS 5001 SP 2024
Dr. Bagley
Final Project

    This module will handle the creation of tiles as instances to be further
    manipulated in later functions.
"""
import turtle
import random
import math
import os
def list_of_gifs(puz_file: str):
    """
    Fxn will take in puz file and return name of puzzle, number of tiles,
    size of tiles, thumbnail gif, and a list of the gif file names.
    Parameters: puz_file (str)
    Return: name, number of tiles, size, thumbnail, list of file names
    """
    file_names = []
    # open puz file
    with open(puz_file, 'r') as puz:
        # take in name of puzzle
        name_line = puz.readline().strip().split()
        name = str(name_line[-1])
##        print(name)

        # take in number of pieces
        number_line = puz.readline().strip().split()
        pieces = int(number_line[-1])
##        print(pieces)

        # take in size of gif
        size_line = puz.readline().strip().split()
        square_size = int(size_line[-1])
##        print(square_size)

        # take in thumbnail gif
        thumbnail_line = puz.readline().strip().split(" ")
        thumbnail = str(thumbnail_line[-1])
##        print(thumbnail)

        # iterate through order/names of gifs and save to list
        for line in puz:
            line = line.strip().split(" ")
            gif = line[-1]
            file_names.append(gif)
##            print(gif)
##        print(file_names)
    return file_names, name, pieces, square_size, thumbnail

def add_gifs(puz_file: str):
    """
    Fxn will take in a puz file name (str), and will utilize the list_of_gifs
    fxn to sort out data as needed for later use
    Parameters: puz_file (str)
    Return: gifs, name, pieces, size, thumbnail
    """
    global screen
    # call pieces fxn to create list of gifs
    gifs, name, pieces, size, thumbnail = list_of_gifs(puz_file)

    # iterate through lists to add shapes
    for i in range(len(gifs)):
        turtle.addshape(gifs[i])

    # add thumbnail gif
    turtle.addshape(thumbnail)
    return gifs, name, pieces, size, thumbnail

def get_puz_files():
    """
    Fxn will utilize os module to get the names of puz files in working
    directory, and will return the names of the puz files.
    Return: puz_files(str)
    """
    puz_files = []
    folder_path = os.getcwd()
    files = os.listdir(folder_path)
##    print(files)
    for each in files:
        if ".puz" in each:
            puz_files.append(each)
    print(puz_files)
    return puz_files
