  

import os
os.system('cls' if os.name == 'nt' else 'clear')

#print(type(1 > 2))
#print(type(1 < 2))
#print(type(1 == 2))


#print("conversión de tipos")
#print(type("100"))
#print(type(int("100")))
#print(type(float("100")))
#print(type(str(100)))
#print(type("100" == 100))


#age=20
#print(2+int(age))
#print(2+float(age))
#print("2"+str(age))

#print(bool(" "))

# print(round(3.5, 0))

#my_name = "Juan"
#my_age = 20
#print(f"Hola, mi nombre es {my_name} y tengo {my_age} años")
#print("type de my_name:", type(my_name))

#MI_CONSTANTE = 3.1416
#print("type de MI_CONSTANTE:",(MI_CONSTANTE))




#nombre = input("¿Cuál es tu nombre?\n")
#edad = input("¿Cuál es tu edad?\n")
#city = input("¿De qué ciudad eres?\n")
#print("Hola, mi nombre es " + nombre + " y tengo " + edad + " años" + " y soy de " + city)


#Ejercicio 1
#print("obtener multiples valores a la vez")
#nombre, edad, ciudad = input("¿Cuál es tu nombre?, ¿Cuál es tu edad?, ¿De qué ciudad eres?\n").split(",")
#print("Hola, mi nombre es " + nombre + " y tengo " + edad + " años" + " y soy de " + ciudad)



#Ejercicio 2
#print("\n Sentencias de control")
#edad = 16
#if edad >= 18:
    #print("Eres mayor de edad")
#else:
    #print("Fin del programa")



#print("\n Sentencias condicional con elif")
#nota = 3

#if nota >= 7:
    #print("Aprobado")   
#elif nota >= 4:
    #print("Recuperación")
#else:
    #print("Desaprobado")


#print("\n Condiciones múltiples")
#edad = 16
#tiene_carne = True

#if edad >= 18 and tiene_carne:
    #print("Puedes conducir")    
#else:
    #print("No puedes conducir")

#print("\n Condiciones múltiples con or")
#edad = 16       
#tiene_carne = False
#if edad >= 18 or tiene_carne:
    #print("Puedes conducir")        
#else:
    #print("No puedes conducir") 


#print("\n Condiciones anidadas")
#edad = 17
#tiene_carne = False
#if edad >= 18:
    #if tiene_carne == True:
        #print("Puedes conducir")
    #else:
       # print("No puedes conducir")
#else: 
   # print("No pus conducir")

#if edad < 18 or tiene_carne:
  # print("Policia")





#Ejercicio 3
#tablas de verdad

#print("\nTabla de verdad")
#print("A      B      A and B")
#print("True  True  ", True and True)
#print("True  False ", True and False)
#print("False True  ", False and True)
#print("False False ", False and False)

#tablas de verdad

#print("\nTabla de verdad")
#print("A      B      A or B")
#print("True  True  ", True or True)
#print("True  False ", True or False)
#print("False True  ", False or True)
#print("False False ", False or False)


#numero = 10 #asignación de valor
#es_numero_10 = numero == 10

#if es_numero_10:
    #print("El número es positivo")






#Ejercicio 4

#edad = input("¿Cuál es tu edad?\n")
#edad = int(edad) #convertir a entero
#mensaje = "Eres mayor de edad" if edad >= 18 else "Eres menor de edad"
#print(mensaje)

#print("La condicion ternaria")

#edad = int(input("¿Cuál es tu edad?\n"))
#mensaje = "Eres mayor de edad" if edad >= 18 else "Eres menor de edad"
#print(mensaje)



#Ejercicio 5

#print("\nCrear listas")
#lista1 = [1, 2, 3, 4, 5] #lista de enteros
#lista2 = ["mazorca", "pera", "uva"] #lista de strings
#lista3 = [1, 2, 3, "mazorca", "pera", "uva"] #lista de enteros y strings
#lista4 = [1, 2, 3, 4.5, True, "mazora", "pera", "uva"] #lista de enteros, float, booleano y strings

#lista_vacia = [] #lista vacia
#lista_de_listas = [1, 2], [3, 4] #lista de listas
#matrix = [[1, 2], [3, 4]] 

#print("Lista 1:", lista1)
#print("Lista 2:", lista2)       
#print("Lista 3:", lista3)
#print("Lista 4:", lista4)
#print("Lista vacia:", lista_vacia)
#print("Lista de listas:", lista_de_listas)
#print("Matriz:", matrix)


#print("\nAcceder a los elementos de una lista")
#print(lista1[-1])
#print(lista2[-2])
#print(lista3[2])
#print(lista4[3])

#lista_de_listas = [[1, 2, 3], [4, "calcetin", 6], [7, 8, 9]]
#print("\nAcceder a los elementos de una lista de listas")
#print(lista_de_listas[0][0])
#print(lista_de_listas[1][2])



