def f(a,b,c,pov,x): # Funkcja zwracająca uzupełnioną funkcję f
    return a*x**pov + b*x + c
def count(x,y,epsilon,a,b,c,pov): # Występuje tylko jeden pierwiastek w funkcji f o przedziale [X,Y], funckja zwraca miejsce zerowe funkcji f
    total = 0
    if x > y: # Jeśli jest to konieczne to zamieniamy granice przedziałów
        x, y = y, x

    epsilon = abs(epsilon)

    if f(a,b,c,pov,x) * f(a,b,c,pov,y) < 0: # Jeśli występuje miejsce zerowe w przedziale to wykonujemy poniższe obliczenia

        total = x # Przybliżenie piierwistka gdyby Y-X < epsilon

        while (y - x) >= epsilon:

            total = (y + x) / 2.0 # Połowa przedziału jako przybliżenie pierwiastka
            if f(a,b,c,pov,x) * f(a,b,c,pov,total) < 0: # Miejsce zerowe jest w przedziale [X,total] -> przesunięcei prawej granicy przedziału
                y = total
            elif f(a,b,c,pov,total) * f(a,b,c,pov,y) < 0: # Miejsce zerowe jest w przedziale [total,Y] -> przesunięcie lewej granicy przedziału
                x = total
            else: # Wyzerowanie iloczynu, miejsce zerowe zostało odnalezione
                break

    elif f(a,b,c,pov,x) == 0: # Sprawdzanie czy lewa i prawa wartość nie jest szukanym pierwiastkiem
        total = x

    elif f(a,b,c,pov,y) == 0:
        total = y

    else: # Pierwiastka nie ma w przedziale albo jest ich więcej niż jeden
        total = "Błąd! W podanym przedziale nie ma pierwiastka, bądź jest ich więcej niż 1."

    return total

def main():
    x = float(input("Podaj wartość lewego elementu przedziału: "))  # Wczytanie lewej i prawej granicy przedziału wraz z dokładnością wyniku
    y = float(input("Podaj wartość prawego elementu przedziału: "))
    epsilon = float(input("Podaj dokładność z jaką ma być zwrócony wynik: "))
    print()
    print("f(x)=a*x^? + b*x + c")
    a = float(input("Podaj wartość elementu a: "))
    b = float(input("Podaj wartość elementu b: "))
    c = float(input("Podaj wartość elementu c: "))
    pov = int(input("Podaj wartość potęgi oznaczonej symbolem '?': "))
    print()
    print("Pierwiastkiem równania jest: ", count(x,y,epsilon,a,b,c,pov))
    str(input("..."))

if __name__ == '__main__':
    main()