def count(tab):
    total=0
    if len(tab) == 1 and len(tab[0]) == 1: # Obliczenie wyznacznika dla macierzy 1x1
        total = tab[0][0]
    elif len(tab) == 2 and len(tab[0]) == 2: # Obliczenie wyznacznika dla macierzy 2x2
        total = tab[0][0] * tab[1][1] - tab[1][0] * tab[0][1]
    elif len(tab) == 3 and len(tab[0]) == 3: # Obliczenie wyznacznika dla macierzy 3x3
        total = (tab[0][0]*tab[1][1]*tab[2][2])+(tab[0][1]*tab[1][2]*tab[2][0])+(tab[0][2]*tab[1][0]*tab[2][1])-(tab[0][2]*tab[1][1]*tab[2][0]+tab[0][0]*tab[1][2]*tab[2][1]+tab[0][1]*tab[1][0]*tab[2][2])
    elif len(tab) == 4 and len(tab[0]) == 4: # Obliczenie wyznacznika dla macierzy 4x4
        total = tab[0][0]*tab[1][1]*tab[2][2]*tab[3][3] + tab[0][0]*tab[1][2]*tab[2][3]*tab[3][1] + tab[0][0]*tab[1][3]*tab[2][1]*tab[3][2] + tab[0][1]*tab[1][0]*tab[2][3]*tab[3][2] + tab[0][1]*tab[1][2]*tab[2][0]*tab[3][3] + tab[0][1]*tab[1][3]*tab[2][2]*tab[3][0] + tab[0][2]*tab[1][0]*tab[2][1]*tab[3][3] + tab[0][2]*tab[1][1]*tab[2][3]*tab[3][0] + tab[0][2]*tab[1][3]*tab[2][0]*tab[3][1] + tab[0][3]*tab[1][0]*tab[2][2]*tab[3][1] + tab[0][3]*tab[1][1]*tab[2][0]*tab[3][2] + tab[0][3]*tab[1][2]*tab[2][1]*tab[3][0] - (tab[0][0]*tab[1][1]*tab[2][3]*tab[3][2] + tab[0][0]*tab[1][2]*tab[2][1]*tab[2][2] + tab[0][0]*tab[1][3]*tab[2][2]*tab[3][1] + tab[0][1]*tab[1][0]*tab[2][2]*tab[3][3] + tab[0][1]*tab[1][2]*tab[2][3]*tab[3][0] + tab[0][1]*tab[1][3]*tab[2][0]*tab[3][2] + tab[0][2]*tab[1][0]*tab[2][3]*tab[3][1] + tab[0][2]*tab[1][1]*tab[2][0]*tab[3][3] + tab[0][2]*tab[1][3]*tab[2][1]*tab[3][0] + tab[0][3]*tab[1][0]*tab[2][1]*tab[3][2] + tab[0][3]*tab[1][1]*tab[2][2]*tab[3][0] + tab[0][3]*tab[1][2]*tab[2][0]*tab[3][1])

    return total

def main():

    print("1. Wyznacznik macierzy 1x1: ")
    print("2. Wyznacznik macierzy 2x2: ")
    print("3. Wyznacznik macierzy 3x3: ")
    print("4. Wyznacznik macierzy 4x4: ")
    x=int(input("Podaj odpowiednią opcje: ")) # Utworzenie macierzy o wybranym rozmiarze i wypełnienie jej wartościami
    if x == 1:
        tab = [[0 for col in range(1)] for row in range(1)]
        for i in range(len(tab)):
            for j in range(len(tab[i])):
                tab[i][j] = int(input("Podaj warość elementu macierzy: "))
    elif x == 2:
        tab = [[0 for col in range(2)] for row in range(2)]
        for i in range(len(tab)):
            for j in range(len(tab[i])):
                tab[i][j] = int(input("Podaj warość elementu macierzy: "))
    elif x == 3:
        tab = [[0 for col in range(3)] for row in range(3)]
        for i in range(len(tab)):
            for j in range(len(tab[i])):
                tab[i][j] = int(input("Podaj warość elementu macierzy: "))
    elif x == 4:
        tab = [[0 for col in range(4)] for row in range(4)]
        for i in range(len(tab)):
            for j in range(len(tab[i])):
                tab[i][j] = int(input("Podaj warość elementu macierzy: "))
    else:
        print("Błędna wartość!")
        print("Wciśnij Enter aby powrócić: ")
        wait=str(input("..."))
        main()
    print("Wyznacznik macierzy jest równy: ", count(tab))
    str(input("..."))
    
if __name__ == "__main__":
    main()