#Ejercicio 6

# Slicing de listas
#lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#print(lista1[0:5]) # [1, 2, 3, 4, 5]
#print(lista1[2:4]) # [3, 4]
#print(lista1[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#print(lista1[::3]) # [1, 4, 7, 10]
#print(lista1[::-1]) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#print(lista1[::-2]) # [10, 8, 6, 4, 2]
#print(lista1[-1:]) # [10]



#print(lista1[-5:]) # [6, 7, 8, 9, 10]
#print(lista1[1:5:2]) # [2, 4] 
#print(lista1[-5:-1]) # [6, 7, 8, 9]


#lista1[9]= 203
#print(lista1)

#lista1 = lista1 + [11, 12, 13]
#print(lista1)

#lista1 += [14, 15, 16]
#print(lista1)

# recuperar longitud de la lista
#print("Longitud de la lista:", len(lista1))


   


   
# METODOS

#list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

#list.append("o")  # Agrega un elemento al final de la lista
#print(list)

#list.insert(2, "@")  # Inserta un elemento en una posición específica
#print(list)

#list.extend(["e" "l", "m"])  # Agrega varios elementos al final de la lista
#print(list)

#list.remove("c")  # Elimina el primer elemento con el valor especificado
#print(list) 

#list.pop(-3) # Elimina el elemento en la posición especificada (en este caso, el tercer elemento desde el final)
#print(list)  # Imprime la lista después de eliminar el elemento

#list.clear()  # Elimina todos los elementos de la lista
#print(list)  # Imprime la lista vacía

#del list[1:3] # Elimina los elementos en el rango especificado (en este caso, los elementos en las posiciones 1 y 2)
#print(list)  # Imprime la lista después de eliminar los elementos en el rango


#print ("\nOrdenar una lista")
#numbers = [5, 3, 8, 1, 2]
#numbers.sort()  # Ordena la lista en orden ascendente
#print(numbers)  # Imprime la lista ordenada

#print("ordenar listas creando una NUEVA lista")
#sorted_numbers = sorted(numbers)  # Crea una nueva lista ordenada sin modificar la original
#print(sorted_numbers)  # Imprime la nueva lista ordenada

#print("ordenar una lista de cadenas de texto")
#words = ["Banana", "apple", "cherry"]
#sorted_words = sorted(words, key=str.lower)  # Ordena las palabras sin distinguir mayúsculas y minúsculas
#print(sorted_words)  # Imprime la lista de palabras ordenada

#print("ordenar listas creando una NUEVA lista")
#sorted_numbers = sort
# }(numbers)  # Crea una nueva lista ordenada sin modificar la original
#print(sorted_numbers)  # Imprime la nueva lista ordenada


# Mas metodos de listas
"""
animals = ["dog", "cat", "elephant", "lion", "cat", "tiger"]
print(len(animals))  # Imprime la longitud de la lista
print(animals.count("cat")) # Cuenta cuántas veces aparece "cat" en la lista

print("cat" in animals)  # Verifica si "cat" está en la lista
print("giraffe" in animals)  # Verifica si "giraffe" no está en la lista






print("\nBucle while")

# bucle con condición simple
contador = 0
while contador < 5:
    print(contador)
    contador+= 1


# Bucle While
contador = 0
print("\nBucle while a")
while contador < 100:
    print(contador)
    contador += 1
    if contador % 5 == 0:
        print("\nel numero es multiplo de 5")
        break
     



# bucle con continue

print("\nBucle con continue")
contador = 0
while contador < 20:
  contador +=1
  if contador % 2 == 0:
     continue
  print (contador)
  

#else, cuando se ejecuta?
print("\nBucle while con else")
contador = 0
while contador < 5:
   print(contador)
   contador += 1
else:
   print("El bucle ha terminado")






 


# PEDIRLE AL USUARIO UN NUMERO POSITIVO 

numero = -1
while numero < 0:
 try:
    numero = int(input("Escribe un numero positivo:"))
    if numero < 0:
      print("EL número debe ser positivo")
 except:
      print("valor erroneo")
print(f"El numero que has introducido es {numero}")
 




#Bucles For
# Permiten ejecutar un bloque de código repetidamente mientras se itera una lista.
 
print("\n Bucle for")
# Iterar una lista
frutas = ("manzana", "pera", "mandarina")
for fruta in frutas:
 print(fruta)

# Iterar sobre cualquier cosa que sea iterable
cadena = "midudev"
for caracter in cadena:
    print(caracter)

    
# enumerate()
frutas = ("manzana", "pera", "mandarina")
for index, fruta in enumerate(frutas):
    print(f"El índice es {index} y la fruta es {fruta}")


#Bucles anidados

letras = ("a", "b", "c")
numeros = (1, 2, 3)
for letra in letras:
    for numero in numeros:
        print(f"{letra} X {numero}")


# break
animales = ("loro", "loror", "loroee", "raton", "pez")
for index, animal in enumerate(animales):
    print(animal)
    if animal == "loro":
     print(f"el loro está escondido en el índice {index}")
     break

# continue
animales = ("loro", "loror", "loroee", "raton", "pez")
for index, animal in enumerate(animales):
    if animal == "loro":
     continue
    print (animal)"""






