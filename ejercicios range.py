
# EJERCICIO FOR AND RANGE


#Imprime los numeros
print("\nEjercicio 1:")
for numero in range(1,11):  # range(inicio, fin, paso)
  print(numero)



#Imprime los numeros impares del 1 al 20 usando for and range
print("\nEjercicio 2:")
for numero in range(1,20,2):  # range(inicio, fin, paso)
  print(numero)


#Imprime los mnultiplos de 5 al 50 usando for and range
print("\nEjercicio 3:")
for numero in range(5,51,5):  # range(inicio, fin, paso)
  print(numero)


#Imprime los numeros del 10 al 1
print("\nEjercicio 4:")
for numero in range(10,0,-1):  # range(inicio, fin, paso)
  print(numero)


print("\nEjercicio 5:")
#calcula la suma de los números del 1 al 100:
suma = sum(range(1,101))
print(suma)


# Ejercicio 5: Suma de números en un rango
# Calcula la suma de los números del 1 al 100 (inclusive) usando un bucle for y range().
print("\nEjercicio 5:")
suma = 0
for i in range(1, 101):
  suma += i
print(f"La suma de los números del 1 al 100 es: {suma}")



print("\nEjercicio 6:")
# Pide al usuario un número
# Introduce la tabla de multiplicar del 1 al 10 de ese número:
numero = int(input("\nintroduce un numero:"))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
