# zadaj pocet hodov, napis, kolko krat padlo ktore

import random

def hadz(pocet:int) -> list:
    hody = []
    for i in range(pocet):
        hod = random.randint(1, 7)
        hody.append(hod)

    return hody

def vycisli(zoznam:list):
    vystup = str()
    for i in range(1, 7):
        pocet = zoznam.count(i)
        vystup += f'Cislo {i} bolo hodene {pocet}x \n'

    return vystup

if __name__ == "__main__":
    pocet = int(input('Zadaj pocet hodov: '))
    hody = hadz(pocet)
    vysledne = vycisli(hody)
    print(vysledne)