import pygame
import tkinter as tk
from pygame.examples.grid import TILE_SIZE
from pygame.examples.grid import WINDOW_HEIGHT
from pygame.examples.grid import WINDOW_WIDTH
from pygame.examples.grid import TILES_HORIZONTAL
from pygame.examples.grid import TILES_VERTICAL
import os
print(os.path.abspath(pygame.examples.grid.__file__)) # Determining path of imported file's data. In other word, where is pygame.example.grid.

"""
Presently the function only have reference to the value TILE_SIZE, and when I run the file. The interpreter processes it without an errors.
However, this is not useful since the method doesn't actually draw a maze! Why?
Within the context of GUI_Based_Maze_Example, I am still able to draw a maze, but why? 
As I strip it out the other context, an number of errors and warning are being generated:
1. Unresolved reference to tk. | Simple fix, just imported tkinter as tk. 
2. Unresolved reference to WIDTH. | Simple fix, importing WINDOW_WIDTH from the example file, and redefining the reference.
3. Unresolved reference to HEIGHT. | Same as above line. 
4. In this context, there is an unresolved reference to maze, though most of the block of code remained in tact. I did pull the entire file into a new file for testing, and it runs without that error. This means there is a reference that the method uses from somewhere else in the program, but where?
    4a. As i'm trying to understand this reference, I've looking at the code block together. How is the MazeApp class being called? | The main() function.
    However, even after importing the main and its associate statements, the error persists.
    💡🐜🐜🦗🦗 PROBLEM: The Maze was not defined!
        4aii.   SOLUTION: The definition process from Example_Code10 relies on data values for: [WIDTH, HEIGHT,WALL,EMPTY]
        a for loop, and a dictionary. 
        After defining those variable the error was resolved.
5. At this point, the program runs without significant errors, but there are still a number of warnings; and the program still doesn't draw the maze@
    Reviewing Example_Code10, the MazeApp class is fundamentally responsible for making the maze, and it relies on
    a number of methods to run: [__init__, printMaze, visit]. If I comment the method out, the program fails to
    run due to: "AttributeError: 'MazeApp' object has no attribute 'visit' " defined by
    the following line: self.visit(self.markX, self.markY)  # Start maze generation
    
"""


###################################################################################
# Example method from GUI_Based_Maze_Example_1

def draw_maze(self):
    self.canvas.delete("all") # Duplicated in GUI_Based_Maze_Example_1.py - however, I am attempting to look at the line in its own context.
    for y in range(self.rows):
        for x in range(self.cols):
                tile = self.maze[y][x]
                x1 = x * TILE_SIZE #TILE_SIZE is associated with PyGame.
                y1 = y * TILE_SIZE
                x2 = x1 + TILE_SIZE
                y2 = y1 + TILE_SIZE

                color = "lightgray"
                if tile == 'W':
                    color = "black"
                elif tile == 'I' and not self.player.has_item:
                    color = "gold"
                elif tile == 'G':
                    color = "green" if self.player.has_item else "gray"

    self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

        # Draw the player
    px, py = self.player.x, self.player.y
    self.canvas.create_oval(
            px * TILE_SIZE + TILE_SIZE // 4,
            py * TILE_SIZE + TILE_SIZE // 4,
            px * TILE_SIZE + 3 * TILE_SIZE // 4,
            py * TILE_SIZE + 3 * TILE_SIZE // 4,
            fill="blue"
        )

#####################################################################################
## Used for Defining the maze i.e. to the program, it looks something like this.
# MAZE_LAYOUT =
    # [
    #   ['', '', 'W', 'W', 'W'],
    #   ['W', ' ', 'W', 'W', 'W'],
    #   ['W', ' ', ' ', '', 'I'],
    #   ['W', 'W', 'W', 'W', ' '],
    #    [' ', ' ', ' ', 'G', ' ']
    # ]

WALL = chr(777)
maze = {}
for x in range(TILES_HORIZONTAL):
    for y in range(TILES_VERTICAL):
        maze[(x, y)] = WALL  # Every space is a wall at first.

###################################################################################
# Example method from GUI_Based_Maze_Example



class MazeApp:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=WINDOW_WIDTH * 20, height=WINDOW_HEIGHT * 20)  # Each cell is 20x20 pixels
        self.canvas.pack()
        self.maze = maze
        self.hasVisited = [(1, 1)]  # Start by visiting the top-left corner.
        self.markX, self.markY = 1, 1  # Starting position of the '@'
        self.running = True
        self.visit(self.markX, self.markY)  # Start maze generation

    def printMaze(self):
        """Draw the maze on the canvas."""
        self.canvas.delete("all")  # Clear the canvas before drawing
        for y in range(TILES_VERTICAL): # Converted from HEIGHT to TILES_VERTICAL
            for x in range(TILES_HORIZONTAL): # Converted from WIDTH to TILES_HORIZONTAL
                # Calculate the screen coordinates for each cell
                x1, y1 = x * 20, y * 20
                x2, y2 = (x + 1) * 20, (y + 1) * 20

                if self.maze[(x, y)] == WALL:
                    color = "black"
                else:
                    color = "white"

                if self.markX == x and self.markY == y:
                    # Mark the current position with '@' (in red)
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="red")
                else:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)


def main():
    root = tk.Tk()
    root.title("Maze Generator")
    app = MazeApp(root)
    root.mainloop()

#########################################################################