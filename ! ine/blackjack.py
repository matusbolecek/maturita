# tiebreaker nefunguje

import random

global karty
global hodnoty
karty = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
hodnoty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def karta(karty = karty):
    draw = random.randint(0, len(karty) - 1)
    return karty[draw]

def konvertuj(kart, list1 = karty, list2 = hodnoty):
    cislo = list1.index(kart)
    return list2[cislo]

def konvertuj_a(zoznam, list1 = karty, list2 = hodnoty):
    esa = 0
    sucet = 0
    for karty in zoznam:
        if karty == "A":
            esa += 1
        else:
            hodnota = konvertuj(karty)
            sucet += hodnota
    
    for i in range(esa):
        if sucet + 11 > 21:
            sucet += 1
        else:
            sucet += 11
    
    return sucet

def game():
    dealer = [karta(), karta()]
    dealer_hodnoty = konvertuj(dealer[0]) + konvertuj(dealer[1])
    print(f'Dealer ma {dealer[0]}')

    hrac_vis = [karta(), karta()]
    hrac_hodnoty = konvertuj(hrac_vis[0]) + konvertuj(hrac_vis[1])

    while hrac_hodnoty <= 21:
        print(f'Tvoje karty su {hrac_vis}')
        query = str(input('karta / x: '))
        if query == 'x':
            break

        else:
            hrac_vis.append(karta())
            nova_hodnota = konvertuj(hrac_vis[-1])
            hrac_hodnoty += nova_hodnota
    hrac_hodnoty = konvertuj_a(hrac_vis)

    if hrac_hodnoty > 21:
        pass
    else:
        while dealer_hodnoty < 17:
            dealer.append(karta())
            nova_hodnota = konvertuj(dealer[-1])
            dealer_hodnoty += nova_hodnota

    if hrac_hodnoty > 21:
        stav = 'lose'
    elif dealer_hodnoty > 21:
        stav = 'win'
    elif hrac_hodnoty < dealer_hodnoty:
        stav = 'lose'
    elif hrac_hodnoty == dealer_hodnoty:
        stav = 'draw'
    else:
        stav = 'win'
    
    return stav, hrac_vis, hrac_hodnoty, dealer_hodnoty, dealer

def tiebreak(dealer, hrac):
    dealer_pocet = len(dealer)
    hrac_pocet = len(hrac)
    
    if dealer_pocet < hrac_pocet:
        result = 'lose'
    elif hrac_pocet < dealer_pocet:
        result = 'win'
    else:
        result = 'draw'

    return result, hrac_pocet, dealer_pocet

def main():
    peniaze = 1000
    print(f'Mas {peniaze} eur')
    
    while peniaze > 0:
        
        stavka = input('Vloz stavku: ')
        if stavka == '':
            stavka = peniaze // 3 
            print(f'Automaticky bolo stavenych {stavka} eur!')
        else:
            stavka = int(stavka)

        if stavka == 0:
            stavka = 1
        elif stavka > peniaze:
            stavka = peniaze
        elif stavka == "x":
            break

        win, hrac_vis, hrac_hodnoty, dealer_hodnoty, dealer_vis = game()
        
        if hrac_hodnoty > 21:
            print(f'Prehral si! Tvoje karty boli {hrac_vis} s hodnotou {hrac_hodnoty}')
        
        elif hrac_hodnoty < dealer_hodnoty and dealer_hodnoty <= 21:
            print(f'Prehral si! Tvoje karty boli {hrac_vis} s hodnotou {hrac_hodnoty} a dealer mal {dealer_hodnoty}: {dealer_vis}')
        
        elif hrac_hodnoty == dealer_hodnoty:
            win, dealer_pocet, hrac_pocet = tiebreak(dealer_vis, hrac_vis)
            if win == 'win':
                uvod = 'Vyhral si!'
            elif win == 'lose':
                uvod = 'Prehral si!'
            else:
                uvod = 'Remizoval si!'

            fraza = str(f'Tvoje karty boli {hrac_vis} s hodnotou {hrac_hodnoty} a dealer mal {dealer_pocet} kariet s hodnotou {dealer_hodnoty}: {dealer_vis}')
        
            print(uvod, fraza)

        else:
            print(f'Vyhral si! Tvoje karty boli {hrac_vis} s hodnotou {hrac_hodnoty} a dealer mal {dealer_hodnoty}: {dealer_vis}')

        if win == 'win':
            peniaze += stavka
            print(f'Gratulujem! Vyhral si {stavka} a mas {peniaze} €')
        elif win == 'lose':
            peniaze -= stavka
            print(f'Lutujeme, prehral si {stavka} € a mas {peniaze} €')
        else:
            pass

if __name__ == "__main__":
    main()