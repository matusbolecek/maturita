# zadaj sumu v banke

def main(suma) -> str:
    vyber = 0
    peniaze = suma
    while peniaze - vyber > 0:
        peniaze = peniaze - vyber
        vyber = int(input(f'Mas {peniaze}$. Kolko chces vybrat? '))
    else:
        if peniaze == 0:
            print('Dosli ti peniaze!')
        else:
            print(f'Mas menej penazi ako chces vybrat. Vybral si {peniaze}$')
            peniaze = 0

if __name__ == "__main__":
    peniaze = int(input('Kolko mas na ucte?'))
    main(peniaze)