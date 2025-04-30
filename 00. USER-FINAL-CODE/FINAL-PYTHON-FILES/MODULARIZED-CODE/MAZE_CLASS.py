import tkinter as tk
import random
from PLAYER_CLASS import Player

TILE_SIZE = 40
TIME_LIMIT = 0  # Time limit in seconds (e.g., 60 seconds)

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


class MazeGame:
    def __init__(self, window,time_limit):
        # The init method takes the new object as the first argument (game as self),
        # and then set any required instance attributes to a valid state,
        # using any other arguments passed to it (root)
        ####################
        print("Create Initializing Maze Game")
        self.window = window #Object attribute of some sort, that is used when the object is created.
        self.maze = random.choice(MAZE_LAYOUTS) # From the random module, a function called .choice() is selecting 1/3 of the maze layouts. # 🔀 Choose a random maze from the number of mazes defined above.
        print(f"{self.maze}")
        self.rows = len(self.maze)  #The length of the first layer of the nested list determines the number of rows
        print(f"{self.rows}")
        self.cols = len(self.maze[0]) #Once the first nested list is selected, the first element of that list is selected and evaluated to determine the columns.
        print(f"{self.cols}")
        self.time_left = time_limit  # Set the initial time limit
        print(f"{self.time_left}")
#### Calls to user defined classes #
        self.setup_GUI()
        self.setup_game_board()
        self.bind_controls()
        self.start_game_loop()
#### The init method relies on calls to other methods defined in the class, this makes the code more readable
#### more modular, and highlights functional cohesion.

    def setup_GUI(self):
        self.canvas = tk.Canvas(self.window, width=TILE_SIZE * self.cols, height=TILE_SIZE * self.rows) # The use of .Canvas is what allows the window to be filled with the player area items: tiles, player ball, and objectives.
        print(f"{self.canvas}")
        self.canvas.pack() # Used to organize and arrange the widgets.
        print(f"{self.canvas}")
        self.timer_label = tk.Label(self.window, text=f"Time: {TIME_LIMIT}", font=("Arial", 14))
        print(f"{self.timer_label}")
        self.timer_label.pack() #Used to organize and arrange the widgets canvass and label.
        print(f"{self.timer_label.pack}")

    def setup_game_board(self):
        # 🧍‍♂️ Create maze and player before drawing
        self.player = Player(0, 0)
        print(f"{self.player}")
        self.draw_maze()
        print(f"{self.draw_maze}")

# The bind_controls method is heavily coupled with the handle_key method.
# It works to ensure that when any key is pressed, tkinter will call the handle_key method
# loaded with event. The event object is created event.keysym
    def bind_controls(self):

        self.window.bind("<KeyPress>", self.handle_key) # An analogy for this statement: "Hey window! If someone presses a key, don't manage that, call my assistant, and give the details.
        # This statement self.window.bind("", self.handle_key) is used to route key presses to player movement.
        # The .bind() method comes from the __init__ working in combination with ensures that every time a key is pressed, a call to self.handle_key will be made and key information will be passed to it.
        # In reference to the __init__ this method will bind to this widget at event SEQUENCE a call to function FUNC.
        # .bind(<SEQUENCE>, <FUNCTION>)
        # The tkinter event loop established by main?
        # This statement use the .bind() method from tkinter to link key presses to the handle_key() method.
        # When the user presses any key while the window is in focus, tkinter automatically calls self.handle_key(event).
        #  This enables the player to move using the arrow keys.
        print(f"{self.window.bind}")

    def start_game_loop(self):

        self.update_timer()
        print(f"{self.update_timer}")



    def draw_maze(self):
        print("Drawing Maze")
        self.canvas.delete("all")
        print(f"{self.canvas.delete}")
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

        # Why isn't the block that is responsible for drawing the player not nested within a method?
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
    def handle_key(self, event): ## A primary method needed for the MazeGame class.
        print("Handling Key Presses")
        if not self.player._reached_goal and self.time_left > 0: #Boolean AND evaluation to determine if the statements will run.
            key_map={"Up":(0,-1),"Down":(0,1),"Left":(-1,0),"Right":(1,0)} #Restructured to use a dictionary.
            direction = key_map.get(event.keysym) # Binding. Tkinter provides a predefined set of event.keysms values ["Up", "Down", "Left","Right"] for each arrow key on a keyboard.
            if direction:
                [dx, dy] = direction
                self.player.move(dx,dy,self.maze)
                self.draw_maze()
            #print(f"{self.player.move}")
            #self.draw_maze()
            #print(f"{self.draw_maze}")
###### END OF SUBTASK IV ######################
###### START OF SUBTASK III ###################
            if self.player._reached_goal:
                elapsed = TIME_LIMIT - self.time_left
                self.timer_label.config(text=f"🎉 You won in {elapsed} seconds!")
###### END OF SUBTASK III #########################

#The following codeblock operates towards the end of subtask II.

    def update_timer(self):
        print("Updating Timer")
        if self.time_left > 0 and not self.player._reached_goal:
            self.time_left -= 1
            self.timer_label.config(text=f"Time: {self.time_left}")
            self.window.after(1000, self.update_timer)
        elif self.time_left == 0 and not self.player._reached_goal:
            self.timer_label.config(text="Game Over! Time's up!")
            print("⏳ Time's up! You lost the game.")
