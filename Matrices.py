#ejercicio 1
matriz1 = []

for i in range(3):
    fila1 = []
    for j in range(3):
        num1 = int(input(f"Ingrese el número para la posición [{i+1}, {j+1}]: "))
        fila1.append(num1)
    matriz1.append(fila1)

suma_total = 0
for fila1 in matriz1:
    suma_total += sum(fila1)

print("La suma de los elementos de la matriz son:", suma_total)

#____________________________________________________________________________________

# #ejercicio 2
matriz2 = [
    [
        [1,1,1,1],
        [2,2,2,2],
        [3,3,3,3],
        [4,4,4,4]
    ]
]

print("Los datos de la matriz son: ",matriz2)

#__________________________________________________

#ejercicio 3
matriz3 = []

for i in range(2):
    fila3 = []
    for j in range(3):
        num3 = int(input(f"Ingrese el número para la posición [{i+1}, {j+1}]: "))
        fila3.append(num3)
    matriz3.append(fila3)

transpuesta = [[matriz3[j][i] for j in range(2)] for i in range(3)]

print("La matriz transpuesta es: ")
for fila3 in transpuesta:
    print(fila3)

#_________________________________________________________________________________________

#ejercicio 4
matriz_A = []
matriz_B = []

print("Ingrese un numero para la primera matriz 2x2: ")
for i in range(2):
    fila4 = []
    for j in range(2):
        num4 = int(input(f"Ingrese el numero para la posición A [{i+1}, {j+1}]: "))
        fila4.append(num4)
    matriz_A.append(fila4)

print("Ingrese un numero para la segunda matriz 2x2: ")
for i in range(2):
    fila4 = []
    for j in range(2):
        num4 = int(input(f"Ingrese el numero para la posición B [{i+1}, {j+1}]: "))
        fila4.append(num4)
    matriz_B.append(fila4)

resultado = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        resultado[i][j] = matriz_A[i][0] * matriz_B[0][j] + matriz_A[i][1] * matriz_B[1][j]

print("El resultado de la multiplicación de las matrices es: ")
for fila4 in resultado:
    print(fila4)

#___________________________________________________________________________________________________

#ejercicio 5
matriz5 = []

print("Ingrese un numero para la matriz 3x3: ")
for i in range(3):
    fila5 = []
    for j in range(3):
        num5 = int(input(f"Ingrese un numero para la posición [{i+1}, {j+1}]: "))
        fila5.append(num5)
    matriz5.append(fila5)

print("Los elementos de la diagonal principal son: ")
for i in range(3):
    print(matriz5[i][i])