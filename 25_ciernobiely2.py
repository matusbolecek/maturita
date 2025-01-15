import tkinter

subor = 'doplnky/25_ciernobiely2.text'

with open(subor) as f:
    r = f.readline()
    
    w, h = r.split()
    w, h = int(w), int(h)

canvas = tkinter.Canvas(height = h, width = w, bg = 'white')
canvas.pack()

with open(subor, 'r') as f: 
    next(f)
    
    riadok = 0

    for line in f: 
        x = line.split(' ')
        if '\n' in x[-1]:
            x[-1] = x[-1].strip('\n') # v tomto pripade je to nepotrebne, ale je dobre checknut, ci ma riadok \n na konci

        if len(x) % 2 == 1:
            x.append('0')
        
        pixely = 0

        for i in range(0, int(len(x) / 2)):
            index = i * 2
            cierna = int(x[index])
            biela = int(x[index + 1])
            
            canvas.create_line(pixely, riadok, pixely + cierna, riadok, fill = 'black')    
            pixely += cierna
            canvas.create_line(pixely, riadok, pixely + biela, riadok, fill = 'white') # tento riadok je nepotrebny - staci vynechat pixely
            pixely += biela

        riadok += 1

canvas.mainloop()