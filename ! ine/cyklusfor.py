# nie je maturitny
# dalo by sa to robit lepsie, ze sa spravia 2 listy, ale je to totalne jedno tbh

import statistics

def zisti(ludia) -> list:
    mzdy = []
    
    for i in range(ludia):
        mzda = int(input(f'Vloz hodinovu mzdu {i+1}. cloveka: '))
        hodiny = int(input(f'Vloz pocet hodin {i+1}. cloveka: '))
        plat = mzda * hodiny
        mzdy.append(plat)
    return mzdy

def porovnaj(mzda):
    if mzda <= 800:
        return 'mal sa lepsie ucit'
    elif mzda >= 8000:
        return 'prezije, gratulujem'
    else:
        return 'je priemer'

def uprav(mzdy) -> list:
    vysledky = []
    for items in mzdy:
        vysledky.append((items))
        vysledky.append((porovnaj(items)))
    
    return vysledky

def vycisli(vysledky):
    for i in range(0, len(vysledky), 2):
        print(f'{(i + 2) / 2}. clovek zaraba {vysledky[i]} a', vysledky[i+1])

def priemer(platy):
    return sum(platy) / len(platy)

if __name__ == "__main__":
    pocet = int(input('Zadaj pocet ludi: '))
    
    mzdy = zisti(pocet)
    vysledky = uprav(mzdy)

    vycisli(vysledky)
    print(f'Priemerný plat je {int(priemer(mzdy))}')
    print(f'Mediánový plat je {int(statistics.median(mzdy))}')