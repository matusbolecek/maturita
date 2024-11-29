# naprogramuj semafor

import tkinter

h = 500
w = 300
canvas = tkinter.Canvas(height = h, width = w, bg = 'white')
canvas.pack()

# a, b su odsadenia od strany
a = 70
b = 40
canvas.create_rectangle(a, b, w - a, h - b, fill = 'gray')

# pocitanie stredov kruhov a pevne stanoveny offset, aby to bolo v strede
stred1 = (h - b - b) / 6
stred2 = w / 2
c = 45
off = 30

def semafor(farby):
    for i in range(2, 8, 2):
        x = int(i / 2 - 1)
        canvas.create_oval(stred2 - c, i * stred1 - c - off, stred2 + c, i * stred1 + c - off, fill = farby[x])

def main(cas):
    vypnuty = ['black', 'black', 'black']
    moznosti = [['red', 'black', 'black'], ['black', 'orange', 'black'], ['black', 'black', 'green']]

    # vypnuty na 2 sekundy (nepovinne)
    semafor(vypnuty)
    canvas.update()
    canvas.after(cas)

    while True:
        for farby in moznosti:
            semafor(farby)
            canvas.update()
            canvas.after(cas)

        for farby in reversed(moznosti):
            semafor(farby)
            canvas.update()
            canvas.after(cas)

if __name__ == "__main__":
    main(1500)