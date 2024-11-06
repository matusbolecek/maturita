# zadaj text na zasifrovanie, posunie sa o n pismen. Mas zadat posun
# na maturite netreba medzeru

def sifruj(slovo:str, posun:int) -> str:
    maximum = ord('z') - ord('a') + 1 # tu treba tu jednotku, lebo inak to nerata prve pismeno
    slovo = slovo.lower()
    cisla = []
    posun = posun % maximum

    for letter in slovo:
        hodnota = ord(letter)
        hodnota += posun
        
        if hodnota > ord('z'):
            hodnota -= maximum
        
        cisla.append(hodnota)
    
    vysledok = str()
    for hodnoty in cisla:
        if hodnoty == ord(' ') + posun:
            vysledok += " "
        else:
            pismeno = chr(hodnoty)
            vysledok += pismeno

    return vysledok

if __name__ == "__main__":
    vstup = str(input('Zadaj frazu, ktoru chces zasifrovat: '))
    posun = int(input('Zadaj posun: '))
    
    vysledok = sifruj(vstup, posun)
    print(f'Vysledok je "{vysledok}"')