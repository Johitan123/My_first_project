import os 
os.system('cls' if os.name == 'nt' else 'clear')
  
  
print("Ejercicio 6")

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
