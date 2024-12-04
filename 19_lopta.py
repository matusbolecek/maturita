# lopta, ktora sa odraza od stien

import tkinter
import random

h = 600
w = 800
canvas = tkinter.Canvas(height = h, width = w, bg = 'white')
canvas.pack()

def klaves(a):
    global k
    k = False

x = 400
y = 300
dx = 5
dy = 3
f = 0 # na farby

while True:
    posun = 25
    farby = ['blue', 'cyan', 'green', 'yellow', 'orange', 'red', 'pink', 'purple'] # toto netreba na maturite, staci 1 farba

    canvas.create_oval(x - posun, y - posun, x + posun, y + posun, fill = farby[f % 8], outline = 'grey')
    if y >= 575 or y <= 25:
        dy = -dy
        f += 1

    if x >= 775 or x <= 25:
        dx = -dx
        f += 1

    x += dx
    y += dy
    canvas.after(1)
    canvas.update()
    canvas.delete('all') # mazanie stopy
    canvas.bind_all('<Key>', klaves)