def count(a1, b1, c1, a2, b2, c2):
    if a1*b2-b1*a2 == 0:
        print("Układ równań nie posiada rozwiązania")
    else:
        x = 0.0
        y = 0.0
        x = (c1*b2-b1*c2)/(a1*b2-b1*a2)
        y = (a1*c2-c1*a2)/(a1*b2-b1*a2)
        print("Wartość x wynosi: ", x ," a wartość y wynosi: ", y)

def main():
    print("a1x + b1 = c1")
    print("a2x + b2 = c2")
    a1=float(input("Podaj wartość a1 z pierwszego równania: "))
    b1=float(input("Podaj wartość b1 z pierwszego równania: "))
    c1=float(input("Podaj wartość c1 z pierwszego równania: "))
    a2=float(input("Podaj wartość a2 z drugiego równania: "))
    b2=float(input("Podaj wartość b2 z drugiego równania: "))
    c2=float(input("Podaj wartość c2 z drugiego równania: "))
    #a1x + b1 = c1
    #a2x + b2 = c2
    count(a1, b1, c1, a2, b2, c2)
    str(input("..."))

if __name__ == "__main__":
    main()