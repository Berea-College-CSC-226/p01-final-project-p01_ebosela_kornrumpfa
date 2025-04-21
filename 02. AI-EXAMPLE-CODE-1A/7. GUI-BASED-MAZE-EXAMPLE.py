# Prompt For Generation:
"""
1. Goal: To create a simple maze (in Python), with an object that can be interacted with.
2. The Maze is generated using a loaded list that is stored in the variable MAZE_LAYOUTS.
3. Both the Maze and the Player Object are nested within classes; called MazeGame and Player respectively.
4. The Player Object once created is able to be moved by a method within MazeGame
5. The object of the game is to move the player within a set time frame to objects in the game space.
"""

import tkinter as tk
import time
import random

TILE_SIZE = 40 # As part of the class definition draw_maze() TILE_SIZE must be defined. In that case, using capitals indicates something of a SQL or static keyword.
TIME_LIMIT = 30  # Time limit in seconds (e.g., 60 seconds)

# 🔁 Multiple, bigger maze layouts
MAZE_LAYOUTS = [
    [
        [' ', 'W', ' ', ' ', 'W', ' ', ' ', ' ', 'W', ' ', ' ', 'W', ' ', 'G'],
        [' ', 'W', ' ', 'W', 'W', ' ', 'W', ' ', 'W', ' ', 'W', ' ', 'W', ' '],
        [' ', ' ', ' ', 'W', ' ', ' ', 'W', ' ', ' ', ' ', 'W', ' ', 'W', ' '],
        ['W', 'W', ' ', 'W', ' ', 'W', 'W', 'W', 'W', ' ', ' ', ' ', 'W', ' '],
        [' ', ' ', ' ', ' ', ' ', 'W', ' ', ' ', ' ', 'W', 'W', ' ', ' ', ' '],
        [' ', 'W', 'W', 'W', ' ', 'W', ' ', 'W', 'W', ' ', ' ', ' ', 'W', ' '],
        [' ', 'W', ' ', ' ', ' ', ' ', ' ', 'W', 'I', ' ', 'W', ' ', 'W', ' '],
        [' ', 'W', ' ', 'W', 'W', 'W', ' ', 'W', 'W', ' ', 'W', ' ', 'W', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', ' '],
    ],
    [
        [' ', ' ', ' ', 'W', ' ', ' ', ' ', 'W', ' ', ' ', 'G'],
        ['W', 'W', ' ', 'W', ' ', 'W', ' ', 'W', 'W', ' ', 'W'],
        [' ', ' ', ' ', ' ', ' ', 'W', ' ', ' ', ' ', ' ', ' '],
        [' ', 'W', 'W', 'W', ' ', 'W', 'W', 'W', 'W', 'W', ' '],
        [' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', 'I', 'W', ' '],
        [' ', 'W', ' ', 'W', 'W', 'W', 'W', ' ', ' ', 'W', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ],
    [
        [' ', ' ', 'W', ' ', 'G'],
        ['W', ' ', 'W', ' ', 'W'],
        ['W', ' ', ' ', ' ', 'W'],
        ['W', 'W', 'W', 'I', ' '],
        [' ', ' ', ' ', ' ', ' ']
    ],

    [
        ['', '', 'W', 'W', 'W'],
        ['W', ' ', 'W', 'W', 'W'],
        ['W', ' ', ' ', '', 'I'],
        ['W', 'W', 'W', 'W', ' '],
        [' ', ' ', ' ', 'G', ' ']
    ]
]

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.has_item = False
        self.reached_goal = False

    def move(self, dx, dy, maze):
        new_x = self.x + dx
        new_y = self.y + dy

        if 0 <= new_y < len(maze) and 0 <= new_x < len(maze[0]):
            tile = maze[new_y][new_x]
            if tile != 'W':
                self.x = new_x
                self.y = new_y

                if tile == 'I' and not self.has_item:
                    self.has_item = True
                    print("🎉 You picked up the item!")

                if tile == 'G':
                    if self.has_item:
                        self.reached_goal = True
                        print("🏁 You reached the goal and won the game!")
                    else:
                        print("⚠️ You need to pick up the item before reaching the goal.")


class MazeGame:
    def __init__(self, root):
        self.root = root

        # 🔀 Choose a random maze
        self.maze = random.choice(MAZE_LAYOUTS) #This line is used to randomly make a choice of the MAZE_LAYOUT to use.
        self.rows = len(self.maze)
        self.cols = len(self.maze[0])

        self.canvas = tk.Canvas(root, width=TILE_SIZE * self.cols, height=TILE_SIZE * self.rows)
        self.canvas.pack()

        self.timer_label = tk.Label(root, text=f"Time: {TIME_LIMIT}", font=("Arial", 14))
        self.timer_label.pack()

        self.time_left = TIME_LIMIT  # Set the initial time limit

        # 🧍‍♂️ Create maze and player before drawing
        self.player = Player(0, 0)

        self.root.bind("<KeyPress>", self.handle_key)
        self.draw_maze()
        self.update_timer()

""" The following class utilizes a for loop.
    I have seen other instance of for loops that rely on a dictionary, but this seems to be
    as an input variable. i.e. for eachKey in myDict, followed by an if statement.
    
    In this case 'y' is the iterator and the range function is being used with the input parameter 
    self.row.
    
    I don't understand the way this works. Why self.row? Why not just an reference to a create dictionary 
    or list? 
    
    To restate, all methods defined in a class that operate on objects of that class 
    must use self at their first parameter. 
    OK, so self is the first parameter for the method draw_maze, but why does it continue into
    the method in:
        self.canvas.delete("all")
        self.rows
        self.cols
        
    
    """

def draw_maze(self):
    self.canvas.delete("all")
    for y in range(self.rows):
        for x in range(self.cols):
                tile = self.maze[y][x]
                x1 = x * TILE_SIZE
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

    def handle_key(self, event):
        if not self.player.reached_goal and self.time_left > 0:
            dx, dy = 0, 0
            key = event.keysym

            if key == "Up":
                dy = -1
            elif key == "Down":
                dy = 1
            elif key == "Left":
                dx = -1
            elif key == "Right":
                dx = 1

            self.player.move(dx, dy, self.maze)
            self.draw_maze()

            if self.player.reached_goal:
                elapsed = TIME_LIMIT - self.time_left
                self.timer_label.config(text=f"🎉 You won in {elapsed} seconds!")

    def update_timer(self):
        if self.time_left > 0 and not self.player.reached_goal:
            self.time_left -= 1
            self.timer_label.config(text=f"Time: {self.time_left}")
            self.root.after(1000, self.update_timer)
        elif self.time_left == 0 and not self.player.reached_goal:
            self.timer_label.config(text="Game Over! Time's up!")
            print("⏳ Time's up! You lost the game.")


# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Maze Game with Timer and Lose Condition")
    game = MazeGame(root)
    root.mainloop()
