# na maturitu treba spravit slovensku vlajku

import tkinter

def vypocet(vyska):
    y1, x1 = 2, 3
    x = vyska * x1
    y = vyska * y1
    return x, y

def vlajka(x, y, farba1, farba2, farba3, znak=None, pozicia=None, skalovanie=None):
    canvas = tkinter.Canvas(width=x, height=y, bg=farba1)
    canvas.pack()

    tretina = y / 6
    width = tretina * 2

    canvas.create_line(0, tretina * 3, x, tretina * 3, width = width, fill=farba2)
    canvas.create_line(0, tretina * 5, x, tretina * 5, width = width, fill=farba3)
    
    if pozicia != None:
        if pozicia == "vlavo":
            sucinitel = 3
        elif pozicia == "vpravo":
            sucinitel = 7
        else:
            sucinitel = 5

    if znak != None:
        obrazok = tkinter.PhotoImage(file = znak)
        obrazok = obrazok.subsample(skalovanie, skalovanie)
        odsadenie = x / 10
        canvas.create_image(odsadenie * sucinitel, tretina * 3, image = obrazok)

    canvas.mainloop()

# Vlajky
def slovensko(x, y):
    vlajka(x, y, "white", "blue", "red", "doplnky/slovensko.png", "vlavo", 2)

def madarsko(x, y):
    vlajka(x, y, "red", "white", "green")

def rusko(x, y):
    vlajka(x, y, "white", "blue", "red")

if __name__ == "__main__":
    x, y = vypocet(300)
    slovensko(x, y)