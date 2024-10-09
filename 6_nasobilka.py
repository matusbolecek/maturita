# Maturitny
# Vyskusanie malej nasobilky, test ma 10 uloh. 
# Kazdy priklad ma 3 pokusy (1. pokus 3 body, 2. pokus 2 body, 3. pokus 1 bod)
# Na maturite netreba osetrit, aby sa neopakovali ulohy, ani vypocitat percenta

import random

def generuj(zoznam):
    generovane = None
    while generovane in zoznam or generovane == None:
        prve, druhe = random.randint(1, 10), random.randint(1, 10)
        generovane = {prve, druhe}
        sorted(generovane)

    return prve, druhe

def main(pocet_prikladov) -> list:
    vysledky = []
    ulohy = []
    
    for i in range(pocet_prikladov):
        body = 3
        prve, druhe = generuj(ulohy)

        while body > 0:
            vysledok = int(input(f'Kolko je {prve} * {druhe}? '))           
            if vysledok == prve * druhe:
                break
            else:
                print('Nespravna odpoved! Skus znova.') 
                body -= 1
        
        if body > 0:
            print(f'Spravna odpoved! Ziskavas {body} body!')
            vysledky.append(int(body))
        else:
            print(f'Nespravna odpoved! Ziskavas {body} bodov!')

        # Overovanie prikladov
        if body == 3:
            uloha = {prve, druhe}
            sorted(uloha)
            ulohy.append(uloha)

    return vysledky

def vycisli(zozn):
    i = 1
    for cislo in zozn:
        print(f'{i}. pokus: ziskal si {cislo} body')
        i += 1

    suma = sum(zozn)
    maximum = len(zozn) * 3
    uspesnost = suma / maximum
    print(f'Celkovo si ziskal {suma} bodov ({format(uspesnost, ".0%")})!')

if __name__ == "__main__":
    test = main(10)
    vycisli(test)