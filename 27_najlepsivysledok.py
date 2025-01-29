# vytvorite si subor, kde bude uvedene priezvisko sportovca (jednoslovne) a jeho namerany cas v sekundach
# vytvorte program, ktory vyberie najlepsi vysledok (minimalny cas)

def precitaj(subor) -> list:
    out = []
    with open(subor) as vysledky:
        for line in vysledky:
            x = list(line.split(' '))
            
            if '\n' in x[-1]:
                x[-1] = x[-1].strip('\n')

            out.append(x)

    return out

def minimalna(zoznam):
    minim = zoznam[0]
    
    for vysledok in zoznam:
        if int(minim[1]) > int(vysledok[1]):
            minim = vysledok
    
    return minim

if __name__ == "__main__":
    subor = 'doplnky/27_najlepsivysledok.text'
    zozn = precitaj(subor)
    minimum = minimalna(zozn)
    mm, ss = int(minimum[-1]) // 60, int(minimum[-1]) % 60
    print(f'Vitazom je {minimum[0]} s casom {mm}:{ss}')