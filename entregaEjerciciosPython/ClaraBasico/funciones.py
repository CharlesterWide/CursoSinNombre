# Ejercicio 1, Calcular Pi
def getPi(itera):
    itera = itera * 1000000
    k = 1
    pi = 0
    for i in range(itera):
        if i%2 == 0:
            pi = pi + (4/k)
        else:
            pi = pi - (4/k)
        k = k + 2
    return pi
# Ejercicio 2, El área de una circunferencia, la longitud del perímetro y el volumen de la esfera de radio R
def getCircunferencia(radio,pi=3.14):
    circunferencia = {
        'radio' : radio,
        'longitud': 2 * pi * radio,
        'area': pi * (radio**2),
        'volumen': (4/3) * (pi * (radio**3))
    }
    return circunferencia
# Ahora strings y listas
# Ejercio 3, un correo
def usuario(mail):
    info = mail.split("@") #devuelve un array con en cada posicion las palabras separadas por el elemento puesto
    email = {
        'usuario' : info[0],
        'dominio' : info[1]
    }
    return email
# Ejercicio 4, a una lista
#he sacado la funcion list() de aqui: https://www.delftstack.com/es/howto/python/split-string-to-a-list-of-characters/
def lista(email):
    caracteres = list(email['usuario'])
    return caracteres
# Bucles
# Ejercico 5, el triangulo de números
def getTriangulo(altura):
    numeros = ""
    for i in range(1,altura+1):
        for j in range(1,i+1):
            numeros = numeros + str(j)
        numeros = numeros + "\n"
    return numeros

# Ejercicio 6, ahora en versión piramidal!
def getPiramide(lineas):
    caden = ""
    for fila in range(1,lineas + 1):
        for esp in range(1,(lineas - fila) + 1):
            caden = caden + " "
    
        for dec in range(fila, 0,-1):
            caden = caden + str(dec)
        
        for inc in range(2, fila+1 ,1):
            caden = caden + str(inc)

        caden = caden + "\n"
    return caden
# Ejercicio 7, salimos de aquí
def salir():
    palabra = ''
    while palabra != "salir":
        palabra = input("Introduzca una palabra o frase (solo podra salir si escribe 'salir' y todo lo que escriba sera puesto en minuscula, sino lo estaba): ")
        palabra = palabra.lower()
        print(f"Ha escrito: {palabra}")


if __name__ == "__main__":
    numIteraciones = int(input("Por favor, introduce un numero para aproximar pi: "))
    pi = getPi(numIteraciones)
    print(f"La aproximacion de pi con {numIteraciones} iteraciones ha sido: {pi}")

    radio = int(input("Por favor, introduce ahora el radio de una circunferencia: "))
    circunferencia = getCircunferencia(radio,pi)
    print(f"La longitud de la circunferencia de radio {circunferencia['radio']} es: {circunferencia['longitud']}")
    print(f"El area de la circunferencia de radio {circunferencia['radio']} es: {circunferencia['area']}")
    print(f"El volumen de la circunferencia de radio {circunferencia['radio']} es: {circunferencia['volumen']}")

    mail = input("Introduzca su correo electronico en formato 'usuario'@'dominio': ")
    email = usuario(mail)
    print(f"El usuario es {email['usuario']} y el dominio es {email['dominio']}")

    caracteres = lista(email)
    print(f"Este es el array caracteres: {caracteres}")

    lineas = int(input("Introduzca ahora el numero de lineas que desea ver: "))
    semiPiramide = getTriangulo(lineas)
    print(semiPiramide)

    print("Ahora en forma de piramide!")
    piramide = getPiramide(lineas)
    print(piramide)

    salir()