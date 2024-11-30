# vstup je nejaka suma (v eurach) a vystup je rozdelenie tejto sumy na bankovky
# na maturite nie su centy

bankovky = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]

def vypocitaj(suma, list = bankovky) -> list:
    vydavok = []
    for penaze in list:
        pocet = suma // penaze
        suma -= pocet * penaze
        vydavok.append(int(pocet))
    
    return vydavok

def rozpis(vydavky, bankovky = bankovky) -> str:
      for i in range(0, len(vydavky)):
        pocty = f'Mas {vydavky[i]} {bankovky[i]}-eurovych'
        if bankovky[i] >=5 and int(vydavky[i]) != 0:
            print(pocty,'bankoviek') 
        elif bankovky[i] <=2 and int(vydavky[i]) != 0:
            print(pocty,'minci') 
        else:
            pass

if __name__ == "__main__":
    suma = float(input('Vloz sumu: '))
    vydavok = vypocitaj(suma)
    rozpis(vydavok)