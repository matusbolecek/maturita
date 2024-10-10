def narodenie(rok, mesiac, den) -> str | int:
    rok = int(rok)
    if rok >= 50:
        rok += 1900
    else:
        rok += 2000

    mesiac = int(mesiac)
    if mesiac - 50 > 0:
        pohlavie = "zena"
        mesiac = mesiac - 50
    else:
        pohlavie = "muz"
    
    den = int(den)

    return pohlavie, rok, mesiac, den

def main():
    cislo = input('Zadaj rodne cislo: ')
    rc2 = (cislo[:6] + cislo[7:])
    
    while int(rc2) % 11 != 0:
        print('nespravne rodne cislo')
        cislo = input('Zadaj rodne cislo: ')

    pohlavie, rok, mesiac, den = narodenie(rc2[:2], rc2[2:4], rc2[4:6])
    print(f'Narodil si sa {den}. {mesiac}. {rok} a si {pohlavie}')

if __name__ == "__main__":
    main()