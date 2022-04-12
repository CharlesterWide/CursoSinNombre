""" <--- Abrir comenteario en bloque

    Este es el primero de los archivos de ayuda sobre Python. En cada uno de estos archivos pondré 
    el uso basico de cada uno de los tipos y funciones que vamos a ver y usar. Al final de cada archivo habrá un pequeño
    ejercicio relacionado con lo visto.

    En este primer archivo vamos a ver los tipos de dato simples. Te recomiendo que lo leas primero y luego ejecutes el código para que veas como son los resultados

Cerrar comentario en bloque--->"""


#### El tipo booleano ####

# Decalrarlo

verdadero = True   # Inciando una variable como "True"
falso = False      # Inciando una variable como "False"

# Hay más maneras de declarar un booleano?

verdadero = 10 > 5       # Asignando a una igualdad
falso = not verdadero    # Asignando a otro booleano negado 

verdadero = len("cinco") == 5 # Si la longitud (funcion len) de la palabra "cinco" es igual a 5 tendremos un "True"

#####
#           Para que podemos usar los booleanos?
#####

# Como variables de control

control = False                 # Iniciamos el control como False
contador = 0                    # Declaramos la variable que vamos a controlar
while not control:              # En la condición de este bucle: mientras que control not True (tengamos un False) seguiremos sumando
    contador = contador + 1     # Aumentamos el valor del contador
    if contador == 10:          # Si contador llega a 10 entramos dentro del bloque del if
        control = True          # Asignamos un valor True a control 
                                # Ahora salimos del bucle porque no se cumple la condición de tener un valor False
print(contador)                 # Por terminal veremos un 10

# Como "flags" de estado de una maquina de estados

estado1 = False                 # Declaramos nuestros estados iniciando el tercero como el por defecto
estado2 = False
estado3 = True
salida = False                  # Nusetra variable para salir de la máquina de estado

while not salida:               # Mientras que salida esté en false se ejecutará el bloque dentro del bucle
    if estado1:                 # Solo cuando el flag del primer estado esté activa se ejecutará este código
        salida = True
    if estado2:                 # Solo cuando el flag del segundo estado esté activa se ejecutará este código
        estado2 = False
        estado1 = True
    if estado3:                 # Solo cuando el flag del tercer estado esté activa se ejecutará este código
        estado3 = False
        estado2 = True

if estado1:
    print("Hemos salido con el estado1")
if estado2:
    print("Hemos salido con el estado2")
if estado3:
    print("Hemos salido con el estado3")

# Se puede introducir un booleano por teclado? Respuesta corta: No, Respusta larga: No pero puedes hacer como que si

booleanoDeEntrada = input("Introduce un carácter: ") == 'f'     # Con la funcion input podemos introducir por teclado para interactuar con nuestro código

if booleanoDeEntrada:
    print("Has introducido la f")
else:
    print("No has introducido la f")

"""
    Obviamente son códigos de ejemplo simples, pero son basicamente son los principales usos de los buleanos
"""


#### Numéricos ####

"""
    Dentro de los numéricos tenemos varios "subtipos"
    int:        Número entero con signo, en python tiene un tamaño de 32 bits, es decir, puede ir desde -2^31 (-2147483648) a 2^31 -1 (2147483647)
    double:     Igual que el int, pero con el doble de tamaño
    float:      Números con decimales, tiene un tamaño de 64 bits, uno para el signo, once para el exponente y cincuenta y dos para el numero, es decir desde ±2,2250738585072020 x 10^-308 hasta ±1,7976931348623157x10^308
    long:       Número con decimales pero con el tamaño variable, el tamaño máximo dependerá de la máquina y memoria disponible
    complex:    Numeros complejos que realmente son dos double, uno para la parte real y otro para la imaginaria
"""

# Declaracion
enteroOdoble  =  1234       # Almacena un entero normal 1234
floatOlong    =  1.234      # Almacena el número con decimales 1.234
floatOlong    =  1.234e-3   # Almacena el número con decimales 0.001234
complejo      =  12 + 34j   # Almacena el número complejo 12 +i34 (los americanos usan la j por algun motivo)

# Declaración por operación
enteroOdoble = 12 + 34
floatOlong = 0.012 + 34
floatOlong = 1e-4 * 100
complejo = 12j + 34 + 5j


