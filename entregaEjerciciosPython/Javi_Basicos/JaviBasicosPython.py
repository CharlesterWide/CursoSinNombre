
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

numero = int(input("Introduce el numero: "))
numero = (numero*100000)
k = 1
Pi = 0

for i in range(numero):
    if i%2 == 0:
        Pi = Pi + (4/k)
    else:
        Pi = Pi - (4/k)
    k = k + 2

print(f"El resultado de Pi es: {Pi}")

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

radio = int(input("Introduce el radio: "))
longitud = 2 * Pi * radio
area = Pi * (radio**2)
volumen = (4 * (Pi * (radio**3))) / 3

Circunferencia = {
    'Radio' : radio,
    'Longitud' : longitud,
    'Area' : area,
    'Volumen' : volumen
}

print(Circunferencia)

# Ahora strings y listas
# Ejercio 3, un correo
"""
    Se pedirá por teclado un email y tendremos que almacenar en un diccionario separados el usuario y el dominio.
    El formato de todo mail es "usuario"@"dominio", por lo que usaremos las funciones de los string que nos permitan separar por un caracter en... (continua tu que este es fácil). Recuerda que la funcion que debes usar 
    devuelve una lista con todos los cachos que encuentre separados por el caracter que quieras, luego deberás acceder a las posiciones de la lista para extraer lo que quieres almacenar.
    El diccionario se llamará email y solo contendrá las dos cosas por separado, muestralo por pantalla.
"""
correo = input("Introduce tu email: ")
cadenas = correo.partition('@')
usuario = cadenas[0]
dominio = cadenas[2]
Email = {
    'Usuario' : usuario,
    'Dominio' : dominio
}

print(Email)


# Ejercicio 4, a una lista
""" 
    Vamos a coger el usuario del email anterior ( si no lo tienes, crea un string inicializado en "abcdefg") y vamos a almacenar todos sus caracteres por separado en una lista llamada caracteres.
    Muestra esa lista por pantalla.
    Se puede hacer de muchas maneras esto, con funciones ya existentes o con bucles, haz lo que más cómodo veas.
"""

letra = ''
usua = ""
usua2 = ""
cont = 0
while cont < len(usuario):
    usua = usuario[cont] + ", "
    usua2 = usua2 + usua
    cont = cont + 1
print(f"Los caracteres separados del usuario son: {usua2}")


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

altura = int(input("Introduce la altura del triangulo: "))
numeros = ""
for i in range(1,altura+1):
    for j in range(1,i+1):
        numeros = numeros + str(j)
    numeros = numeros + "\n"

print(numeros)

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

lineas = int(input("Introduce la altura de la piramide: "))
k=0
cuenta=0
cuenta2=0
for i in range(1,lineas+1):
    for j in range(1,(lineas-i)+1):
        print(" ",end="")
        cuenta+=1
    while k!=((2*i)-1):
        if cuenta<=lineas-1:
            print(i+k,end="")
            cuenta+=1
        else:
            cuenta2+=1
            print(i+k-(2*cuenta2),end="")
        k+=1
    k=cuenta=cuenta2=0
    print()




# Ejercicio 7, salimos de aquí
"""
    Como último ejercicio, vamos a hacer un bucle que pida por teclado al usuario una frase/palabra. Nos aseguraremos de transformar lo introducido a minusculas.
    Todo lo que pongamos será escrito como un eco en la pantalla y solo saldremos del bucle si lo introducido es la palabra "salir"
"""
frase = ""
while frase!="salir":
    frase = input("Introduce una frase en mayusculas: ")
    frase = frase.lower()
    if frase == "salir":
        print("Saliendo del programa, adios")
    else:
        print(frase)
