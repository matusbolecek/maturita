# vytvorite si subor, kde bude uvedene priezvisko sportovca (jednoslovne) a jeho namerany cas v sekundach
# vytvorte program, ktory usporiada vysledkovu listinu

def precitaj(subor) -> list:
    out = []
    with open(subor) as vysledky:
        for line in vysledky:
            x = list(line.split(' '))
            
            if '\n' in x[-1]:
                x[-1] = x[-1].strip('\n')

            out.append(x)

    return out

def zorad(zoznam):
    novy = []
    novy.append(zoznam[0])
    zoznam.pop(0)

    for x in zoznam:
        inserted = False
        for i in range(len(novy)):
            if int(x[1]) < int(novy[i][1]):
                novy.insert(i, x)
                inserted = True
                break
        
        if not inserted:
            novy.append(x)
    
    return novy

if __name__ == "__main__":
    subor = 'doplnky/28_vysledkovalistina.text'
    zozn = precitaj(subor)
    novy = zorad(zozn)
    for a in novy:
        print(a[0], "s casom", a[1])