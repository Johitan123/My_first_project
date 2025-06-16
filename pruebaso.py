
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



del persona["edad"]
print(persona)
