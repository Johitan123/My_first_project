
import os 
os.system('cls' if os.name == 'nt' else 'clear')

persona = {
    "nombre": "namesu",
    "edad": 25,
    "es_estudiante": True,
    "calificaciones": [7, 8, 9],
    "socials": {
        "twitter": "jol@e",
        "facebook": "jsddasda",
        "insta": "pichurria.com"
    }
}
         
print(persona["nombre"])
print(persona["calificaciones"][2])
print(persona["socials"]["twitter"])

# cambiar valores al acceder
persona["nombre"] = "madeval"
persona["calificaiones[2]"] = 23


# ELiminar un valor
del persona["edad"]
#print(persona)

#mostrar el valor eliminado pero volverlo a eliminar
es_estudiante = persona.pop("es_estudiante")
print(f"es_estudiante: {es_estudiante}")
#print(persona)

# sobreeescribir los valores
a = { "name": "midudev", "age":25}
b = { "name": "madeval", "es_estudiante":True}

a.update(b)
print(a)


#comprobar una propiedad
print ("name" in persona) # True
print ("nombre" in persona) # False







#obtener todas las claves
print(persona.keys())

#obtener todos los valores
print(persona.values())

#obtener tanto clave como valor
print("\nitems:")
print(persona.items())


# muy util para mostrar llaves y valores en orden
for key, value in persona.items():
    print(f"{key} : \n{value}")
      


