#from MAZE-CLASS import MazeGame
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