# Operaciones con números
numero = 2 + 2     # Suma normal entre dos números
numero += 2        # Resultado de sumar a si mismo con otro número
numero = 2 - 2     # Resta normal entre dos números
numero -= 2        # Resultado de restar a si mismo con otro número
numero = 2 * 2     # Multiplicación entre dos números
numero *= 2        # Multiplicación de si mismo con otro número
numero = 2 / 2     # División entre dos números
numero /= 2        # División de si mismo con otro número
numero = 2**2      # Un número elevado a otro
numero **= 2       # Si mismo elevado a otro número
numero = 2 % 2     # Para conocer el resto de la division (muy util para saber si un número es par o impar, el resto de cualquier número entre 2 puede dar o 0 o 1, si da 0 es par, 1 impar)
numero %= 2        # El resto de la división de si con otro número
numero = 2 // 2    # Al contrario que %, este devuelve la parte entera de la división
numero //= 2       # La parte entera de la división de si con otro número

# Conversión de tipos
"""
    Podemos usar la conversion para pasar de un tipo a otro
"""
enteroOdoble = int(12.34)             # Almacena el número 12. Qué pasa con .34? Al ser un entero se descarta la parte decimal
print(enteroOdoble)
enteroOdoble = int("1234")            # Convertimos una cadena de texto a número. POR DEFECTO ES EN BASE DECIMAL
print(enteroOdoble)
enteroOdoble = int("10011010010",2)   # Con el segundo parámetro indicamos en que base está en binario
print(enteroOdoble)
enteroOdoble = int("0o2322", 8)       # Indicamos que la base es octal (JODER SI LO USAS)
print(enteroOdoble)
enteroOdoble = int("0x4D2",16)        # Base hexadecimal
print(enteroOdoble)

# También vale para el resto de tipos MENOS las conversiones de cadenas en otra base
floatOlong = float(1234)              # Añade al final parte decimal, en este caso sería 1234.0
print(floatOlong)
floatOlong = float("12.34")
print(floatOlong)
"""floatOlong = float("0o2322", 8)  ---> NO FUNCIONARÍA
print(floatOlong)"""
complejo = complex(1234)
print(complejo)

# Entrada por teclado
"""
    Es importante aclarar que la funcion input() da como resultado solamente cadenas de texto, por lo que siempre habrá que aplicarle una conversión de tipo
"""
enteroOdoble = int(input("Introduce un entero: "))
print(f"Tu entero es: {enteroOdoble}")
floatOlong = float(input("Ahora un número con decimales: "))
print(f"Tu número con decimales es: {floatOlong}")


#####
#           Para que podemos usar los numéricos?
#####
"""
    Tampoco hace falta echarle mucha imaginación, son número, po pa cosas de números
"""


#####
#       Repaso de funciones vistas
#####

# Funcion print
"""
    La usamos para mostrar por terminal (u otra salida que veremos más adelante) variables, cadenas de texto, arrays, objetos...... Basicamente lo que queramos
"""
print("Cadena de texto normal")         # Saca por pantalla el texto entre las comillas
print(enteroOdoble)                     # Saca por pantalla el valor de la variable
print("Otra cadena",enteroOdoble)       # Muestra cada cosa dentro de los parentesis separados con un espacio normal (puedes poner tantos argumentos como quieras)
print("Cadena pegada a otra", end='')   # Al poner el parámetro end=, en lugar de acabar con \n (salto de linea normal) acabará con el caracter que le indiques entre las comillas '', vacio es para indicar que no ponga nada
print("Estoy pegado a la de arriba y acabo distinto tambien",end='?') # Hacemos que acabe con el signo ?
print()                                 # Si lo dejamos vacio solo mete un salto de línea


# Funcion input
"""
    Con ella podemos interactuar con el programa.
    Es importante saber que es una función bloqueante, hasta que no se le de al "enter" no continuará el programa.
    Otra cosa importante es que solo devuelve cadenas de texto, si queremos usarla para números, debemos convertir adecuadamente.
    Tiene un parámetro opcional, si dentro de los paréntesis ponemos una cadena de texto, esta se mostrará por pantalla antes de pedir la entrada del usuario.
"""
input("Para continuar presiona \"enter\" dos veces")    # Muestra un mensaje y espera una entrada por teclado
input()                                                 # No muestra nada pero si espera la entrada igual


# Funcion type
"""
    Es una funcion realmente útil. La podemos usar para saber el tipo de una variable.
"""
unNumero = 123
print("Tipo de la variable unNumero: ", type(unNumero))
unFloat = 123.4
print("Tipo de la variable unFloat: ", type(unFloat))

print("Hasta aquí la lección de datos SIMPLES")