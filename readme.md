# Úvod - Maturitné Príklady z Informatiky

Vitaj na mojom GitHub repozitári, kde zdieľam svoje riešenia maturitných príkladov z informatiky zo štúdia na Gymnáziu Jozefa G. Tajovského (GJGT). 💻🎓

## Obsah
Tento repozitár obsahuje:
- Maturitné zadania a ich riešenia
- Príklady a úlohy na prípravu na maturitu
- Rôzne hry a iné experimenty vytvorené vo voľnom čase na hodinách

## Použitie
Hlavný priečinok obsahuje samostatné príklad so stručnými zadaniami a mojimi riešeniami. Ak máš záujem, môžeš si stiahnuť celý repozitár alebo prejsť na jednotlivé príklady.
Priečinok iné obsahuje rôzne hry alebo iné príklady na prípravu, ktoré nie sú súčasťou maturity. Sú vytvorené so zábavy vo voľnom čase.

## Poznámky
- Pri práci s textom sú výstupné súbory (*.txt) zahrnuté v gitignore, čiže nie sú súčasťou repozitára. Vstupné textové súbory (*.text) zahnruté sú
- Office príklady budú doplnené neskôr

---

Šťastné programovanie! 🎉

# Teoretický základ k príkladom
Tento dokument zahŕňa podpornú dokumentáciu k príkladom.

