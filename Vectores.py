#ejercicio 1
numeros1 = []

for i in range(5):
    num1 = int(input(f"Ingrese un numero por favor: {i+1}: "))
    numeros1.append(num1)

Resultado = sum(numeros1)
print("el resultado de los 5 numeros es: ",Resultado)

#___________________________________________________________

#ejercicio 2
numeros2 = []

for i in range(10):
    num2 = int(input(f"Ingrese un numero del 1 al 10 por favor: {i+1}: "))
    numeros2.append(num2)

Suma_de_Datos = sum(numeros2)

Promedio = Suma_de_Datos / len(numeros2)

print("El preomedio de los 10 numeros es: ", Promedio)

#__________________________________________________________________________________________

#ejercicio 3
numeros3 = []

for i in range(7):
    num3 = int(input(f"Ingrese un numero del 1 al 7 por favor: {i+1}: "))
    numeros3.append(num3)

Mostrar_Datos = (numeros3)

Mostrar_Datos = max(numeros3)

print("el numero mas alto es: ", Mostrar_Datos)

#____________________________________________________________

#ejercicio 4
Numeros4 = [1,4,7,9,-2,-6,2,10]

numeros_positivos = 0

for Numeros in Numeros4:
    if Numeros > 0:
        numeros_positivos += 1

print("Los numeros positivos son: ", numeros_positivos)

#_______________________________________________________________

#ejercicio 5
nombres = ["Oscar","Stacy","Michelle","Orlin","Nicole","Diego"]

nombres.reverse()
print("Los nombres invertidos son: ",nombres)