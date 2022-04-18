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
print("Ejercicio 1")
num = int(input("Introduce un numero: "))
num = num * 1000000
k = 1
Pi = 0
for i in range(num + 1):
    if i % 2 == 0:
        Pi = Pi + 4/k
    else:
        Pi = Pi - 4/k
    k = k + 2
print(Pi)


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
print("Ejercicio 2")
rad = float(input("Introduce el radio: "))
lon = 2 * Pi * rad
ar = Pi * rad ** 2
vol = 4 * (Pi * (rad ** 3)) / 3
circunferencia = {
    'radio' : rad,
    'longitud' : lon,
    'area' : ar,
    'volumen' : vol
}
print(circunferencia)


# Ahora strings y listas
# Ejercio 3, un correo
"""
    Se pedirá por teclado un email y tendremos que almacenar en un diccionario separados el usuario y el dominio.
    El formato de todo mail es "usuario"@"dominio", por lo que usaremos las funciones de los string que nos permitan separar por un caracter en... (continua tu que este es fácil). Recuerda que la funcion que debes usar 
    devuelve una lista con todos los cachos que encuentre separados por el caracter que quieras, luego deberás acceder a las posiciones de la lista para extraer lo que quieres almacenar.
    El diccionario se llamará email y solo contendrá las dos cosas por separado, muestralo por pantalla.
"""
print("Ejercicio 3")
mail = input ("Introduce un email: ")
pos = mail.find("@")
us = ""
dom = ""
for car in range(pos):
    us += mail[car]
for i in range(pos+1,len(mail),1):
    dom += mail[i] 
email = {
    'usuario' : us,
    'dominio' : dom
}
print(email)


# Ejercicio 4, a una lista
""" 
    Vamos a coger el usuario del email anterior ( si no lo tienes, crea un string inicializado en "abcdefg") y vamos a almacenar todos sus caracteres por separado en una lista llamada caracteres.
    Muestra esa lista por pantalla.
    Se puede hacer de muchas maneras esto, con funciones ya existentes o con bucles, haz lo que más cómodo veas.
"""
print("Ejercicio 4")
caracteres = [*range(len(us))]
for c in caracteres:
    caracteres[c] = us[c]
print(caracteres)


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
print("Ejercicio 5")
numero = int(input("Introduce un numero: "))
cadena = ""
for fil in range(1,numero + 1):
    for col in range(1, fil + 1):
        cadena = cadena + str(col)
    cadena = cadena + "\n"
print(cadena)


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
print("Ejercicio 6")
numer = int(input("Introduce un numero: "))
caden = ""
for fila in range(1,numer + 1):
    for esp in range(1,(numer - fila) + 1):
        caden = caden + " "
 
    for dec in range(fila, 0,-1):
        caden = caden + str(dec)
    
    for inc in range(2, fila+1 ,1):
        caden = caden + str(inc)

    caden = caden + "\n"
print(caden)

# Ejercicio 7, salimos de aquí
"""
    Como último ejercicio, vamos a hacer un bucle que pida por teclado al usuario una frase/palabra. Nos aseguraremos de transformar lo introducido a minusculas.
    Todo lo que pongamos será escrito como un eco en la pantalla y solo saldremos del bucle si lo introducido es la palabra "salir"
"""
print("Ejercicio 7")
palabra = ""
while palabra != "salir":
    palabra = input("Escribe una palabra: ")
    palabra = palabra.lower()
    print(palabra)