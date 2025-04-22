
def main():
    program = RandomMazeGame()

    program.window.mainloop()

class RandomMazeGame:
    def __int__(self, window):
        self.window = window

        self.maze = random.choice(maze_layouts)
        self.rows = len(self.maze)
        self.columns = len(self.maze[0])