
import os 
os.system('cls' if os.name == 'nt' else 'clear')
  
print("Ejercicio 6")

numero = -1

while numero < 0:
    try:
        numero = int(input("\nEscribe un número positivo: "))
        if numero < 0:
            print("El número debe ser positivo")
    except ValueError:
        print("Valor erróneo, escribe un número válido.")

x = 2
es_primo = True
while x < 100:
    if x % 2 == 0:
        es_primo = True
    break
x += 1


if numero > 1 and es_primo:
    print(f"El número {numero} es primo")
else:
    print(f"El número {numero} no es primo")

