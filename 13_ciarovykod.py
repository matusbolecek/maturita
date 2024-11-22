# Na maturitu staci mat 8 miestny bez moznosti vyberu od pouzivatela

import random
import tkinter

def read() -> int:
    pocet = int(input('Zadaj pocet cislic ciaroveho kodu (2 - 12): '))

    while pocet not in range(2, 13):
        print('Vstup nie je v rozmedzi (2 - 12)!')
        pocet = int(input('Zadaj pocet cislic ciaroveho kodu (2 - 12): '))

    return pocet

def cisla(pocet) -> list:
    vysledok = []
    
    # prve cislo nema byt nula
    vysledok.append(str(random.randint(1, 9)))
    for i in range(pocet - 1):
        vysledok.append(str(random.randint(0, 9)))

    return vysledok

def ciarovy(cisla, scale = 1):
    pocet = len(cisla)
    canvas = tkinter.Canvas(height = 400, width = 400, bg = 'tan')
    canvas.pack()
    
    for i in range(pocet):
        canvas.create_line(20*i + 100, 100, 100 + 20*i, 250, width = 2 * int(cisla[i]), fill = 'black')
        canvas.create_text(20 * i + 100, 280, text = cisla[i], fill = "black")

    tkinter.mainloop()

if __name__ == "__main__":
    cisla = cisla(read())
    ciarovy(cisla)