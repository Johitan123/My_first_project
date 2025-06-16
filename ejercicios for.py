# EJERCICIOS FOR


import os 
os.system('cls' if os.name == 'nt' else 'clear')


# EJERCICIO NUMERO 1
 
print("\nEjercicio 1")
PARES = [num for num in range(21) if num % 2 == 0]
print(PARES)

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
print("\nEjercicio 1:")
for numero in range(2, 21, 2):  # range(inicio, fin, paso)
  print(numero)




print("\nEjercicio 2")
#Calcular la media de una lista usando un bucle for

lista = [10, 20, 30, 40, 50, 60]
suma = 0
for num in lista:
	suma += num
Media = suma / len(lista)
print(int(Media))



print("\nEjercicio 3")
#Calcular el número más grande de la lista

lista = [15, 5, 35, 10, 20]
numero_mayor = lista[0]
for num in lista:
	if num > numero_mayor:
		numero_mayor = num
print(numero_mayor)





print("\nEjercicio 4")
# Crea una nueva lista que contenga solo las palabras con más de 5 letras

animales = ["loro", "loror", "loroee", "raton", "pejesapoz"]
animales_largos = [animal for animal in animales if len(animal) > 5]
print(animales_largos)


# CON BUCLE FOR:
for animal in animales:
    if len(animal) > 5:
      print(animal)
	  



print("\nEjercicio 5")
# Pide al usuario una letra y cuenta cuantas palabras empiezan por esa letra

cosas = ["casa", "arbol", "sol", "elefante", "luna", "coche", "arepa"]
letra = input("\nintroduce una letra:")
numero_de_veces = sum(1 for animal in cosas if animal.startswith(letra))
print(f"\nhay {numero_de_veces} palabras que empiezan con la letra {letra}")






# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).

print("\nEjercicio 5:")
palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
letra = input("Introduce una letra: ").lower()  # Convertimos la letra a minúscula
contador = 0
for palabra in palabras:
  if palabra.lower().startswith(letra):  # Comparamos en minúsculas
    contador += 1
print(f"Hay {contador} palabras que empiezan con la letra {letra}")
