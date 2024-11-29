# naprogramuj piskvorky
# alternativy postup je za pomoci textu (pozri. komenty)
# neviem, ci je nepresnost na pravej strane iba mac issue, alebo je niekde chyba v kode
# na maturite sa na jedneho a druheho hraca pouzivaju dve tlacidla mysi, no tento sposob vyuziva premennu a jedno tlacidlo

import tkinter
cislo = 1 # striedanie jedneho a druheho hraca

def tah(sur):
    global cislo
    okno = canvas.winfo_reqheight() / 15
    offset = okno / 7
    x = sur.x // okno * okno # + (okno / 2)
    y = sur.y // okno * okno # + (okno / 2)

    if cislo % 2 != 0:
        canvas.create_line(x + offset, y + offset, x + okno - offset, y + okno - offset, width = offset, fill = 'blue')
        canvas.create_line(x + offset, y + okno - offset, x + okno - offset, y + offset, width = offset, fill = 'blue')
        # canvas.create_text(x, y, text = "X", fill = "blue", font = ("Arial-Bold", 60))
    else:
        canvas.create_oval(x + offset, y + offset, x + okno - offset, y + okno - offset, width = offset, fill = 'white', outline = 'red')
        
        # canvas.create_text(x, y, text = "O", fill = "red", font = ("Arial-Bold", 60))
    
    cislo += 1

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
canvas.mainloop()