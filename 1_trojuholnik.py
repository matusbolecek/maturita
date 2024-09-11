# maturitny

def read(vstup) -> float:
    strana = float(input(f'Zadaj dlzku strany {vstup}: '))
    return strana

def existuje(a, b, c) -> bool:
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

def vlastnosti(a, b, c) -> str:
    if a == b and b == c and a == c:
        return 'rovnostranny'
    elif a == b or b == c or a == c:
        return 'rovnoramenny'
    else:
        return 'roznostranny'

# Zistovanie, ci je pravouhly na maturite nie je
    
def pravouhly(a, b, c) -> bool:
    strany = [a, b, c]
    strany.sort()

    if strany[0]**2 + strany[1]**2 == strany[2]**2:
        return True
    else:
        return False

def main() -> str:
    a = read('a')
    b = read('b')
    c = read('c')

    if existuje(a, b, c) == True:
        print('trojuholnik existuje')
        
        vlastnost = vlastnosti(a, b, c)
        print(f'trojuholnik je {vlastnost}')

        if pravouhly(a,b,c) == True:
            print('trojuholnik je pravouhly')
        else:
            print('trojuholnik nie je pravouhly')
    
    else:
        print('trojuholnik neexistuje')

if __name__ == "__main__":
    main()