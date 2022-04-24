## Ejercicios resueltos por Francisco

# Ejercicio 1, Calcular Pi
""" 
    Vamos a calcular el número Pi usando el método de Leibniz. Este es un algoritmo muy util, ya que nos permite aproximar con bastante precisión este puñetero número.
    Para este algoritmo, primero vamos a pedir por teclado un número (input()), este número lo multiplicaremos por 1000000 (cuantas más iteraciones del algoritmo, más precisión), importante, si estas usando una tostadora o 
    patata como pc, deja ese millón y multiplica solo por cien mil o diez mil, puede chuparse muchos recursos (yo he llegado a probar recorrer más de 100 mill millones y me ha tardado 10 min con un pc potente, no te recomiendo hacer esto).
    Una vez que hemos pedido y multiplicado el número, tenemos que declarar dos variables numéricas, una que será nuestra constante K y otra que será el propio numero Pi. Inicializa K a 1 y Pi a 0.
    Ahora deberás crear un bucle que va a ser para hacer el algoritmo en si. El bucle tendrá que ir desde 0 hasta el número que hemos calculado antes.
    En cada iteración del bucle deberemos comprobar si el iterador (al que llamaremos i), es par o no. Si es par, sumaremos a Pi 4/k, si es impar le restaremos 4/k.
    Una vez sumado o restado, incrementamos k en 2.
    Después de recorrer todo el bucle, muestra por pantalla el Pi obtenido.
"""

print("====== Ejercicio 1 ======")
n = int(input('Dame un número semilla para calcular Pi: '))
#n = 112             # seteo para ahorrarme el input mientras estoy trabajando los ejecicios (comentar antes de entregar)

n = n * 10000

K = 1

Pi = 0

for i in range(n):
    if i%2 == 0:
        Pi = Pi + 4/K
    else:
        Pi = Pi - 4/K
    K += 2

print(f"\nLa aproximación al número Pi es: {Pi}\n")


# Ejercicio 2, El área de una circunferencia, la longitud del perímetro y el volumen de la esfera de radio R
"""
    Con el número Pi obtenido en el ejercicio 1 ( si no lo has conseguido hacer usa 3.1416 ), vamos a calcular el área, longitud y volumen.
    Primero pedimos por teclado un radio y lo almacenamos.
    Para calcular la longitud usamos la fórmula -> longitud = 2 * pi * radio
    Para el área -> area = pi * radio^cuadrado
    Y para el volumen -> 4*( pi * radio^cubo) / 3
    Las fómulas no están escritas para Python, ten en cuenta que tendrás que escribirlas correctamente.
    Crea un diccionario llamado circunferencia que almacene los cuatro datos, el radio, longitud, área y volumen y lo enseñas por pantalla
"""

print("====== Ejercicio 2 ======")
R = int(input('Dame radio de la circunferencia: '))
#R = 5                  # seteo para ahorrarme el input mientras estoy trabajando los ejecicios (comentar antes de entregar)

longitud = 2 * Pi * R

area = Pi * R**2

volumen = 4 * ( Pi * R**3 ) / 3

circunferencia = {
    'radio' : R,
    'longitud' : longitud,
    'area' : area,
    'volumen' : volumen
}

for (clave, valor) in circunferencia.items():
    print(clave + ":", "{0:.2f}".format(valor))
print()

# Ahora strings y listas
# Ejercio 3, un correo
"""
    Se pedirá por teclado un email y tendremos que almacenar en un diccionario separados el usuario y el dominio.
    El formato de todo mail es "usuario"@"dominio", por lo que usaremos las funciones de los string que nos permitan separar por un caracter en... (continua tu que este es fácil). Recuerda que la funcion que debes usar 
    devuelve una lista con todos los cachos que encuentre separados por el caracter que quieras, luego deberás acceder a las posiciones de la lista para extraer lo que quieres almacenar.
    El diccionario se llamará email y solo contendrá las dos cosas por separado, muestralo por pantalla.
"""

print("====== Ejercicio 3 ======")
email = {
    'usuario' : "",
    'dominio' : ""
}

correo = input("\n· Introduce un email \n· (no voy a programar 200 verificaciones de que el correo sea correcto\n asique ajustate al formato ==> usuario@dominio ) : ")
#correo = "pepe@gmail.com"   # seteo para ahorrarme el input mientras estoy trabajando los ejecicios (comentar antes de entregar)


lista = correo.split('@')

i = 0
for e in email.keys():
    email[e] = lista[i]
    i += 1

for (clave, valor) in email.items():
    print(clave + ":", valor)
print()


# Ejercicio 4, a una lista
""" 
    Vamos a coger el usuario del email anterior ( si no lo tienes, crea un string inicializado en "abcdefg") y vamos a almacenar todos sus caracteres por separado en una lista llamada caracteres.
    Muestra esa lista por pantalla.
    Se puede hacer de muchas maneras esto, con funciones ya existentes o con bucles, haz lo que más cómodo veas.
"""

print("====== Ejercicio 4 ======")

caracteres = []

for caracter in email['usuario']:
    caracteres.append(caracter)

for i,c in enumerate(caracteres):
    print("[ ", i, "=> ", c, " ]")
print()


# Bucles
# Ejercico 5, el triangulo de números
"""
    Pediremos por teclado un número y tendremos que dibujar un triangulo de tantas lineas como el número que se haya indicado.
    Cada línea estará formada por números que van desde el 1 hasta el número de linea que es.
    Por ejemplo, metemos por teclado el 5, el triangulo deberá ser:
    1
    12
    123
    1234
    12345
"""

print("====== Ejercicio 5 ======")

F = int(input('Induca el número de filas del triángulo a dibujar: '))
#F = 5                  # seteo para ahorrarme el input mientras estoy trabajando los ejecicios (comentar antes de entregar)

for i in range(F):
    for j in range(i + 1):
        print((j + 1), end="")
    print()

print()

# Ejercicio 6, ahora en versión piramidal!
""" 
    Así es, la puñetera piramide. Es una extensión de lo anterior, solo que ahora tenemos lado izquierdo. El lado izquierdo en un espejo del derecho.
    El ejemplo con el 5:
        1
       212
      32123
     4321234
    543212345
    Date cuenta que ahora tenemos "espacios blancos" en el lado izquierdo que tenemos que respetar y que en el centro solo hay un número, que si lo haces sin pensar en el centro tendrás siempre 11.
"""

print("====== Ejercicio 6 ======")

F = int(input('Induca el número de filas de la pirámide a dibujar: '))
#F = 5                  # seteo para ahorrarme el input mientras estoy trabajando los ejecicios (comentar antes de entregar)

izda = []

for i in range(F):
    
    cont = 0
    for k in range(F - 1):
        if ((F-1)-i) > cont:
            izda.append(" ")
            cont += 1
        else:
            izda.append(F-k)
    
    for ei in izda:
        print(ei, end="")

    izda.clear()

    for j in range(i + 1):
        print((j + 1), end="")

    print()

print()

# Ejercicio 7, salimos de aquí
"""
    Como último ejercicio, vamos a hacer un bucle que pida por teclado al usuario una frase/palabra. Nos aseguraremos de transformar lo introducido a minusculas.
    Todo lo que pongamos será escrito como un eco en la pantalla y solo saldremos del bucle si lo introducido es la palabra "salir"
"""

print("====== Ejercicio 7 ======")

booleano = True

while booleano:

    palabra = input("Escribe una frase o palabra: ")

    palabra = palabra.lower()

    print(palabra)

    if palabra == "salir":
        booleano = False

print()