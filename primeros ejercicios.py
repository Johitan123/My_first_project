


import os
os.system('cls' if os.name == 'nt' else 'clear')

#EJERCICIO MIO

try:
    numero1 = int(input("ingrese numero uno: "))
    numero2 = int(input("ingrese numero dos: "))
    if numero1 == 0 or numero2 == 0:
        raise ValueError("Los números deben ser positivos")
except ValueError:
    print("Error: Los valores no son números enteros")
    exit()

suma= (input)("¿que operación desea realizar? suma,resta,multplicación o división?: ")
if suma == "resta":
   print(f"el resultado de la resta es:{numero1-numero2}")
elif suma == "multiplicación":
    print(f"el resultado de la multiplicación es:{numero1*numero2}")
elif suma == "división":
    print(f"el resultado de la división es:{numero1/numero2}")
elif suma == "suma":
    print(f"el resultado de la suma es:{numero1+numero2}")







#Ejercicio 6

# Slicing de listas
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,12, 13, 14, 15, 16, 17, 18, 19, 20]
print(lista1[0:5]) # [1, 2, 3, 4, 5]
print(lista1[2:4]) # [3, 4]
print(lista1[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista1[::-1]) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(lista1[::-1]) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(lista1[::-2]) # [10, 8, 6, 4, 2]
print(lista1[-1:]) # [10]
print(lista1[-5:]) # [6, 7, 8, 9, 10]
print(lista1[1::2]) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(lista1[-5:-1]) # [6, 7, 8, 9]


           



