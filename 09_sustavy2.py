# prevod cisla z lubovolnej sustavy do desiatkovej
# vlastny postup; normalne by sa to malo riesit cez chr() a ord()
# treba doplnit aj, ze si mimo sustavy, ak bude clovek mimo sustavy

import string

def konvertuj(cislo: str, sustava: int) -> str:
    hodnoty = [str(i) for i in range(10)] + list(string.ascii_uppercase)
    hodnoty = hodnoty[:sustava]

    vstup = list(reversed(list(cislo)))
    for cislo in vstup:
        if str(cislo) not in hodnoty:
            return False    # mimo sustavy

    mnozina = 0
    vysledok = 0
    for i in vstup:
        hodnota = hodnoty.index(i)
        vysledok += hodnota * (sustava ** mnozina)
        mnozina += 1

    return vysledok

if __name__ == "__main__":
    sustava = int(input('Zadaj sustavu (2 - 36): '))
    
    while True:
        vstup = str(input('Zadaj cislo: '))
        vystup = konvertuj(vstup, sustava)
        
        if vystup == False:
            print('Si mimo sustavy, skus znova.')
        else:
            print(f'Cislo {vstup} v {sustava}-kovej sustave je {vystup} v 10-kovej sustave')
            break