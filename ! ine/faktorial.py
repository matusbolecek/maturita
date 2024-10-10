# nematuritny a nedokonceny ig

def faktorial(cislo) -> int:
    vysledok = cislo
    for i in range (cislo - 1, 0, -1):
        vysledok = vysledok * i
    
    return vysledok

if __name__ == "__main__":
    cislo = int(input('Zadaj cislo na faktorial: '))
    vysledok = faktorial(cislo)
    print('Vysledok je', vysledok)