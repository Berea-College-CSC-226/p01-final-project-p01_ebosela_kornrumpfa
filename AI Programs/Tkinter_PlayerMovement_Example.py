import tkinter as tk

# Set up window
window = tk.Tk()
window.title("Tkinter Player Movement")
canvas = tk.Canvas(window, width=600, height=600, bg="black")
canvas.pack()

# Create player (a white square)
player = canvas.create_rectangle(290, 290, 310, 310, fill="white")

# Movement function
def move_player(event):
    if event.keysym == "Up":
        canvas.move(player, 0, -20)
    elif event.keysym == "Down":
        canvas.move(player, 0, 20)
    elif event.keysym == "Left":
        canvas.move(player, -20, 0)
    elif event.keysym == "Right":
        canvas.move(player, 20, 0)

# Bind keys
window.bind("<KeyPress>", move_player)

# Start game loop
window.mainloop()