## Obsah
1. [Trojuholník](#trojuholník)
2. [Priemer](#priemer)
3. [Vlajka](#vlajka)
4. [Rodné číslo](#rodné-číslo)
5. [Bankomat](#bankomat)
6. [Násobilka](#násobilka)
7. [Športka](#športka)
8. [Číselné sústavy 1](#číselné-sústavy-1)
9. [Číselné sústavy 2](#číselné-sústavy-2)
10. [Cézarova šifra](#cézarova-šifra)
11. [Hod kockou](#hod-kockou)
12. [Dni do konca roka](#dni-do-konca-roka)
13. [Čiarový kód](#čiarový-kód)
14. [Kombinačné číslo](#kombinačné-číslo)
15. [Piškvorky](#piškvorky)
16. [Zátvorky](#zátvorky)
17. [Semafor](#semafor)
18. [Reklama](#reklama)
19. [Lopta](#lopta)
20. [Had](#had)
21. [PIN](#pin)
22. [Pracovná doba](#pracovná-doba)
23. [Dĺžka skladieb](#dĺžka-skladieb)
24. [Čiernobiely obrázok 1](#čiernobiely-obrázok-1)
25. [Čiernobiely obrázok 2](#čiernobiely-obrázok-2)

## Trojuholník
Program overuje existenciu trojuholníka a jeho vlastnosti. Trojuholník existuje, ak súčet každých dvoch strán je väčší ako tretia strana. Následne sa určuje, či je:
- **Rovnostranný**: všetky strany sú rovnako dlhé
- **Rovnoramenný**: aspoň dve strany sú rovnako dlhé
- **Rôznostranný**: žiadne strany nie sú rovnako dlhé

Problematické môže byť pochopenie podmienky existencie trojuholníka a správne porovnanie strán.

## Priemer
Jednoduchý program na výpočet priemeru známok a určenie prospechu. Dôležité body:
- Vstup končí zadaním 0
- Kontrola, či je vstup v rozsahu 1-5
- Výpočet priemeru: súčet / počet
- Určenie prospechu podľa hraničných hodnôt (1.5 a 2.0)

## Vlajka
Program na kreslenie vlajok pomocou knižnice tkinter. Kľúčové koncepty:
- Práca s canvas (plátnom)
- Kreslenie základných tvarov
- Práca s farbami
- Vkladanie obrázkov

## Rodné číslo
Program na analýzu rodného čísla. Dôležité informácie:
- Formát: RRMMDD/XXXX
- Ženy majú k mesiacu pripočítané číslo 50
- Celé číslo musí byť deliteľné 11
- Prvé dvojčíslie určuje rok (00-99, nutné určiť storočie)

## Bankomat
Program na rozdelenie sumy na bankovky a mince. Kľúčové body:
- Zostupné zoradenie nominálnych hodnôt
- Použitie celočíselného delenia (//) a modulo (%)
- Postupné odčítavanie najväčších možných hodnôt

## Násobilka
Interaktívny test z malej násobilky. Dôležité prvky:
- Generovanie náhodných čísel
- Bodový systém (3,2,1 bod podľa počtu pokusov)
- Kontrola správnosti výsledku
- Výpočet percentuálnej úspešnosti

## Športka
Program simulujúci žrebovanie Športky. Hlavné body:
- Generovanie náhodných čísel bez opakovania
- Kontrola vstupov v rozsahu 1-49
- Porovnanie tipovaných a vyžrebovaných čísel
- Počítanie zhôd

## Číselné sústavy 1
Program na prevod z desiatkovej do inej sústavy. Algoritmus:
1. Delíme číslo základom novej sústavy
2. Zapisujeme zvyšky po delení
3. Výsledok čítame odzadu
4. Pre základy >10 používame písmená A-Z

Príklad prevodu 83 do sústavy so základom 16:
```
83 : 16 = 5 zvyšok 3
5 : 16 = 0 zvyšok 5
Výsledok: 53 (hex)
```

## Číselné sústavy 2
Program na prevod z ľubovoľnej sústavy do desiatkovej. Algoritmus:
1. Každú cifru vynásobíme mocninou základu podľa pozície
2. Sčítame všetky hodnoty

Príklad prevodu 53 (hex) do desiatkovej sústavy:
```
5 * 16^1 + 3 * 16^0 = 80 + 3 = 83
```

## Cézarova šifra
Jednoduchá šifra založená na posune písmen v abecede. Kľúčové body:
- Práca s ASCII hodnotami (ord(), chr())
- Cyklický posun v rámci abecedy
- Zachovanie veľkosti písmen
- Ošetrenie špeciálnych znakov

## Hod kockou
Simulácia hodu kockou s využitím náhodných čísel. Dôležité prvky:
- Generovanie náhodných čísel
- Počítanie výskytov jednotlivých hodnôt
- Štatistické spracovanie výsledkov

## Dni do konca roka
Program na výpočet zostávajúcich dní do konca roka. Kľúčové body:
- Práca s dátumami
- Kontrola priestupného roka
- Počítanie dní v mesiacoch
- Spracovanie vstupného reťazca

## Čiarový kód
Vizualizácia čiarového kódu pomocou tkinter. Hlavné koncepty:
- Generovanie náhodných čísel
- Kreslenie čiar rôznej hrúbky
- Práca s canvas
- Zobrazenie textu

## Kombinačné číslo
Výpočet kombinačného čísla (n nad k). Dôležité body:
- Implementácia faktoriálu
- Vzorec: n!/(k!(n-k)!)
- Práca s veľkými číslami
- Optimalizácia výpočtu

## Piškvorky
Implementácia hry piškvorky. Kľúčové prvky:
- Práca s canvas
- Zachytávanie kliknutí myši
- Striedanie hráčov
- Kreslenie značiek (X, O)

## Zátvorky
Program na kontrolu a vizualizáciu zátvoriek. Hlavné body:
- Kontrola párovosti zátvoriek
- Práca s farbami
- Kreslenie textu
- Spracovanie vstupu

## Semafor
Animácia semaforu. Dôležité prvky:
- Časovanie (after())
- Zmena farieb
- Kreslenie kruhov
- Nekonečný cyklus

## Reklama
Animovaný text - reklama. Kľúčové koncepty:
- Posúvanie textu
- Práca s reťazcami
- Časovanie animácie
- Aktualizácia canvas

## Lopta
Animácia pohybujúcej sa lopty. Hlavné body:
- Fyzika odrazu
- Zmena smeru pohybu
- Detekcia kolízie so stenami
- Plynulá animácia

## Had
Implementácia hry had. Kľúčové prvky:
- Ovládanie šípkami
- Pohyb v smere
- Detekcia kolízie
- Kreslenie čiar

## PIN
Program na generovanie možných PIN kódov. Dôležité body:
- Práca so súbormi
- Generovanie kombinácií
- Filtrovanie podľa podmienok
- Počítanie možností

## Pracovná doba
Spracovanie pracovnej doby zo súboru. Hlavné koncepty:
- Čítanie zo súboru
- Práca s časom
- Výpočet časových rozdielov
- Formátovanie výstupu

## Dĺžka skladieb
Výpočet celkovej dĺžky skladieb. Kľúčové body:
- Čítanie zo súboru
- Spracovanie času (mm:ss)
- Sčítavanie časov
- Prevod sekúnd na minúty

## Čiernobiely obrázok 1
Vykreslenie obrázka podľa hodnôt pixelov. Dôležité prvky:
- Čítanie zo súboru
- Práca s farbami v hex formáte
- Kreslenie jednotlivých pixelov
- Spracovanie matice hodnôt

## Čiernobiely obrázok 2
Vykreslenie obrázka podľa počtu čiernych a bielych pixelov. Hlavné body:
- Čítanie zo súboru po riadkoch
- Striedanie farieb
- Kreslenie súvislých úsekov
- Spracovanie vstupného formátu
