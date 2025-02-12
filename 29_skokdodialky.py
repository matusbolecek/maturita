# subor ma meno (bez medzier), pri ktorom je 5 ciselnych udajov
# vyber maximum (bez funkcie) a v pripade rovnosti, vypíš všetkých, čo dosiahli vysledok

def main(subor):
    s = open(subor,'r')

    vitaz = [(None, 0)]
    for i in s.readlines():
        riadok = i.split(' ')
        meno = riadok[0]
        
        for x in riadok[1:]:
            x = int(x)
            if x > vitaz[0][1]:
                vitaz = [(meno, x)]
            
            elif x == vitaz[0][1]:
                vitaz.append((meno, x))

    return vitaz

def vypis(vysledky):
    if len(vysledky) == 1:
        print(f'Vitazom je {vysledky[0][0]}, ktory skocil {vysledky[0][1]}')
    
    else:
        mena = []
        for a in vysledky:
            mena.append(a[0])
        print(f'Vitazom su {', '.join(mena)} s vysledkom {vysledky[0][1]}')

if __name__ == "__main__":
    subor = 'doplnky/29_skokdodialky.text'
    x = main(subor)
    vypis(x)