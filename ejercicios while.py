
# EJERCICIOS BUCLE WHILE


#print("\nEjercicio 1")
#numero = 11
#while numero > 1:
     #numero -=1
    # print(numero)



#print("\nEjercicio 2")
#sum = 0
#contador = 0
#while contador < 20:
  #contador +=1
  #if contador % 2 == 0:
   # sum += contador
#print(sum)





#import math  

#print("Ejercicio 3")
#numero = -1
#while numero < 0:
   # try:
        #numero = int(input("\nEscribe un numero positivo:"))
        #if numero < 0:
          #  print("El numero debe ser positivo")
    #except:
       # print("valor erroneo")
#print(f"\nEl factorial del numero es {math.factorial(numero)}")



#print("Ejercicio 4")

#numero = " "

#while True:
        #numero = input("\nEscribe tu contraseña:")
        #if len(numero) < 8:
           # print("La contraseña debe incluir minimo 8 caracteres ")
        #else:
            #print("La contraseña es valida")
           # break



print("Ejercicio 5")
numero = -1
while numero < 0:
  try:
      numero = int(input("\nEscribe un numero positivo:"))
      if numero < 0:
        print("El numero debe ser positivo")
  except:
      print("valor erroneo")   
print(f"\nLa tabla del {numero} es:")
x = 0
while x < 10:
   x = x + 1
   tabla = (numero*x)
   print(f"{numero} * {x} = {tabla}")




# SOlUCIÓN DE CHAT GPT

print("Ejercicio 5")

numero = -1
x = 1

while x <= 10:
    if numero < 0:
        try:
            numero = int(input("\nEscribe un número positivo: "))
            if numero < 0:
                print("El número debe ser positivo")
        except ValueError:
            print("Valor erróneo, escribe un número válido.")
    else:
        print(f"{numero} * {x} = {numero * x}")
        x += 1





print("\nEjercicio 6:")
n = int(input("Introduce un número entero positivo N: "))

numero = 2
while numero <= n:
  es_primo = True  # Asumimos que el número es primo hasta que se demuestre lo contrario
  divisor = 2
  while divisor * divisor <= numero:  # Optimizamos: no es necesario probar divisores hasta numero
    if numero % divisor == 0:
      es_primo = False  # Si encontramos un divisor, no es primo
      break  # Salimos del bucle interior
    divisor += 1
  if es_primo:
    print(numero)

  numero += 1



 