# Zisti, kolko dni ostava do konca roka
# Riesenie je pomocou vstupov (netreba automaticky zistovat dnesny datum cez funkciu)
# zada sa datum, daj prec bodky

def februar(rok:int) -> int:
    if rok % 4 == 0:
        return 29
    else:
        return 28

def konvertuj(datum:str) -> int:
    den, mesiac, rok = datum.split('.')
    den, mesiac, rok = int(den), int(mesiac), int(rok)
    mesiace = [31, februar(int(rok)), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    pocet = mesiace[mesiac - 1] - den
    for i in mesiace[mesiac:]:
        pocet += i

    return pocet

if __name__ == "__main__":
    datum = str(input('Zadaj datum v tvare xx.x.xxxx: '))
    vysledok = konvertuj(datum)
    print(vysledok)