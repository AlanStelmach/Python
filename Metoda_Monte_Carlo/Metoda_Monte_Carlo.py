import random

def f(x): # Funkcja zwracająca wyliczoną wartość funkcji f z podanego x
    return x*x+2*x

def antiderivative(x): # Funkcja zwracająca wyliczoną wartość pochodnej z podanego x
    return x**3 / 3. + x**2

def count(s, xk, xp): # S - liczba "trafień" (prób), xk - koniec przedziału xp - początek przedziału
    hit = 0 # Zmienna przechowująca ogólną wartość prób
    dx = abs(xk-xp) # Zakres od xk do xp (wart. bezwględna)
    for i in range(s):
        x = xp + random.random()*(abs(xp-xk)) # Obliczenie punktu x = początek przedziału + wylosowana wartość z zakresu od xp do xk (wart. bezwględna)

        hit += f(x) # Obliczenie wartości próby z punktu x i dodanie jej do ogólnej wartości prób
    total = dx*hit/s # Zakres * ( ogólna wartość prób / liczbę prób)
    return total

def main():

    for i in range(10): # Wylosowanie z przedziału od -100 do 100 wartości xp (początek przedziału) i xk (koniec przedziału)

        xp = random.randint(-100, 100)
        xk = random.randint(-100, 100)

        xp, xk = sorted([xp, xk]) # Posortowanie wylosowanych wartości

        numerical = count(100000, xk, xp)
        real = antiderivative(xk) - antiderivative(xp)

        print("{:<4d} XP ={:=3d} XK ={:=3d} Wartość rzeczywista całki ={:>10.2f} Wartość numeryczna całki ={:>10.2f} Błąd względny w % ={:>11.8f}".\
            format(i+1, xp, xk, real, numerical, 100. * (real - numerical) / (real or 1)))

    str(input("..."))

if __name__ == "__main__":
    main()