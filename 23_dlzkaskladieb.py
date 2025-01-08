# V subore su zadane nazvy skladieb a dlzky (Nazov mm:ss)
# Program precita subor a scita minuty a sekundy - vystup je celkova dlzka CD / albumu

def main(subor):
    minuty, sekundy = 0, 0
    
    with open(subor) as skladby:
        for line in skladby:
            a = line.split(" ")
            x = a[-1]
            mm, ss = x.split(':')
            mm, ss = int(mm), int(ss)

            minuty += mm
            sekundy += ss

    minuty += sekundy // 60
    sekundy = sekundy % 60

    return minuty, sekundy

if __name__ == "__main__":
    subor = 'doplnky/23_dlzkaskladieb.text'
    minuty, sekundy = main(subor)

    print(f'CD má {minuty} minút a {sekundy} sekúnd')