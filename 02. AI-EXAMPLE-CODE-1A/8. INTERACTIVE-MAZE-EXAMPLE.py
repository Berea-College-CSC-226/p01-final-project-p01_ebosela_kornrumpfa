import tkinter as tk
import pygame
from pygame.examples.moveit import WIDTH, HEIGHT
from GUI_Based_Maze_Example import print
import logging

# logging.basicConfig(filename='my_log_file.log',
#                     level=logging.DEBUG,
#                     format='%(asctime)s - %(levelname)s - %(message)s')
#
# logging.info("Program started")
# logging.error("An error occurred")

class MazeApp:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=WIDTH * 20, height=HEIGHT * 20)
        self.canvas.pack()

        self.maze = maze
        self.hasVisited = [(1, 1)]
        self.markX, self.markY = 1, 1  # For generation only
        self.playerX, self.playerY = 1, 1  # For movement after generation
        self.generateMaze()

        self.root.bind("<Up>", lambda e: self.move_player(0, -1))
        self.root.bind("<Down>", lambda e: self.move_player(0, 1))
        self.root.bind("<Left>", lambda e: self.move_player(-1, 0))
        self.root.bind("<Right>", lambda e: self.move_player(1, 0))

        self.printMaze()

    def generateMaze(self):
        self.visit(self.markX, self.markY)
        self.printMaze()

    def printMaze(self):
        self.canvas.delete("all")
        for y in range(HEIGHT):
            for x in range(WIDTH):
                x1, y1 = x * 20, y * 20
                x2, y2 = (x + 1) * 20, (y + 1) * 20

                color = "black" if self.maze[(x, y)] == WALL else "white"

                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

        # Draw player
        x1, y1 = self.playerX * 20, self.playerY * 20
        x2, y2 = (self.playerX + 1) * 20, (self.playerY + 1) * 20
        self.canvas.create_rectangle(x1, y1, x2, y2, fill="red")

    def visit(self, x, y):
        self.maze[(x, y)] = EMPTY
        self.printMaze()
        self.root.update()
        self.root.after(10)

        directions = [NORTH, SOUTH, EAST, WEST]
        random.shuffle(directions)

        for direction in directions:
            dx, dy = 0, 0
            if direction == NORTH:
                dx, dy = 0, -2
            elif direction == SOUTH:
                dx, dy = 0, 2
            elif direction == WEST:
                dx, dy = -2, 0
            elif direction == EAST:
                dx, dy = 2, 0

            nx, ny = x + dx, y + dy
            if 0 < nx < WIDTH and 0 < ny < HEIGHT and (nx, ny) not in self.hasVisited:
                self.hasVisited.append((nx, ny))
                self.maze[(x + dx // 2, y + dy // 2)] = EMPTY
                self.visit(nx, ny)

    def move_player(self, dx, dy):
        newX = self.playerX + dx
        newY = self.playerY + dy
        if (0 <= newX < WIDTH and 0 <= newY < HEIGHT and self.maze[(newX, newY)] == EMPTY):
            self.playerX, self.playerY = newX, newY
            self.printMaze()
