# vlastny postup

import string

def konvertuj(cislo: str, sustava: int) -> str:
    hodnoty = []
    for i in range (0, 10):
        hodnoty.append(str(i))
    hodnoty += list(string.ascii_uppercase)
    vstup = reversed(list(cislo))

    mnozina = 0
    vysledok = 0
    for i in vstup:
        hodnota = hodnoty.index(i)
        vysledok += hodnota * (sustava ** mnozina)
        mnozina += 1

    return vysledok

if __name__ == "__main__":
    vstup = str(input('Zadaj cislo: '))
    sustava = int(input('Zadaj sustavu (1 - 36): '))
    vystup = konvertuj(vstup, sustava)
    print(f'Cislo {vstup} v {sustava}-kovej sustave je {vystup} v 10-kovej sustave')