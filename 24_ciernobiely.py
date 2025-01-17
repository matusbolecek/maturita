# zadany je subor (doplnky/ciernobiely.text), ktory treba precitat a podla pixelov vykreslit obrazok

import tkinter

subor = open('doplnky/24_ciernobiely.text', 'r')
r = subor.readline()
w, h = r.split()
w, h = int(w), int(h)

canvas = tkinter.Canvas(height = h, width = w, bg = 'white')
canvas.pack()

y = 0

for r in subor:
    for i in range(w):
        odtien = r[i*2 : i*2 + 2]
        farba = f'#{3 * odtien}'
        canvas.create_line(i, y, i + 1, y, fill = farba)

    y += 1

subor.close()
canvas.mainloop()
