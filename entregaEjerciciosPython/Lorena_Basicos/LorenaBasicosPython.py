# Ejercicios de Lorena

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

#Ejercicio1

from numpy import append


num = int(input("numero: "))
valornum = num*100000

K = 1
Pi = 0


for i in range(valornum):
    if(i%2 == 0):
        Pi = Pi + 4/K
    if(i%2 != 0):
        Pi = Pi - 4/K
    K = K +2

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

#Ejercicio2

Radio = int(input("meter el radio "))
Longitud = 2*Pi*Radio
Área = Pi*Radio**2
Volumen = 4*(Pi*Radio**3)/3

Circunferencia = {
'Radio'    : Radio,
'Longitud' : Longitud,
'Área'     : Área,
'Volumen'  : Volumen
}

print (Circunferencia)


# Ejercio 3, un correo
"""
    Se pedirá por teclado un email y tendremos que almacenar en un diccionario separados el usuario y el dominio.
    El formato de todo mail es "usuario"@"dominio", por lo que usaremos las funciones de los string que nos permitan separar por un caracter en... (continua tu que este es fácil). Recuerda que la funcion que debes usar 
    devuelve una lista con todos los cachos que encuentre separados por el caracter que quieras, luego deberás acceder a las posiciones de la lista para extraer lo que quieres almacenar.
    El diccionario se llamará email y solo contendrá las dos cosas por separado, muestralo por pantalla.
"""
#int: poner solo si quiero nº
#No poner int, sino solo input si quiero que muestre letras
#ctrl + C: cancelar el programa

#Ejercicio 3

Correo = input("correo electrónico: ")      # aqui guardo en una variable llamada correo lo que mete el usuario por teclado mostrando el texto de "correo electrónico: "

Array = Correo.split('@')                   # guardo en un array de variable con nombre Array lo que saca la funcion de string "split" que separa el string contenido en la variable "Correo" siempre que encuentre el caracter '@'

Usuario = Array[0]                          # guardo en una variable llamada Usuario el contenido de la primera posición del array de nombre Array, que sé de antemano que es el usuario del correo que metieron por teclado
Dominio = Array[1]

Email = {
    'Usuario'  : Usuario,
    'Dominio' : Dominio
}

print (Email)
        


# Ejercicio 4, a una lista
""" 
    Vamos a coger el usuario del email anterior ( si no lo tienes, crea un string inicializado en "abcdefg") y vamos a almacenar todos sus caracteres por separado en una lista llamada caracteres.
    Muestra esa lista por pantalla.
    Se puede hacer de muchas maneras esto, con funciones ya existentes o con bucles, haz lo que más cómodo veas.
"""

#Ejercicio 4


#CLS lo pondre en la termninal para borrar todo

print("============================================")
nombreDeUsuario = Email['Usuario']    # guardo en una variable nueva que llamo "nombreDeUsuario" el contenido del campo 'Usuario' del diccionario Email del ejercicio anterior
print (nombreDeUsuario)     #print para ir haciendo comprobaciones de vez en cuando

otraLista = []      # inicializo una lista (o Array) vacía donde almacenar los caracteres (o lertas) del usuario mencionado                                             
#otraLista.append(Pepe[0])

for contador in range(len(nombreDeUsuario)):        # creo un bucle for para recorrer cada letra del usuario. Contador se usa para especificar que tiene que hacer conteo de todas las letras del usuario. Con Range y len le digo que me muestre la longitud desde la primera posición de la palabra situada en "Usuario".
    otraLista.append(nombreDeUsuario[contador])     # añado la letra de la posicion "contador" de la variable nombreDeUsuario en la lista llamada otraLista
    print(otraLista[contador])                      # imprime por pantalla letra a letra con cada paso del bucle lo contenido en la lista llamada otraLista

print(otraLista)        # imprime todo el array o la lista llamada otraLista de una vez

print (len(nombreDeUsuario))


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

# Ejercicio 7, salimos de aquí
"""
    Como último ejercicio, vamos a hacer un bucle que pida por teclado al usuario una frase/palabra. Nos aseguraremos de transformar lo introducido a minusculas.
    Todo lo que pongamos será escrito como un eco en la pantalla y solo saldremos del bucle si lo introducido es la palabra "salir"
"""