# babka stratila pin, pamata si, ze prve cislo je 3, druhe cislo je mensie nez 2, tretie cislo je 5, stvrte je mensie rovne 7
# vypis vsetky kody a pocet
# zapis do suboru piny.txt

if __name__ == "__main__":
    prve, druhe, tretie, stvrte = 3, list(range(2)), 5, list(range(8))
    pocet = 0

    f = open("piny.txt", "a")

    for i in druhe:
        for x in stvrte:
            cislo = str(prve) + str(i) + str(tretie) + str(x)
            f.write(cislo)
            f.write('\n')
            pocet += 1

    f.close()
    print('Pocet pinov je', pocet)