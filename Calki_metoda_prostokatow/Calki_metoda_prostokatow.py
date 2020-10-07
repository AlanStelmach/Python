def count(a, b, n):  # Metoda szacująca wartość całki funkcji f w podanym przedziale
    if n == 0:
        return 0  # Zwrócenie 0 w przypadku gdy nie da się podzielić funkcji na kilka prostokątów

    else:
        total = 0.0  # Przygotowanie zmiennej na oszacowaną wartość całki
        h = float((b - a) / n)  # Obliczenie wysokości prostokątów

        for x in range(n):
            total = total + (a + (x + 1.0) * h)  # Wyliczenie kolejnych pól prostokątów i ich sumowanie

        total = total * h

        return total


def main():
    start = float(input("Podaj początek przedziału: "))  # Wczytanie początku przedziału
    end = float(input("Podaj koniec przedziału: "))  # Wczytanie końca przedziału
    amount = int(input("Podaj ilość prostokątów: "))  # Wczytanie na ile prostokatów należy podzielić wykes funkcji w podanym przedziale

    print("Oszacowana wartość całki wynosi:  ", count(start, end, amount))
    str(input("..."))
if __name__ == "__main__":
    main()