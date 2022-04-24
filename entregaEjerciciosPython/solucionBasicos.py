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
print("====================================")
print("Ejercicio 1: calculando el número PI")
rango = int(input(
    "Introduce el número de veces que se hará el algoritmo (por un millon): ")) * 1000000
k = 1
pi = 0

for i in range(rango):
    if i % 2 == 0:
        pi += 4/k
    else:
        pi -= 4/k

    k += 2
print(f"La aproximación obtenida después de hacer {rango} iteraciones del número PI es: {pi}")

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
print("====================================")
print("Ejercicio 2: El cículo y sus características")
radio = int(input("Radio de la circunferencia: "))
circunferencia = {
    'radio': radio,
    'longitud': 2 * pi * radio,
    'area': pi * radio**2,
    'volumen': 4/3 * pi * radio**3
}
print(f"La circunferencia tiene:\n"+
      f"Radio: {circunferencia['radio']}\n"+
      f"Longitud: {circunferencia['longitud']}\n"+
      f"Área: {circunferencia['area']}\n"+
      f"Volumen: {circunferencia['volumen']}")

# Ahora strings y listas
# Ejercio 3, un correo
"""
    Se pedirá por teclado un email y tendremos que almacenar en un diccionario separados el usuario y el dominio.
    El formato de todo mail es "usuario"@"dominio", por lo que usaremos las funciones de los string que nos permitan separar por un caracter en... (continua tu que este es fácil). Recuerda que la funcion que debes usar 
    devuelve una lista con todos los cachos que encuentre separados por el caracter que quieras, luego deberás acceder a las posiciones de la lista para extraer lo que quieres almacenar.
    El diccionario se llamará email y solo contendrá las dos cosas por separado.
"""
print("====================================")
print("Ejercicio 3: Separando un email")
correo = input("Introduce un email: ")
correo = correo.split('@')
email = {
    'usuario': correo[0],
    'dominio': correo[1]
}


# Ejercicio 4, a una lista
""" 
    Vamos a coger el usuario del email anterior ( si no lo tienes, crea un string inicializado en "abcdefg") y vamos a almacenar todos sus caracteres por separado en una lista llamada caracteres.
    Muestra esa lista por pantalla.
    Se puede hacer de muchas maneras esto, con funciones ya existentes o con bucles, haz lo que más cómodo veas.
"""
print("====================================")
print("Ejercicio 4: Los carácteres del usuario")
caracteres = list(email['usuario'])
print("La lista de carácteres del usuario es: ",caracteres)


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
print("====================================")
print("Ejercicio 5: Triangulo de números")
tamaño = int(input("Di el tamaño del triangulo: "))
for i in range(1, tamaño+1):
    for j in range(1,i+1):
        print(j,end='')
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
print("====================================")
print("Ejercicio 6: La pirámide de números")
tamaño = int(input("Di el tamaño de la pirámide: "))
for i in range(1, tamaño+1):
    # Debemos comprobar que lo que toca sea 
    for j in range(tamaño+1,1,-1):
        if j > i:
            print(" ",end='')
        else:
            print(j,end='')
    # El lado derecho es igual que antes
    for j in range(1,i+1):
        print(j,end='')
    print()


# Ejercicio 7, salimos de aquí
"""
    Como último ejercicio, vamos a hacer un bucle que pida por teclado al usuario una frase/palabra. Nos aseguraremos de transformar lo introducido a minusculas.
    Todo lo que pongamos será escrito como un eco en la pantalla y solo saldremos del bucle si lo introducido es la palabra "salir"
"""
print("====================================")
print("Ejercicio 7: El bucle de salida")
frase = ""
while frase != "salir":
    frase = input("Di algo, soy como un loro (si quieres salir, dilo): ").lower()
    print(frase)