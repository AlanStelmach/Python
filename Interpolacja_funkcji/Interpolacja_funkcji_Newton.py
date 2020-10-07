def count(xf, yf, nw,x): # Metoda interpolująca
    i = 0 #Liczniki
    j = 0
    total = yf[0]
    t = [] # Tablica robocza

    for i in range(nw): # Przypisanie tablicy X do tablicy roboczej
        t.append(float(xf[i]))

    for i in range(nw): # Obliczanie wartości i wstawienia ich do tablicy roboczej
        for j in range(i):
            t[i] = (t[i] - t[j]) / (yf[i] - yf[j])

    for i in range(1, nw): # Obliczanie ze wzoru
        f = 1.0

        for j in range(0, i):
            f = f * (x - xf[j])
            y = total + t[i] * f

    return total


def main():
    xf = list() # Utworzenie listy przechowującej zmienne X
    yf = list() # Utworzenie listy przechowującej zmienne Y

    nw = int(input("Podaj ilość węzłów: ")) # Stopień wielomianu

    for k in range(nw): # Przypisanie X i Y do odpowiednich list
        print("Podaj x", k, ": ")
        tx = input()
        xf.append(float(tx))

        print("Podaj y", k, ": ")
        ty = input()
        yf.append(float(ty))

    xx = float(input("Podaj dla jakiego x chcesz znależć wartość funkcji: x = "))

    print("Przybliżona wartość funkcji w podanym punkcie x = ", xx, " wynosi y = ",count(xf, yf, nw, xx))
    str(input("..."))

if __name__ == "__main__":
    main()