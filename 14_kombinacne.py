# na vstupe je pocet ziakov v triede a velkost skupin
# factorial musi byt rucne vytvoreny, nie import

def faktorial(cislo) -> int:
    vysledok = cislo
    for i in range (cislo - 1, 0, -1):
        vysledok = vysledok * i
    
    return vysledok

def kombinacne(k, n) -> int:
    citatel = faktorial(n)
    menovatel = faktorial(k) * faktorial(n - k)

    vysledok = citatel / menovatel

    return int(vysledok)

if __name__ == "__main__":
    ziaci = int(input('Zadaj pocet ziakov: '))
    skupiny = int(input('Zadaj pocet skupin: '))
    vysledok = kombinacne(skupiny, ziaci)

    print(vysledok)