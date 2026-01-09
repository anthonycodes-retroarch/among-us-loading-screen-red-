import tkinter as tk
import math
import time

WIDTH = 800
HEIGHT = 600
DURATION = 5  # seconds the screen stays

root = tk.Tk()
root.overrideredirect(True)
root.attributes("-fullscreen", True)
root.configure(bg="black")

canvas = tk.Canvas(root, bg="black", highlightthickness=0)
canvas.pack(fill="both", expand=True)

cx = root.winfo_screenwidth() // 2
cy = root.winfo_screenheight() // 2

# Loading text
text = canvas.create_text(
    cx, cy + 180,
    text="Loading...",
    fill="white",
    font=("Arial", 24, "bold")
)

# Crewmate body
body = canvas.create_oval(
    cx - 60, cy - 60,
    cx + 60, cy + 60,
    fill="#ff3b3b", outline=""
)

# Visor
visor = canvas.create_oval(
    cx - 20, cy - 25,
    cx + 50, cy + 10,
    fill="#9fdcff", outline=""
)

angle = 0
start_time = time.time()

def animate():
    global angle

    angle += 6
    r = 120

    x = cx + math.cos(math.radians(angle)) * r
    y = cy + math.sin(math.radians(angle)) * r

    canvas.coords(
        body,
        x - 60, y - 60,
        x + 60, y + 60
    )

    canvas.coords(
        visor,
        x - 20, y - 25,
        x + 50, y + 10
    )

    dots = int((time.time() * 2) % 4)
    canvas.itemconfig(text, text="Loading" + "." * dots)

    if time.time() - start_time < DURATION:
        root.after(16, animate)
    else:
        root.destroy()

animate()
root.mainloop()