# COMPRENSIÓN DE LISTAS

animales = ["loro", "loror", "loroee", "raton", "pez"]
animales_mayus = [animal.upper() for animal in animales]
print (animales_mayus)


# NUMEROS PARES DE UNA LISTA

PARES = [num for num in range(1,100) if num % 2 == 0]

print(PARES)



# range
# Permite crear una secuencia de números. Puede ser útil para for


# Imprime la lista del rango en un renglón
print(list(range(-10, 0)))


# Imprime la lista del rango en varios renglones
for num in range(-10, 0):
    print(num)

# RANGE EN INICIO FIN CADA TANTOS PASOS
# IMPRIMIR SOLO LOS PARES
for num in range(200, 0,-3):
    print(num)


# Hacer 5 veces algo con range en vez de while

contador = 0
while contador < 5:
    print("hacer cinco veces algo")
    contador += 1

for _ in range(5):
    print("hacer 5 veces algo")





 # FUNCIONES

 # DEFINIR LA FUNCIÓN

 #def nombre_de_la_función(parametro1, parametro2, parametro3)
   # docstring
   # cuerpo de la función
   # return valor_de_retorno # opcional

# Ejemplo de una función para imprimir algo en consola
def saludar():
    print("!Hola!")

saludar()

# Ejemplo con parametro
def saludar_a(nombre):
    print(f"!Hola {nombre}!")

saludar_a("miduddev")
saludar_a("madeval" )
saludar_a("sandra")     
saludar_a("festish")



# Funciones con mas parametros
 
def sumar(a, b):
    """Suma 2 números y devuelve el resultado"""
    suma = a + b
    return suma

result = sumar(2, 3)
print(result)


#Documentar las funciones con docstring
def rest(a, b):
    """Resta 2 números y devuelve el resultado"""
    rest = a - b
    return rest

result = rest(2, 3)
print(result)
print(rest.__doc__)
help(rest)


def any(a, b = 5):
    """Multiplica 2 números y devuelve el resultado"""
    return  a * b
print(any(2))

# Argumentos por posición
def describir_persona(nombre, edad, sexo):
    print(f"soy {nombre}, tengo {edad} y me identifico como {sexo}")

describir_persona("midu", 25, "gato")
describir_persona("midu", "perro", 39) #erroneo por posición

#Argumentos por clave
def describir_persona(nombre="midudev", edad = 24, sexo = "gato"):
    print(f"soy {nombre}, tengo {edad} y me identifico como {sexo}")

#SON MEJORES EN LA MAYORIA DE LOS CASOS PUES LOS POSICIONALES PUEDEN GENERAR ERRORES.

describir_persona(nombre="midudev", edad = 24, sexo = "gato")
describir_persona(edad = 24, nombre="madevl", sexo = "perra")

#Argumentos de longitud de variable(*args):
def sumar_numeros(*args):
    sum = 0
    for numero in args:
        sum += numero
        return sum


print((sumar_numeros)(1, 2, 3, 4))
print((sumar_numeros)(1, 2, 3, 4, 5, 6))
print((sumar_numeros)(1, 2, 3))

# Argumentos de clave valor variable(**kwargs):
def mostrar_informacion_de(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_informacion_de(noe="aragan", edado = 25, sexo="mujer")
print("\n")
mostrar_informacion_de(nombre="aragan", ciudad = "sana", sexo="mujer")
print("\n")
mostrar_informacion_de(nombre="aragan", edad = 25, country="uruguay")
print("\n")
mostrar_informacion_de(es_rico="aragan", edad = 25, sexo="mujer")


""" EJERCICIOS

ELEGIR ALGUNOS EJERCICIOS DE RANGE Y FOR Y CONVERTIRLOS 
EN FUNCIONES TRATANDO DE UTILIZAR 
TODOS LOS CONCEPTOS 
VISTO HASTA AHORA"""

# Introduce un numero positivo y retorna la multiplicacion de ese numero por 1 hasta 10
numero = 0
def tabla_multiplicar():
    numero = int(input("imprime un numero positivo: "))
    if numero > 0:
        for i in range(1, 11):
            print(f"{numero} x {i} = {numero * i}")
    else:
        print("valor no aceptado")
tabla_multiplicar()


