import tkinter as tk
from maze_class import MazeGame

"""
We have modularized the classes out, and are running the game using
a main file called mazegame_main.py.
 
The way this file works is, that once the main runs, 
in the maze_class with import tkinter as tk, and we import the random module.
Then from the player_class we import into the maze_class.py file.
Then we import tk into the mazegame_main.py file, and we imported the mazegame module from
the game module from maze_class.py.
"""

if __name__ == "__main__":
    root = tk.Tk() # This references out to
    root.title("Random Maze Game") # Titles the Maze.
    game = MazeGame(root) # # This references out to maze_class.py, which references player_class.py
    root.mainloop() #Keeps the window open.
