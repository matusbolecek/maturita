# vygenerovat 6 cisel (1-49), osetrit, aby neboli v zozname
# porovnaj a pocitaj, kolko si uhadol
# over, ci vstup neni blbost

from random import randint

def vygeneruj(zoznam: list, min: int, max:int) -> int:
    cislo = None
    while cislo in zoznam or cislo == None:
        cislo = randint(min, max)
    
    return cislo

def losuj(pocet = 6, min = 1, max = 49) -> list:
    los = []
    for i in range(pocet):
        cislo = vygeneruj(los, min, max)
        los.append(cislo)

    return los

def hrac(pocet = 6, min = 1, max = 49) -> list:
    hrac_zoznam = []
    for i in range(pocet):
        cislo = None
        
        while cislo in hrac_zoznam or cislo not in range(1, 49) or cislo == None:
            if cislo != None:
                print('Nespravny vstup! Skus znova')
            
            cislo = int(input(f'Zadaj tvoje {i + 1}. cislo ({min} - {max}) '))
        
        hrac_zoznam.append(cislo)

    return hrac_zoznam

def porovnaj(los: list, hrac: list) -> int | list:
    i = 0
    zhody = []
    for items in hrac:
        if items in los:
            i += 1
            zhody.append(items)

    return i, zhody

def main() -> str:
    losovane = sorted(losuj())
    hracove = sorted(hrac())
    i, zhody = porovnaj(losovane, hracove)

    if i == 0:
        fraza = 'Lutujeme,'
    else:
        fraza = 'Gratulujeme,'

    if i in range(2, 4):
        koniec = 'cisla'
    elif i == 1:
        koniec = 'cislo'
    else:
        koniec = 'cisel'

    print('Vyzrebovane cisla boli', losovane)
    print('Tvoje cisla boli', hracove)
    print(f'{fraza} trafil si {i} {koniec} - {zhody}')
    
if __name__ == "__main__":
    main()