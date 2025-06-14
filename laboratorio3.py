import re 
#usamos una exprecion regular avansada para sacar palabras en mayusculas de un acadena 
cadena="ESTO es un EJEMPLO de uso AVANSADO de CADENAS y Expresiones REGULARES."
#expresion regular que busca palabras completamente en mayusculas
clave=r"\b[A-Z]{2,}\b"
#determinamos todas las coincidencias
palabras_mayusculas=re.findall(clave,cadena)
print("palabras en mayusculas:",palabras_mayusculas)