# neni maturitny

def vypocet(rychlost) -> str:
    if rychlost <= 80:
        return 'pridaj'
    elif rychlost > 140:
        return 'pribrzdi!'
    else:
        return 'mozes pridat!'

def main() -> int:
    rychlost = int(input('Zadaj rychlost: '))
    return (vypocet(rychlost))
    
if __name__ == "__main__":
    print(main())