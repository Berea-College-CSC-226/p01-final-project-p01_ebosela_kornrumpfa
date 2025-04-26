import tkinter as tk
from maze_class import MazeGame

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Random Maze Game")
    game = MazeGame(root)
    root.mainloop()
