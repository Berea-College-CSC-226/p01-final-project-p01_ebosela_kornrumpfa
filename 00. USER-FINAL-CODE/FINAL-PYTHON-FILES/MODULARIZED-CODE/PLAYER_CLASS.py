class Player:

    """
        Represents a player in a maze game.

        Attributes:
            _x (int): Player's x position (private attribute).
            _y (int): Player's y position (private attribute).
            _has_item (bool): Whether the player has picked up the item (private attribute).
            _reached_goal (bool): Whether the player has reached the goal (private attribute).
        """

    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._has_item = False
        self._reached_goal = False


    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_y(self, y):
        self._y = y

    def set_x(self, x):
        self._x = x

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
