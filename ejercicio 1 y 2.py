




# 1. Escribe un programa que pida al usuario un año y determine si es bisiesto o no.
# Un año es bisiesto si es divisible entre 4, pero no entre 100, a menos que también sea divisible entre 400.

import os
os.system('cls' if os.name == 'nt' else 'clear')

age = int(input("Introduce el año que quieres saber si es bisiesto: "))
if age % 4 == 0 and age % 100 != 0:
    print(f"El año {age} es bisiesto")
elif age % 100 == 0 and age % 400 == 0 and age % 4 == 0:
    print(f"El año {age} es bisiesto")
else:
    print(f"El año {age} no es bisiesto")

   


           


