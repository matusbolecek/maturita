# narpogramuj hru had. Hlavicka je jeden bod, poybuje sa urcenym smerom a ovlada sa klavesov
# Uvodna orientacia je na sever
# Koniec hry je ked narazi do steny - vypise slovo

import tkinter

h = 400
w = h
canvas = tkinter.Canvas(height = h, width = w, bg = 'white')
canvas.pack()

def klaves(event):
    global sx, sy
    if event.keysym == 'Left':
        sx, sy = -1, 0
    
    if event.keysym == 'Right':
        sx, sy = 1, 0

    if event.keysym == 'Up':
        sx, sy = 0, -1

    if event.keysym == 'Down':
        sx, sy = 0, 1

x, y = 200, 200
n = True
sx, sy = 0, -1

canvas.bind_all('<Key>', klaves)

while n:
    x += sx
    y += sy
    
    if y >= h or y <= 0 or x >= w or x <=0:
        n = False
        canvas.create_text(200, 200, fill='black', text='koniec', font=('arial 25'))
        canvas.mainloop()
    else:
        canvas.create_line(x, y, x + sx, y + sy, fill = 'black', width = 5)
        canvas.after(1)
        canvas.update()