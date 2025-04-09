""" Initially, thought that the .PY failed to generate a GUI, but this
was simply a timing problem. This .py does generate a maze, but it cannot be
interacted with. We need to attempt to overlay the play_movement to enable this."""

import random
import tkinter as tk

WIDTH = 39  # Width of the maze (must be odd)
HEIGHT = 19  # Height of the maze (must be odd)
assert WIDTH % 2 == 1 and WIDTH >= 3
assert HEIGHT % 2 == 1 and HEIGHT >= 3
SEED = 1
random.seed(SEED)

# Use these characters for displaying the maze:
EMPTY = ' '
MARK = '@'
WALL = chr(9608)  # Character 9608 is '█'
NORTH, SOUTH, EAST, WEST = 'n', 's', 'e', 'w'

# Create the filled-in maze data structure to start:
maze = {}
for x in range(WIDTH):
    for y in range(HEIGHT):
        maze[(x, y)] = WALL  # Every space is a wall at first.


class MazeApp:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=WIDTH * 20, height=HEIGHT * 20)  # Each cell is 20x20 pixels
        self.canvas.pack()

        self.maze = maze
        self.hasVisited = [(1, 1)]  # Start by visiting the top-left corner.
        self.markX, self.markY = 1, 1  # Starting position of the '@'
        self.running = True
        self.visit(self.markX, self.markY)  # Start maze generation

    def printMaze(self):
        """Draw the maze on the canvas."""
        self.canvas.delete("all")  # Clear the canvas before drawing
        for y in range(HEIGHT):
            for x in range(WIDTH):
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

    def visit(self, x, y):
        """Carve out spaces in the maze and update the GUI."""
        self.maze[(x, y)] = EMPTY
        self.printMaze()

        # Delay for a short time to show the changes in the maze
        self.root.after(50)

        while True:
            unvisitedNeighbors = []
            if y > 1 and (x, y - 2) not in self.hasVisited:
                unvisitedNeighbors.append(NORTH)
            if y < HEIGHT - 2 and (x, y + 2) not in self.hasVisited:
                unvisitedNeighbors.append(SOUTH)
            if x > 1 and (x - 2, y) not in self.hasVisited:
                unvisitedNeighbors.append(WEST)
            if x < WIDTH - 2 and (x + 2, y) not in self.hasVisited:
                unvisitedNeighbors.append(EAST)

            if len(unvisitedNeighbors) == 0:
                return  # Backtrack when no unvisited neighbors are left
            else:
                nextIntersection = random.choice(unvisitedNeighbors)

                if nextIntersection == NORTH:
                    nextX = x
                    nextY = y - 2
                    self.maze[(x, y - 1)] = EMPTY  # Connecting hallway
                elif nextIntersection == SOUTH:
                    nextX = x
                    nextY = y + 2
                    self.maze[(x, y + 1)] = EMPTY  # Connecting hallway
                elif nextIntersection == WEST:
                    nextX = x - 2
                    nextY = y
                    self.maze[(x - 1, y)] = EMPTY  # Connecting hallway
                elif nextIntersection == EAST:
                    nextX = x + 2
                    nextY = y
                    self.maze[(x + 1, y)] = EMPTY  # Connecting hallway

                self.hasVisited.append((nextX, nextY))
                self.markX, self.markY = nextX, nextY
                self.visit(nextX, nextY)  # Recursive call to visit next cell


def main():
    root = tk.Tk()
    root.title("Maze Generator")
    app = MazeApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
