import tkinter as tk
import time
import random

############## START OF SUBTASK I ################
TILE_SIZE = 40
TIME_LIMIT = 30  # Time limit in seconds (e.g., 60 seconds)

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
    ]
]

class MazeGame:
    def __init__(self, root):
        ####################
        self.root = root #Object attribute of some sort, that is used when the object is created.

        # 🔀 Choose a random maze from the number of mazes defined above.
        self.maze = random.choice(MAZE_LAYOUTS) # From the random module, a function called .choice() is selecting 1/3 of the maze layouts.
        self.rows = len(self.maze)  #The length of the first layer of the nested list determines the number of rows
        self.cols = len(self.maze[0]) #Once the first nested list is selected, the first element of that list is selected and evaluated to determine the columns.

        self.canvas = tk.Canvas(root, width=TILE_SIZE * self.cols, height=TILE_SIZE * self.rows) # The use of .Canvas is what allows the window to be filled with the player area items: tiles, player ball, and objectives.
        self.canvas.pack() # Used to organize and arrange the widgets.

        self.timer_label = tk.Label(root, text=f"Time: {TIME_LIMIT}", font=("Arial", 14))
        self.timer_label.pack() #Used to organize and arrange the widgets canvass and label.

        self.time_left = TIME_LIMIT  # Set the initial time limit

        # 🧍‍♂️ Create maze and player before drawing
        self.player = Player(0, 0)
        self.root.bind("<KeyPress>", self.handle_key)
        self.draw_maze()
        self.update_timer()
        ###################

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

        # Why isn't the block that is responsible for drawing the player not nested within a method?
        [px, py] = [self.player.x, self.player.y]
        self.canvas.create_oval(
            px * TILE_SIZE + TILE_SIZE // 4,
            py * TILE_SIZE + TILE_SIZE // 4,
            px * TILE_SIZE + 3 * TILE_SIZE // 4,
            py * TILE_SIZE + 3 * TILE_SIZE // 4,
            fill="blue"
        )
### START OF SUBTASK IV ########
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
###### END OF SUBTASK IV ######################
###### START OF SUBTASK III ###################
            if self.player.reached_goal:
                elapsed = TIME_LIMIT - self.time_left
                self.timer_label.config(text=f"🎉 You won in {elapsed} seconds!")
###### END OF SUBTASK III #########################

#The following codeblock operates towards the end of subtask II.

    def update_timer(self):
        if self.time_left > 0 and not self.player.reached_goal:
            self.time_left -= 1
            self.timer_label.config(text=f"Time: {self.time_left}")
            self.root.after(1000, self.update_timer)
        elif self.time_left == 0 and not self.player.reached_goal:
            self.timer_label.config(text="Game Over! Time's up!")
            print("⏳ Time's up! You lost the game.")

######################### END OF SUBTASK I ##################

######################### START OF SUBTASK II ###############
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





# Run the game - modified initial code name variable from root to windows for clarification of its usage.

if __name__ == "__main__":
    window = tk.Tk() # Create a window, similar to turtle.Screen() to create a graphical object.
    window.title("Random Maze") #Modifying the class attribute 'title' of the window object.
    game = MazeGame(window) # Game is the object that is created by MazeGame, that is passed the window object that is created by .Tk(). This line demonstrates the use of a class as a blueprint.
    window.mainloop() # What is .mainloop() referencing? | This is an event handler within the tkinter library. Which keep the program closing, and waits for input.

