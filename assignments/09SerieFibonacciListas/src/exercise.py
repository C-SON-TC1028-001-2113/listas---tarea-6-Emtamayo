def main():
    n = int(input())
    suma = 0
    n1 = 1
    n2 = 1
    serie = []
    while n <= -1 :
        n = int(input())
    if n == 0 :
        print(serie)
    elif n == 1:
        serie.append(0)
        print(serie)
    elif n == 2:
        serie.append(0)
        serie.append(1)
        print(serie)
    else :
        serie.append(0)
        serie.append(1)
        serie.append(1)
        for i in range(n-3) :
            suma = n1 + n2
            n2 = n1
            n1 = suma
            serie.append(suma)
        print(serie)

if __name__=='__main__':
    main()
