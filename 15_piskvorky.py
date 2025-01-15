# naprogramuj piskvorky
# na maturite sa na jedneho a druheho hraca pouzivaju dve tlacidla mysi, no tento sposob vyuziva premennu a jedno tlacidlo
# doplnena verzia, kde prave tlacidlo "maze". Tiez nie je na maturite.

import tkinter
cislo = 1 # striedanie jedneho a druheho hraca

def tah(sur):
    global cislo
    okno = int(canvas.winfo_reqheight() / 15)
    offset = okno / 7
    x = sur.x // okno * okno
    y = sur.y // okno * okno

    if cislo % 2 != 0:
        canvas.create_line(x + offset, y + offset, x + okno - offset, y + okno - offset, width = offset, fill = 'blue')
        canvas.create_line(x + offset, y + okno - offset, x + okno - offset, y + offset, width = offset, fill = 'blue')
    else:
        canvas.create_oval(x + offset, y + offset, x + okno - offset, y + okno - offset, width = offset, fill = 'white', outline = 'red')
    
    cislo += 1

def vymaz(sur): # toto nie je na maturite
    global cislo
    okno = int(canvas.winfo_reqheight() / 15)
    offset = okno / 7
    x = sur.x // okno * okno # + (okno / 2)
    y = sur.y // okno * okno # + (okno / 2)

    for i in range(6): # najprimitivnejsie riesenie toho, aby sa odstranili zvysky
        canvas.create_line(x + offset, y + offset, x + okno - offset, y + okno - offset, width = offset, fill = 'white')
        canvas.create_line(x + offset, y + okno - offset, x + okno - offset, y + offset, width = offset, fill = 'white')
        canvas.create_oval(x + offset, y + offset, x + okno - offset, y + okno - offset, width = offset, fill = 'white', outline = 'white')
    
    cislo -= 1  # tu moze byt problem, keby niekto vymaze prazdne policko. 
                # Riesenim by bola nejaka tabulka, ktora by sa checkla, ci tam nieco je.

rozmer = 900
canvas = tkinter.Canvas(height = rozmer, width = rozmer, bg = 'white')
canvas.pack()
krok = 1

# vertikalne
for i in range(15):
    posun =  i * (rozmer / 15)
    canvas.create_line(0 + posun, 0, 0 + posun, rozmer, fill = "black", width = "2")

# horizontalne
for i in range(15):
    posun =  i * (rozmer / 15)
    canvas.create_line(0, 0 + posun, rozmer, 0 + posun, fill = "black", width = "2")

canvas.bind("<Button-1>", tah)
canvas.bind("<Button-2>", vymaz)
canvas.mainloop()