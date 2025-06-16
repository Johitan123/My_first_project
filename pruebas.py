
import os 
os.system('cls' if os.name == 'nt' else 'clear')



print("\nEjercicio 6:")
# Pide al usuario un número
# Introduce la tabla de multiplicar del 1 al 10 de ese número:
numero = int(input("\nintroduce un numero:"))
for numero in range(1,11):
  print("la tabla de multiplicar del {numero} * {range} es:")
