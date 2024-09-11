# opakovanie, nie maturita

def delitelnost(cislo, delitel) -> bool:
    if cislo % delitel == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    cislo = int(input('Vloz cislo: '))
    if delitelnost(cislo, 3) == True:
        print('Cislo je delitelne.')
    else:
        print('Cislo nie je delitelne.')