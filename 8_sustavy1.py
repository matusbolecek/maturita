# na maturitu staci 2 - 16

import string

def konvertuj(cislo: int, sustava: int) -> str:
    hodnoty = list(range(0, 10)) + list(string.ascii_uppercase)
    vysledky = []
    vysledok = cislo
    
    while vysledok != 0:
        zvysok = vysledok % sustava
        vysledok = vysledok // sustava
        hodnota = hodnoty[zvysok]

        vysledky.append(str(hodnota))
    
    output = str()
    for i in reversed(vysledky):
        output += i

    return output

if __name__ == "__main__":
    vstup = int(input('Zadaj cislo: '))
    sustava = int(input('Zadaj sustavu (1 - 36): '))
    vystup = konvertuj(vstup, sustava)
    print(f'Cislo {vstup} v {sustava}-kovej sustave je {vystup}')