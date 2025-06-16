
import os 
os.system('cls' if os.name == 'nt' else 'clear')

# EJERCICIO 1

"""Reed Richards (Mr. Fantantisc) = LETRA R
    Johnny Storm (la Antorcha Humana) = LETRA J

si R = J (true)
si R es diferente J (False)
si no aparece ningunade las dos letras (0 = 0) = (True)

"""



"""
text = "Sanaba bitch" 

def check_is_balanced(text):
    text = text.upper()

    count_r = text.count("R")  # Reed Richards
    count_j = text.count("J")  # Johnny Storm 

    print(f"count_r: {count_r} count_j: {count_j}")

    return count_r == count_j

print(check_is_balanced("rrrrrrrrrrrrrrjjjjjjj"))
print(check_is_balanced("rrrrjjjjjjj"))
print(check_is_balanced("rrrrjjjjjjj"))
print(check_is_balanced("rrrrrrrrrjjjjjjj"))
print(check_is_balanced("aqaqaqa"))






# EJERCICIO 2

#CHALLENGE JURASIC PARK

def carnivo_ros(egg_list) -> int:
    total_eggs = 0
    for eggs in egg_list:
        if eggs % 2 == 0:
            total_eggs += eggs

    return total_eggs

egg_list = [1,2,3,4,5,6,7,8,9,12]
print(carnivo_ros(egg_list))


# EJERCICIO 3

import os 
os.system('cls' if os.name == 'nt' else 'clear')


def sumar_numeros(nums, goal):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)-1):
          if nums[i] + nums[j] == goal:
           return [i, j]
    return None # no se encontro ninguna combinación


nums = [4, 2, 6, 2]
goal = 8
result = sumar_numeros(nums, goal)
print(result)
"""

# solución con diccionario

lista_a = [1, 5, 6, 10, 4, 9]
goal = 8

def find_firs_numb(lista_a, goal):
    seen = {} #diccionario para guardar el numero y indice
    for index, value in enumerate(lista_a): # Sin confirmar
        missing = goal - value # calcular el número que falta para llegar al objetivo
        if missing in seen: return [seen[missing], index]
        seen[value] = index # guardar el número actual a los vistos porque no hemos encontrado el goal.
    return None
 
result = find_firs_numb(lista_a, goal)
print(result)







