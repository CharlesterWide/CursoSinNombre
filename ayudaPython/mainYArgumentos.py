"""
    Segundo archivo extra de ayuda. Aquí vamos a ver como usamos el main con argumentos.

    Importante, para trabajar más fácil, en lugar de usar el botoncito de play del Visual Studio Code, recomiendo trabajar con la consola/terminal para ejecutar el archivo.
    Para ejecutar un archivo de python, ve a la carpeta donde tengas tu archivo .py desde la terminal (o abre la terminal directamente en esa carpeta para que sea más fácil) y lo ejecutas de esta forma:
    python nombreDelPrograma.py argumento1 argumento2 ... argumentoN
"""

import sys                              # Esta librería es imprescindible para trabajar con los argumentos


""" 
    Recuerda lo que hemos visto en clase. La variable __name__ indica el entorno en el que nos encontramos, si es un archivo importado, el __name__ de ese archivo será el mismo nombre del archivo sin el .py.
    En caso de que el archivo sea el que estamos ejecutando, es decir, el código principal, su __name__ será __main__ permitiendo ejecutar código diferente si estamos tratando el código como principal o importado.
    Para extra info ve a la carpeta "modulos" de este mismo repositorio.
"""
if __name__ == "__main__":              # De esta forma, si este es el archivo que ejecutamos, entraremos en el código main
    longitudArgumentos = len(sys.argv)  # Con sys.argv accedemos a la lista de argumentos que hemos pasado al ejecutar el programa
    print("El número de argumentos es:",longitudArgumentos)           # El número mínimo de argumentos, es decir, la longitud mínima de la cadena, siempre va a ser 1, pues el nombre del programa es siempre el primer argumento
    for indice,argumento in enumerate(sys.argv):          # Al ser una cadena podemos recorrerla con un bucle
        print(f"El argumento {indice}º es:",argumento)

""" 
    Si cojo este código y lo ejecuto de esta forma: python .\mainYArgumentos.py 1 2 3
    En la terminal vería esto:
        El número de argumentos es: 4
        El argumento 0º es: .\mainYArgumentos.py
        El argumento 1º es: 1
        El argumento 2º es: 2
        El argumento 3º es: 3
"""