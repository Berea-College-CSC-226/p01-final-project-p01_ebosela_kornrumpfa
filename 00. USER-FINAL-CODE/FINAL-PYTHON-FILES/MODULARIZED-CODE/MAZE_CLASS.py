import tkinter as tk
import random
from PLAYER_CLASS import Player

TILE_SIZE = 40
TIME_LIMIT = 0  # TimE limit in seconds (e.g., 60 seconds)

# 🔁 Multiple, bigger maze layouts, that are hard-coded, but randomly selected.
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
        [' ', ' ', 'W', ' ', ' ', ' ', 'W', 'W', ' ', ' ', ' ', ' ', 'W', 'I'],
        [' ', ' ', ' ', 'W', 'W', ' ', 'W', ' ', 'W', ' ', 'W', 'W', ' ', ' '],
        ['W', ' ', ' ', ' ', ' ', ' ', 'W', ' ', ' ', ' ', ' ', 'W', ' ', ' '],
        ['W', ' ', 'W', 'W', 'W', ' ', ' ', ' ', 'W', 'W', ' ', 'W', ' ', 'W'],
        [' ', ' ', ' ', ' ', 'W', ' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['W', 'W', 'W', ' ', 'W', ' ', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', ' ', ' '],
        [' ', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', ' ', ' ', ' ', 'W'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', ' ', ' '],
        ['G', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
    ],
    [
        [' ', ' ', ' ', 'W', ' ', ' ', 'W', 'W', ' ', ' ', ' ', 'W', ' ', 'I'],
        ['W', 'W', ' ', 'W', 'W', ' ', 'W', ' ', 'W', ' ', 'W', 'W', ' ', ' '],
        [' ', 'W', ' ', ' ', ' ', ' ', 'W', ' ', ' ', ' ', ' ', 'W', ' ', ' '],
        [' ', 'W', 'W', 'W', 'W', ' ', ' ', ' ', 'W', 'W', ' ', 'W', ' ', 'W'],
        [' ', ' ', ' ', ' ', 'W', ' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['W', 'W', 'W', ' ', 'W', ' ', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', ' ', ' '],
        [' ', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', ' ', ' ', ' ', 'W'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', ' ', ' '],
        ['G', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
    ],
    [
        ['G', ' ', ' ', 'W', ' ', ' ', ' ', ' ', 'W', ' ', 'W', ' ', ' ', ' '],
        ['W', 'W', ' ', 'W', 'W', 'W', 'W', ' ', 'W', ' ', 'W', 'W', 'W', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', ' '],
        ['W', ' ', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', ' ', 'W', 'W', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', ' ', ' ', ' ', ' '],
        ['W', 'W', 'W', 'W', ' ', 'W', 'W', 'W', ' ', 'W', 'W', 'W', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', 'W', 'W', 'W', 'W', 'W', ' ', 'W', 'W', 'W', 'W', 'W', 'W', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'I'],
        ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
    ],
    [
        [' ', ' ', ' ', 'W', ' ', ' ', ' ', ' ', ' ', 'W', ' ', ' ', ' ', 'I'],
        ['W', 'W', ' ', 'W', 'W', 'W', 'W', ' ', 'W', ' ', 'W', 'W', 'W', ' '],
        ['G', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', ' '],
        ['W', ' ', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', ' ', 'W', 'W', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', ' ', ' ', ' ', ' '],
        ['W', 'W', 'W', 'W', ' ', 'W', 'W', 'W', ' ', 'W', 'W', 'W', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', 'W', 'W', 'W', 'W', 'W', ' ', 'W', 'W', 'W', 'W', 'W', 'W', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
    ],
    [
        [' ', ' ', 'W', ' ', ' ', ' ', 'W', 'W', ' ', ' ', ' ', ' ', 'W', ' '],
        [' ', ' ', ' ', 'W', 'W', ' ', 'W', ' ', 'W', ' ', 'W', 'W', ' ', ' '],
        ['W', 'W', ' ', ' ', ' ', ' ', 'W', ' ', ' ', ' ', ' ', 'W', ' ', 'I'],
        ['W', 'W', 'W', 'W', 'W', ' ', ' ', ' ', 'W', 'W', ' ', 'W', ' ', 'W'],
        [' ', ' ', ' ', ' ', 'W', ' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['W', 'W', 'W', ' ', 'W', ' ', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', ' ', ' '],
        [' ', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', ' ', ' ', ' ', 'W'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', ' ', ' '],
        ['G', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
    ],
]

"""
Initializes the game window, loads a random maze layout, sets up gameplay state,
and binds player controls for movement via keypresses.

This method (typically __init__) performs the following tasks:
- Sets up the game object (`self`) with the necessary attributes and valid initial state.
- Selects a random maze layout from predefined options using `random.choice()`.
- Determines the maze's dimensions by measuring the length of its nested list structure.
- Sets the initial time limit for the game.
- Instantiates and calls other helper methods to promote modularity and readability.
- Arranges graphical components (e.g., canvas and labels) for visual layout using Tkinter's layout tools.

Keyboard Input Handling:
- Uses the `.bind()` method from the Tkinter library to link keyboard events to the `handle_key` method.
- The `bind_controls()` method ensures keypresses (e.g., arrow keys) are captured and routed to the movement handler.
- Example: `self.window.bind("<Key>", self.handle_key)` tells the program:  
  "Hey window! If someone presses a key, don’t process it yourself — call `handle_key` and pass the event details."

Event Binding Concept:
- The `.bind(<SEQUENCE>, <FUNCTION>)` format binds a specific key event (like arrow keys) to a callback function.
- The `handle_key(event)` method receives the key information via the `event` object (`event.keysym`).
- Enables real-time control of the player character based on user input.

Overall, this setup supports interactive gameplay using the keyboard, organized through clean object-oriented structure.
"""

class MazeGame:
    def __init__(self, window,time_limit):

        print("Create Initializing Maze Game")
        self.window = window
        self.maze = random.choice(MAZE_LAYOUTS)

        self.rows = len(self.maze)

        self.cols = len(self.maze[0])

        self.time_left = time_limit

        self.setup_GUI()
        self.setup_game_board()
        self.bind_controls()
        self.start_game_loop()


    def setup_GUI(self):
        self.canvas = tk.Canvas(self.window, width=TILE_SIZE * self.cols, height=TILE_SIZE * self.rows) # The use of .Canvas is what allows the window to be filled with the player area items: tiles, player ball, and objectives.

        self.canvas.pack()

        self.timer_label = tk.Label(self.window, text=f"Time: {TIME_LIMIT}", font=("Arial", 14))

        self.timer_label.pack()


    def setup_game_board(self):
        # 🧍‍♂️ Create maze and player before drawing
        self.player = Player(0, 0)

        self.draw_maze()



    def bind_controls(self):

        self.window.bind("<KeyPress>", self.handle_key)


    def start_game_loop(self):

        self.update_timer()




    def draw_maze(self):
        print("Drawing Maze")
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
                elif tile == 'I' and not self.player._has_item:
                    color = "gold"
                elif tile == 'G':
                    color = "green" if self.player._has_item else "gray"

                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color) #Statement is used to color the tiles within the maze

        [px, py] = [self.player._x, self.player._y]
        self.canvas.create_oval(

            px * TILE_SIZE + TILE_SIZE // 4,
            py * TILE_SIZE + TILE_SIZE // 4,
            px * TILE_SIZE + 3 * TILE_SIZE // 4,
            py * TILE_SIZE + 3 * TILE_SIZE // 4,
            fill="blue"
        )
        print(f"{self.canvas.create_oval}")

### START OF SUBTASK IV ########
    def handle_key(self, event):

        if not self.player._reached_goal and self.time_left > 0: #Boolean AND evaluation to determine if the statements will run.
            key_map={"Up":(0,-1),"Down":(0,1),"Left":(-1,0),"Right":(1,0)} #Restructured to use a dictionary.
            direction = key_map.get(event.keysym) # Binding. Tkinter provides a predefined set of event.keysms values ["Up", "Down", "Left","Right"] for each arrow key on a keyboard.
            if direction:
                [dx, dy] = direction
                self.player.move(dx,dy,self.maze)
                self.draw_maze()
            if self.player._reached_goal:
                elapsed = TIME_LIMIT - self.time_left
                self.timer_label.config(text=f"🎉 You won in {elapsed} seconds!")



    def update_timer(self):
        print("Updating Timer")
        if self.time_left > 0 and not self.player._reached_goal:
            self.time_left -= 1
            self.timer_label.config(text=f"Time: {self.time_left}")
            self.window.after(1000, self.update_timer)
        elif self.time_left == 0 and not self.player._reached_goal:
            self.timer_label.config(text="Game Over! Time's up!")
            print("⏳ Time's up! You lost the game.")
