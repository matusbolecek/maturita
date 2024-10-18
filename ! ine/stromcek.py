def main(pocet):
    x = 1
    uprava = pocet // 2
    y = uprava * 2 + 1

    char1 = '*'
    char2 = ' '

    for i in range(y // 2):
        prazdne = (y - x) // 2
        out = str(prazdne * char2) + str(x * char1)
        x += 2

        print(out)

if __name__ == "__main__":
    main(25)