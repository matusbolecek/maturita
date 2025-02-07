# vytvorte program, ktory analyzuje vstupny text a spravi analyzu nasledovne:
# vypise pocet jednotlivych znakov anglickej abecedy (nerozlisuje male, velke pismena)
# ako by ste program rozsirili o zistenie najcastejsieho pismena

import string

def main(vstup) -> list:
    pismena = list(vstup.upper())
    abeceda = list(string.ascii_uppercase)
    vystup = []

    for x in abeceda:
        pocet = pismena.count(x)
        if pocet > 0:
            vystup.append([x, pocet])

    return vystup

def vypis(zoznam) -> str:
    for a in zoznam:
        print(f'Pismeno {a[0]} bolo v texte {a[1]} krat.')

if __name__ == "__main__":
    vstup = input('Zadaj text: ')
    vystup = main(vstup)
    vypis(vystup)