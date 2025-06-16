
import re

# [:] Coincide con cualquier caracter dentro de los corchetes

username = "rub.$ius_69+"
pattern = r"^[\w._%+-]+$"

match = re.search(pattern, username)
if match:
  print("El nombre de usuario es válido: ", match.group())
else:
  print("El nombre de usuario no es válido")


# Buscar todas las vocales de una palabra
text = "Hola mundo"
pattern = r"[aeiou]"
matches = re.findall(pattern, text)
print(matches)

# Una Regex para encontrar las palabras man, fan y ban
# pero ignora el resto
text = "man ran fan ñan ban"
pattern = r"[mfb]an"

matches = re.findall(pattern, text)
print(matches)

# Ejercicio:
# Nos han complicado el asunto, porque ahora hay palabras que encajan pero no empiezan por esas letras.
# Solo queremos las palabras man, fan y ban
text = "omniman fanatico man bandana"
pattern = r"\b[mfb]an\b"

text = "22"
pattern = r"[4-9]"

matches = re.findall(pattern, text)
print(matches)


# Ejercicio final con todo lo aprendido
# Mejorar esto: https://www.computerhope.com/jargon/r/regular-expression.png
pattern = r"[\w._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
## Buscar corner cases que no pasa y arreglarlo:

text = "lo.que+sea@shopping.online"
pattern = r"[\w._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
match = re.search(pattern, text)
print("Regex para correos electrónicos:", match.group() if match else "No se encontró un correo electrónico válido")

text = "michael@gov.co.uk"
pattern = r"[\w._%+-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2}+\.[a-zA-Z]{2,3}"

# [^]: Coincide con cualquier caracter que no esté dentro de los corchetes
text = "Hola mundo"
pattern = r"[^aeiou]"
matches = re.findall(pattern, text)
print(matches)


import re

def numeros_validos(texto):
    # Este patrón captura solo los números del 18 al 99
    pattern = r"\b(1[89]|[2-9][0-9])\b"
    return re.findall(pattern, texto)

# Ejemplo de uso
texto = "17, 209, 5, 100, 12"
resultado = numeros_validos(texto)
if resultado:
    print("Números válidos entre 18 y 99:", resultado)
else:
    print("No se encontraron números válidos entre 18 y 99.") 