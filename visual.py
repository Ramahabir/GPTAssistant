import tkinter as tk

class BouncingCircle:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=200, height=200, bg="black")
        self.canvas.pack()

        self.circle = self.canvas.create_oval(80, 90, 120, 130, fill="cyan")
        self.direction = 1

        self.animate()

    def animate(self):
        self.canvas.move(self.circle, 0, self.direction * 2)
        y1, y2 = self.canvas.coords(self.circle)[1], self.canvas.coords(self.circle)[3]

        if y2 >= 140 or y1 <= 60:
            self.direction *= -1

        self.canvas.after(20, self.animate)

root = tk.Tk()
root.title("voice indicator")
BouncingCircle(root)
root.mainloop()