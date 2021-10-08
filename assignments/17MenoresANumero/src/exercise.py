
def crear_matriz():
    A = int(input())
    B = int(input())
    matriz = []
    for i in range(A):
        matriz.append([])
        for j in range(B):
            matriz[i].append(int(input()))
    return matriz

def menor_diez(matriz):
    resultado = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]<10:
                resultado.append(matriz[i][j])
    return resultado

def main():
    matriz = crear_matriz()
    resultado = menor_diez(matriz)
    print(resultado)
   

if __name__=='__main__':
    main()
