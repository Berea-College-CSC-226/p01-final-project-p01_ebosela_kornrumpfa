"""
My teams final code base shows improved mastery of object-oriented programming through hand-on software development.
The goal is to present a maze game that demonstrates increased proficiency in all major OOP concepts:
The key task are:
Write a class definition with a constructor. #__init__() methods (e.g., in MazeGame, Player)
Add and access class and or instance attributes. #There are no class attributes in this program, only instance attributes.
Write getter and setter methods #
Make instance attributes private # Successfully did so with the use of classes.
Create a parent and child class # N/A
Override a method in the child class # N/A
Create an abstract class and implement it.
Instantiate objects and use them in main logic. # game = MazeGame(window) and self.player = Player(...)
Handle object lifecycle (destruction or cleanup).

"""
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

"""
Object oriented programming relies on the creation of classes with the capacity to create objects 
that contain both data and functionality together. In other words, the object that will be 
created is associated with something in the real world, and its functions are associated to 
the way real-world object interact. 

Prime Example: object.function()>  microwave.cook(). 

Classes, a class can be thought of as a blueprint that generically describes something: objects. 
Classes describe the attributes (i.e., properties) and methods (i.e., behaviors) that each object 
can have. Put another way, an object is an instance of a class. 
A class is a blueprint that describes an object by its attribute-properties, 
and methods of behaving.  Yet another way to state this, that a class describes 
the attributes and methods that each object can have. 
Sometimes it necessary to create ones own classes to solve a problem, as built in classes like 
[str, int, float, and Turtle]  may not be effective.

Objects, In object-oriented programming (OOP), objects are the basic entities that 
exists in the memory. Each object is based on a blueprint of attributes 
and behaviors (variables and functions) defined as Class. 
When the program doesn’t know about the external world, it can’t do anything. 
For example, when programming a robot to make a peanut butter sandwich, 
the objects: bag, jar, knife, etc. are objects. 
In python, everything is an object broadly. 
An object is a bit of information stored in memory. Memory is manipulated. 
"""
class MazeGame:
    def __init__(self, root): #The init method takes the new object as the first argument (game as self), and then set any required instance attributes to a valid state, using any other arguments passed to it (root)
        ####################
        print("Create Initializing Maze Game")

        self.root = root #Object attribute of some sort, that is used when the object is created.
#
        # 🔀 Choose a random maze from the number of mazes defined above.
        self.maze = random.choice(MAZE_LAYOUTS) # From the random module, a function called .choice() is selecting 1/3 of the maze layouts.
        print(f"{self.maze}")
        self.rows = len(self.maze)  #The length of the first layer of the nested list determines the number of rows
        print(f"{self.rows}")
        self.cols = len(self.maze[0]) #Once the first nested list is selected, the first element of that list is selected and evaluated to determine the columns.
        print(f"{self.cols}")
        self.canvas = tk.Canvas(root, width=TILE_SIZE * self.cols, height=TILE_SIZE * self.rows) # The use of .Canvas is what allows the window to be filled with the player area items: tiles, player ball, and objectives.
        print(f"{self.canvas}")
        self.canvas.pack() # Used to organize and arrange the widgets.
        print(f"{self.canvas}")
        self.timer_label = tk.Label(root, text=f"Time: {TIME_LIMIT}", font=("Arial", 14))
        print(f"{self.timer_label}")
        self.timer_label.pack() #Used to organize and arrange the widgets canvass and label.
        print(f"{self.timer_label.pack}")
        self.time_left = TIME_LIMIT  # Set the initial time limit
        print(f"{self.time_left}")
        # 🧍‍♂️ Create maze and player before drawing
        self.player = Player(0, 0)
        print(f"{self.player}")
        self.root.bind("<KeyPress>", self.handle_key)
        print(f"{self.root.bind}")
        self.draw_maze()
        print(f"{self.draw_maze}")
        self.update_timer()
        print(f"{self.update_timer}")
        ###################

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
    def handle_key(self, event):
        print("Handling Key Presses")
        if not self.player._reached_goal and self.time_left > 0:
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
            print(f"{self.player.move}")
            self.draw_maze()
            print(f"{self.draw_maze}")
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
            self.root.after(1000, self.update_timer)
        elif self.time_left == 0 and not self.player._reached_goal:
            self.timer_label.config(text="Game Over! Time's up!")
            print("⏳ Time's up! You lost the game.")

######################### END OF SUBTASK I ##################

######################### START OF SUBTASK II ###############
class Player:

    def __init__(self, x, y):
        print("Initializing Player")
        self._x = x # Player's x position (private attribute)
        print(f"{self._x}")
        self._y = y # Player's y position (private attribute)
        print(f"{self._y}")
        self._has_item = False # # Whether the player has picked up the item (private attribute)
        print(f"{self._has_item}")
        self._reached_goal = False
        print(f"{self._reached_goal}") ## Whether the player has reached the goal (private attribute)

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_y(self, y):
        self._y = y

    def get_has_item(self):
        return self._has_item

    def get_reached_goal(self):
        return self._reached_goal

    def set_reached_goal(self, reached_goal):
        self._reached_goal = reached_goal

    def move(self, dx, dy, maze):
        print("Moving Player")
        new_x = self._x + dx
        new_y = self._y + dy

        if 0 <= new_y < len(maze) and 0 <= new_x < len(maze[0]):
            tile = maze[new_y][new_x]
            if tile != 'W':
                self._x = new_x
                self._y = new_y

                if tile == 'I' and not self._has_item:
                    self._has_item = True
                    print("🎉 You picked up the item!")

                if tile == 'G':
                    if self._has_item:
                        self._reached_goal = True
                        print("🏁 You reached the goal and won the game!")
                    else:
                        print("⚠️ You need to pick up the item before reaching the goal.")





# Run the game - modified initial code name variable from root to windows for clarification of its usage.

if __name__ == "__main__":
    window = tk.Tk() # Create a window, similar to turtle.Screen() to create a graphical object.
    window.title("Random Maze") #Modifying the class attribute 'title' of the window object.
    game = MazeGame(window) # Game is the object that is created by MazeGame, that is passed the window object that is created by .Tk(). This line demonstrates the use of a class as a blueprint. This object is then loaded with "the nested items are all attributes/properties/functions of the class.
    window.mainloop() # What is .mainloop() referencing? | This is an event handler within the tkinter library. Which keep the program closing, and waits for input.

