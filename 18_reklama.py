# text, ktory bude scrollovat

import tkinter

def animacia():
    global nazov
    nazov = nazov[1:] + nazov[0]
    canvas.delete('all')
    canvas.create_text(300, 50, text = nazov, fill = 'red', font = ('courier New', 35, 'bold'))
    canvas.after(100, animacia)

nazov = input('Zadaj text: ')
nazov += (20 - len(nazov)) * " "
nazov += '  ' # ak je text dlhy, tak nech sa prida medzera

h = 200
w = 600
canvas = tkinter.Canvas(height = h, width = w, bg = 'black')
canvas.pack()

animacia()
canvas.mainloop()