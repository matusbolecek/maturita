# Subor obsahuje informacie meno hodina_prichodu:minuta_prichodu hodina_odchodu:minuta_odchodu
# Vypocitajte dlzku pracovnej doby kazdeho
# Vystup: Meno pracoval hh hodin, mm minut

def main(subor):
    vystup = []
    
    with open(subor) as praca:
        for line in praca:
            meno, cp, co = line.split(" ")
            hp, mp = cp.split(':')
            ho, mo = co.split(':')
            hodiny = int(ho) - int(hp)
            minuty = int(mo) - int(mp)
            if minuty < 0:
                minuty += 60
                hodiny -= 1

            vystup.append([meno, hodiny, minuty])

    return vystup

if __name__ == "__main__":
    subor = "doplnky/22_pracovnadoba.text"
    zoznam = main(subor)
    
    for ludia in zoznam:
        print(f'{ludia[0]} pracoval/a {ludia[1]} hodin a {ludia[2]} minut.')