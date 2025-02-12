# pocet riadkov, slov a znakov v texte.

def main(subor):
    s = open(subor,'r')

    riadky, slova, znaky = 0, 0, 0
    for i in s.readlines():
        riadky += 1
        riadok_slova = i.split(' ')
        slova += len(riadok_slova)
        riadok_pismena = list(i.strip('\n'))
        znaky += len(riadok_pismena)

    return riadky, slova, znaky

if __name__ == "__main__":
    subor = 'doplnky/26_pocetvtexte.text'
    riadky, slova, znaky = main(subor)
    print(f'Subor ma \n{riadky} riadkov \n{slova} slov \n{znaky} znakov')