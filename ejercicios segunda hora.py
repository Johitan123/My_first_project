


# ejercicio 1

# el mensaje secreto

# lista1 = ['c', 'o', 'd', 'i', 'g', 'o']
#lista2 = ['s', 'e', 'c', 'r', 'e', 't', 'o']

#print(''.join(lista1) +" "+ ''.join(lista2))



# ejercicio 2

#lista1 = [10, 20, 30, 40, 50]

#lista2 = ((lista1[4:5]) + (lista1[1:4]) + (lista1[0:1]))
#print(lista2)






# ejercicio 3

#creación de un sandwich

#ingredientes = ['pan arriba', 'jamón', 'queso', 'tomate', 'pan abajo']
#sandwich = ingredientes[0:1] + ingredientes[1:3] + ingredientes[3:4] + ingredientes[4:5]
#print(sandwich)






# ejercicio 4   

# crea una lista que tenga los elementos de la lista original duplicados

#lista1 = [1, 2, 3, 4, 5]  
#print (lista1*2)





# ejercicio 5

#Extrayendo el centro de una lista
# Dadá una lista de números, extrae el centro de la lista y crea una nueva lista con esos elementos.


#lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9
#lista1 = len(lista1)
#centro = (lista1//2) + 1
#print(centro)




# ejercicio 6
# Slicing de listas
# Se deben invertir la primera mitad y la segunda mitad de la lista original.


print("\nEjercicio 6:")
lista = [1, 2, 3, 4, 5, 6, 7]
mitad = len(lista) // 2
lista_invertida = lista[:mitad][::-1] + lista[mitad:]
print(lista_invertida)