""" 
    Sexto archivo de ayuda. Vamos a ver como interactuar con ficheros (archivos de texto) externos a nuestro código.
    Sobre estos archivos podemos leer o escribir según necesitemos.
"""
# Por defecto los archivos se abren como lectura
fichero = open("ayudaPython/archivo.txt")                     # Creamos un "objeto" del tipo archivo al usar la función open(string con nombre del fichero o dirección al fichero)
print("El archivo entero:\n",fichero.read())                   # Con read sin argumentos leemos el archivo entero
fichero.seek(0)
""" Cada vez que leemos un archivo, se desplaza el cursor tantos bytes como se haya leido (o escrito) anteriormente, por lo que usando la función seek(posición) nos podemos ir al byte que queramos del archivo (si existe) """
print("Solo unos bytes del fichero: ",fichero.read(4))        # Si al read le ponemos argumentos, le indicamos cuantos bytes queremos leer (por lo general un byte es un carácter)
fichero.seek(0)
print("La primera línea: ", fichero.readline())               # Con esto leemos solo una línea

fichero.close()                                               # Con close cerramos el objeto y no podemos interactuar más con el fichero
### SIEMPRE CIERRA TUS ARCHIVOS ###

# Otras formas de abrir para lectura
fichero = open("ayudaPython/archivo.txt",'r')                 # Apertura como lectura, no podríamos escribir
contenido = fichero.readline() + fichero.readline() + fichero.readline()
fichero.close()
open("ayudaPython/archivo.txt",'rb')                          # Apertura para leer en binario (puede ser más útil de lo que parece)
fichero.close()

# Escritura en un fichero
""" 
    Aunque podamos escribir en un fichero que esté abierto para lectura, la recomendación es siempre siempre separar cuando leemos de cuando escribimos para evitar romper algo.
    Cuando hayas terminado de leer o escribir, siempre haz un close.
"""
fichero = open("ayudaPython/archivo.txt",'w')                 # La opción w indica que abrimos el archivo en escritura pero borrando todo lo que haya en el. Se escribe desde 0
fichero.write(contenido)                                      # Con write escribimos el string de parámetro en el fichero
fichero.close()
fichero = open("ayudaPython/archivo.txt",'a')                 # Con a abrimos el fichero en escritura pero, nos vamos a lo último que haya escrito y empezamos a escribir desde ahí, sin borrar nada de lo anterior
fichero.write("dddd")
fichero.close()
fichero = open("ayudaPython/archivo.txt")
print("El archivo entero con los últimos cambios:\n",fichero.read())
fichero.close()

# ¿Si el fichero no existe?
""" 
    Si intentamos abrir para lectura un fichero que no existe, nos generará un error, pero, si lo hacemos para escritura, se creará el fichero.
"""
fichero = open("ayudaPython/destino.txt",'w')               # El fichero no existe (al menos la primera vez que ejecutas), entonces lo creo
ficheroO = open("ayudaPython/archivo.txt")                  # Vamos a copiar este archivo en el otro

for linea in ficheroO:                                      # Podemos iterar todas las líneas del fichero como si una lista se tratase
    fichero.write(linea)
print("Mira en la carpeta que ahora tienes un fichero nuevo")
fichero.close()
ficheroO.close()

fichero = open("ayudaPython/destino.txt")
linea = fichero.readline() 
while linea != "":                                          # Otra manera de iterar archivos
    print(linea)
    linea = fichero.readline()


fichero.seek(15)                                            # Con el seek podemos ir donde queramos
print(fichero.readlines(2))                                 # Con readlines podemos leer tantas lineas como le indicamos y nos las da en una lista

fichero.close()