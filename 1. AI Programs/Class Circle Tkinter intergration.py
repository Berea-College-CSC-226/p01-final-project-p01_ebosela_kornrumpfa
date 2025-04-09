import tkinter as tk

class MyCircle:
    def __init__(self, canvas, x, y, radius, color):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.circle = self.canvas.create_oval(
            x - radius, y - radius, x + radius, y + radius,
            fill=color, outline=color
        )

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.canvas.move(self.circle, dx, dy)

class App:
    def __init__(self, master):
        self.master = master
        master.title("Object Example")

        self.canvas = tk.Canvas(master, width=400, height=300, bg="white")
        self.canvas.pack()

        self.circle1 = MyCircle(self.canvas, 100, 150, 50, "blue")
        self.circle2 = MyCircle(self.canvas, 300, 150, 30, "red")

        self.move_button = tk.Button(
            master, text="Move Circles", command=self.move_circles
        )
        self.move_button.pack()

    def move_circles(self):
        self.circle1.move(10, 0)
        self.circle2.move(-5, 5)

root = tk.Tk()
app = App(root)
root.mainloop()