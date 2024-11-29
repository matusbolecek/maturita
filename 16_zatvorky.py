# zapis vyraz v zatvorkach (max 7 farieb): vzorovy vstup (((aa)))
# zisti, ci pocet lavych a pravych zatvoriek je spravny
# ak ano, vykresli ich farebne

import tkinter

def over(vyraz):
    rozdelene = list(vyraz)

    if rozdelene.count('(') == rozdelene.count(')'):
        return True
    else:
        return False

def vykresli(vyraz, h = 200, w = 600, t = 35):
    farby = ['blue', 'red', 'green', 'yellow', 'orange', 'purple', 'pink'] # 7 je ocakavane maximum
    canvas = tkinter.Canvas(height = h, width = w, bg = 'white')
    canvas.pack()

    r = list(vyraz)
    a = 0
    b = r.count('(') - 1
    x = 0
    s = t - 15 # medzera medzi znakmi

    for znaky in r:
        if znaky == '(':
            canvas.create_text(20 + x * s, 20, text = znaky, fill = farby[a], font = ('courier New', t, 'bold'))
            a += 1
        elif znaky == ')':
            canvas.create_text(20 + x * s, 20, text = znaky, fill = farby[b], font = ('courier New', t, 'bold'))
            b -= 1            
        else:
            canvas.create_text(20 + x * s, 20, text = znaky, fill = 'black', font = ('courier New', t, 'bold'))
        
        x += 1

    canvas.mainloop()

if __name__ == "__main__":
    vyraz = str(input('Zadaj vyraz: '))

    if list(vyraz).count('(') < 8 and list(vyraz).count(')') < 8:
        if over(vyraz) == True:
            vykresli(vyraz)
        else:
            print('Pocet zatvoriek na jednej strane sa nerovna poctu na druhej strane!')
    else:
        print('Maximalny pocet zatvoriek je 7!')