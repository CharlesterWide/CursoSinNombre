"""
    Archivo de ayuda extra. En este veremos como usar las condiciones tanto para las sentencias if como para los bucles.
"""
import random       # De momento esto lo puedes ignorar

# Usando el if
""" Podríamos definir el If como la sentencia de control básica, traducciendolo como una pregunta de "si esto es verdad, hacemos esto" """

if 1:       # Aquí hacemos un mal uso, no tiene sentido este if
    print("Siempre vamos a entrar aquí, es una pregunta sin sentido que siempre será un 'Sí'")

booleanoDeContro = False
if booleanoDeContro:                                        # Nunca podremos entrar aquí porque tenemos una variable fija a False
    print("Nunca me vas a ver")
else:
    print("No he entrado en el if, voy a por el por defecto")

numeroRandom = random.randint(0, 10)                        # Cada vez que lo ejecutes saldrá un resultado diferente
if numeroRandom > 2 and numeroRandom < 5:                   # Usando el AND forzamos a que se cumplan ambas condiciones, "si es esto Y esto, haz esto "
    print("Estamos entre 2 y 5, solo puedo ser un 3 o 4")
elif numeroRandom >= 5 and numeroRandom <= 8:               # Hemos ampliado el rango posible
    print("Estamos en el rango que va desde el 5 al 8 con ambos incluidos")  
elif numeroRandom == 1 or numeroRandom == 0 or numeroRandom == 9:   # Con el OR solo necesitamos que se cumpla una de las condiciones, "si es este o este o este, haz esto"
    print("El numero es o el 0 o el 1 o el 9")     
else:
    print("Aquí no debería llegar")         

# Podemos combinar tantos como queramos
numero1 = random.randint(0, 20)
numero2 = random.randint(0, 20)

if (numero1 < 5 and numero2 < 5) or (numero1 > 15 and numero2 > 15):        # Los paréntesis se evaluan primero, hay que saber cuando se deben usar para forzar condiciones específicas
    print("Ambos números están en los extremos")
elif (numero1 == 5 or numero1 == 6) and (numero2 == 5 or numero2 == 6):     
    print("Los dos números o son 5 o 6")
elif numero1 == 7 and numero2 == 9 or numero1 > 10:                         # Esto es un error, haría falta los paréntesis en alguna parte, ya que si el numero1 es mayor que 10, siempre va a entrar ignorando el and
    print("Un error de formulación de condiciones")


## Condiciones en los bucles ##

booleano = False

while not booleano:                                     # No saldremos del bucle mientras se cumpla la condición 
    if random.randint(0, 20) == 10:                     # Hemos puesto una función directamente en la condición
        booleano = True
        print("Ha salido un 10 y salimos del bucle")
    else:
        print("No hemos generado un 10 de forma aleatoria") 

# Podemos, al igual que con el if, añadir tantas condiciones como necesitemos
while random.randint(-1, 2) != 1 and random.randint(-1, 2) != 1 and random.randint(-1, 2) != 1:
    print("No hemos sacado un 1 tres veces, vuelvo a probar")
print("Han salido tres 1 a la vez, salimos del bucle")

""" 
    Es muy importante recordar que, en los while, la "pregunta" se hace siempre primero, es decir
    hacemos la comprobación antes de ejecutar el código dentro del bucle. Si la condición se cumple de antes
    no entramos siquiera.
"""

## Condiciones en el for?
""" 
    En los bucles for de python, en otros lenguajes si se puede, no podemos meter condiciones, solo podemos usarlos para recorrer iterables (listas, array, rangos...)
"""