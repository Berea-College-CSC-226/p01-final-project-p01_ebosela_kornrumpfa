def main():
    program = RandomMazeGame()
    program.window.mainloop()


class RandomMazeGame:
    def __int__(self, window):
        self.window = window

        self.maze = random.choice(maze_layouts)
        self.rows = len(self.maze)
        self.columns = len(self.maze[0])

        self.board = tk.Canvas(window, width=tile_size * self.columns, height=tile_size * self.rows)
        self.board.pack()

        self.clock_label = tk.label(window, text=f'TIme: {Time_limit}', fontname=("Times New Roman", 17))
        self.clock_label.pack()

        self.time_remaining = Time_limit