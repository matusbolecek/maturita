# maturitny
# na vstupe je postupnost znamok, zadavanie ukoncite 0
# vypocitajte priemer
# ak priemer <= 1.5 prospel s vyznamenanim, <= ako 2 PVD, inac prospel
# znamky 1 - 5, ine nie

def priemeruj() -> float:
    znamky = []
    while True:
        vstup = int((input(f'Vlož {len(znamky) + 1}. známku ')))
        if vstup == 0:
            break
        elif vstup in range(1,6):
            znamky.append(vstup)
        else:
            print(f'Zadany vstup "{vstup}" nie je vhodny!')

    priemer = sum(znamky) / len(znamky)
    return priemer

def vysledok(priemer) -> str:
    if priemer <= 1.5:
        return 'prospel s vyznamenanim'
    elif priemer <= 2:
        return 'prospel velmi dobre'
    else:
        return 'prospel'

if __name__ == "__main__":
    priemer = priemeruj()
    vysledok = vysledok(priemer)
    print(f'Ziak mal priemer {priemer} a', vysledok)