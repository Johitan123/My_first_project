print("\nEjercicio 6:")
lista = [1, 2, 3, 4, 5, 6, 7]
mitad = len(lista) // 2
lista_invertida = lista[:mitad][::-1] + lista[mitad:]
print(lista_invertida)

# Ejercicio 7: 
# Crear una lista de números del 1 al 5.
# Añade un número al final de la lista usando append.
# Inserta el número 10 en la segunda posición de la lista usando insert.
# Modifica el primer elemento de la lista para que sea 0.

print("\nEjercicio 7:")
lista_numeros = [1, 2, 3, 4, 5]
lista_numeros.append(6)  # Añade el número 6 al final de la lista
lista_numeros.insert(1, 10)  # Inserta el número 10 en la segunda posición
lista_numeros[0] = 0  # Modifica el primer elemento para que sea 0
print(lista_numeros)


