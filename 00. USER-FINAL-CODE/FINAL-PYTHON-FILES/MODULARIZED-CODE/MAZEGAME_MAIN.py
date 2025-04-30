import tkinter as tk
import tkinter.simpledialog
from MAZE_CLASS import MazeGame

"""
We have modularized the classes out, and are running the game using
a main file called MAZEGAME_MAIN.py.
 
The way this file works is, that once the main runs, 
in the maze_class with import tkinter as tk, and we import the random module.
Then from the player_class we import into the MAZE_CLASS.py file.
Then we import tk into the MAZEGAME_MAIN.py file, and we imported the mazegame module from
the game module from MAZE_CLASS.py.
"""

if __name__ == "__main__":
    window = tk.Tk() # This references out to
    window.title("Random Maze Game") # Titles the Maze.
    user_input = tk.simpledialog.askinteger("Set your timer.", "Enter the desired time limit between 30 and 60 seconds:",minvalue=30,maxvalue=120)
    game = MazeGame(window, time_limit=user_input) # # This references out to MAZE_CLASS.py, which references PLAYER_CLASS.py
    window.mainloop() #Keeps the window open.
