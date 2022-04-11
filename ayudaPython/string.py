"""
    Segundo archivo de ayuda de python. Vamos a ver el tipo string, las cadenas de caracteres, el tipo texto o "las frases"
"""

# Declaración del string

frase = "Esto es una frase"     # Aunque no es obligatorio, es como norma general poner, cuando es solo un caracter, comillas simples y
caracter = 'a'                  # usar las dobles comillas para cuando es más de uno
print(frase,caracter)

# Concatenar strings (juntar o sumar)
frase = "Esta es la primera parte"
frase = frase + " esto la segunda"
print(frase)
frase1 = "Primera parte "
frase2 = "Segunda parte"
frase = frase1 + frase2
print(frase)

""" Es fácil ver que se pueden hacer operaciones de suma simples, pero ningún otro operador matemático funciona (-,*,**) """

# Formación compleja
numero = 5
frase = f"He declarado el número {numero}"  # Si delante de las comillas ponermos la letra 'f', dentro de las comillas podemos poner los corchetes {} para introdicir variables
print(frase)                                # o incluso funciones

# ejemplo con función
nuevaFrase = "abcdef"
frase = f"Aquí meto una función y veo una función nueva {nuevaFrase.capitalize()}"
print(frase)

### Funciones del string ###
""" Vamos a ver muchas funciones innecesarias para lo que realmente vamos a hacer, muchas las he omitido"""
frase = "frase de ejemplo para todo este bloque"
frase = frase.capitalize()                  # La primera letra en mayúscula
print(frase)
frase = frase.casefold()                    # Todo a minusculas para más fácil comparación
print(frase)
frase = frase.center(50,'*')                # Deveulve una cadena centrada del tamaño especificado como primer parámetro, si es más pequeño, rellena los laterales con el carácter indicado en el segundo
print(frase)
numero = frase.count('*')                   # Devuelve el número de veces que aparece un carácter o una frase dentro del string
print(numero)
# frase = frase.encode() No es necesaria: codifica el string en el formato que indiques
booleano = frase.endswith('*')              # Comprueba si el string acaba con el carácter o frase indicado
print(booleano)
#frase = frase.expandtabs()  No necesaria (NN): Cambia el carácter de tabulador por el número de espacios indicados
numero = frase.find("todo")                 # Devuelve la posición donde encuentre la primera coincidencia, si no lo encuentra, devuelve -1
print(numero)
#frase = frase.format() NN, al menos por ahora
#frase = frase.format_map(map) NN, igual que arriba
numero = frase.index("todo")                # Similar al find, pero devuelve Error en lugar de -1 (recomiendo la find mejor)
print(numero)
booleano = frase.isalnum()                  # Comprueba si lo que hay en el string es un número
print(booleano)
booleano = frase.isalpha()                  # Comprueba si todos los caracteres son alfanuméricos (no contiene caracteres especiales)
print(booleano)
booleano = frase.isascii()                  # Comprueba si todos los caracteres están dentro del estandar ASCII (preguntame si no sabes que es esto)
print(booleano)
booleano = frase.isdecimal()                # Comprueba si es un número Y que tenga decimales (float o long)
print(booleano)
booleano = frase.isdigit()                  # Comprueba si todos los caracteres son digitos (no haya nada que no sea un número)
print(booleano)
#booleano = frase.isidentifier() NN: Para saber si es una palabra clave de python
booleano = frase.islower()                  # Comprueba si todo está en minus
print(booleano)
booleano = frase.isnumeric()                # Igual que isdigit
booleano = frase.isprintable()              # Que todos los caracteres puedan ser mostrados por pantalla
print(booleano)
#booleano =frase.isspace() NN: Todo son espacios
#booleano = frase.istitle() NN: Empiece por mayusculas seguido de todo minuscula (como demasiado especifica esta funcion)
booleano = frase.isupper()                  # Todo en mayus
print(booleano)
frase1 = "Extra 1"
frase2 = "Extra 2"
frase3 = "Extra 3"
frase = '.'.join([frase1,frase2,frase3])    # Otra forma de llamar a las funciones es directamente sobre un string entre comillas, sin usar una variable. La funcion "join" une todos los strings dentro del array como argumento usando como separador el string que se usa para la llamada
print(frase)
frase = frase.ljust(30,'*')                 # Como la funcion center, pero solo por la izquierda       
print(frase)
frase = frase.lower()                       # Toda la frase a minusculas
print(frase)
#frase = frase.lstrip() NN: Ni idea de que hace la verdad
#frase = frase.maketrans(x) NN: Para traducir (raro que usemos esto)
tupla = frase.partition(" ")                # Devuelve una TUPLA de todos los strings que pueda encontrar separados por el caracter o frase pasado como argumento
print(tupla)
frase = frase.removeprefix("extra")         # Elimina, si lo encuentra, el incio del string si empieza por lo indicado
print(frase)
frase = frase.removesuffix("***")           # Lo mismo pero al final
print(frase)
frase = frase.replace("extra", "patata")    # Reemplaza todo lo que encuentre igual que el primer argumento con el segundo argumento
print(frase)
array = frase.split(' ')                    # Igual que el partition pero devolviendo un array
print(array)
frase = frase.upper()                       # Todo a mayusculas
print(frase)

""" Me he saltado algunas funciones, pero o son muy tontas o hacen similar a otras pero desde la dereca """

### Podemos acceder a un caracter específico del string ###
""" Los string no dejan de ser una lista de caracteres, por lo que podemos tanto acceder a una posición específica como iterarlo """
frase = "abcdefghijklmnñopqrstuvwxyz1234567890*!<> +-·\"$%&/()=?¿¡"  # Usando la barra lateral "\" podemos poner carácteres especiales como las comillas o retorno de carro
print(frase[15])
# frase[15] = '~' SOLO PODEMOS ACCEDER PARA LEER PERO NO PARA MODIFICAR EL VALOR

for caracter in frase:                      # Podemos recorrer todo el string con un bucle for
    print(caracter)

contador = 0
caracter = ''
while caracter != '<' and contador < len(frase):        # La funcion len() devuelve el número de caracteres que tiene el string
    caracter = frase[contador]
    contador = contador + 1
print(contador, caracter, len(frase))


""" Con esto acabamos los strings, habrá cosas que me he dejado en el tintero, pero o no son necesarias o será muy raro que las usemos"""