def aproximaPI(numero):
    numero = numero * 10000

    K = 1

    Pi = 0

    for i in range(numero):
        if i%2 == 0:
            Pi = Pi + 4/K
        else:
            Pi = Pi - 4/K
        K += 2

    return Pi

def geometriaCircunferencia(radio, Pi=3.1416):
    longitud = 2 * Pi * radio

    area = Pi * radio**2

    volumen = 4 * ( Pi * radio**3 ) / 3

    circunferencia = {
        'radio' : radio,
        'longitud' : longitud,
        'area' : area,
        'volumen' : volumen
    }

    return circunferencia

def incorporaEmail(correo):
    email = {
        'usuario' : "",
        'dominio' : ""
    }   

    lista = correo.split('@')

    i = 0
    for e in email.keys():
        email[e] = lista[i]
        i += 1

    return email

def stringALista(cadena):

    caracteres = []

    for caracter in cadena:
        caracteres.append(caracter)

    return caracteres

def imprimeTriangulo(F):
    numeros = ""
    for i in range(1,F+1):
        for j in range(1,i+1):
            numeros = numeros + str(j)
        numeros = numeros + "\n"
    return numeros

def imprimePiramide(F):
    caden = ""
    for fila in range(1,F + 1):
        for esp in range(1,(F - fila) + 1):
            caden = caden + " "
    
        for dec in range(fila, 0,-1):
            caden = caden + str(dec)
        
        for inc in range(2, fila+1 ,1):
            caden = caden + str(inc)

        caden = caden + "\n"

    return caden

def eco():

    booleano = True

    while booleano:

        palabra = input("Escribe una frase o palabra: ")

        palabra = palabra.lower()

        print(palabra)

        if palabra == "salir":
            booleano = False

    print()

if __name__ == "__main__":
    print("====== Ejercicio 1 ======")
    n = int(input('Dame un número semilla para calcular Pi: '))
    Pi = aproximaPI(n)
    print(f"\nLa aproximación al número Pi es: {Pi}\n")

    print("====== Ejercicio 2 ======")
    R = int(input('Dame radio de la circunferencia: '))
    circunferencia = geometriaCircunferencia(R, Pi)
    for (clave, valor) in circunferencia.items():
        print(clave + ":", "{0:.2f}".format(valor))
    print()

    print("====== Ejercicio 3 ======")
    correo = input("\n· Introduce un email \n· (no voy a programar 200 verificaciones de que el correo sea correcto\n asique ajustate al formato ==> usuario@dominio ) : ")
    email = incorporaEmail(correo)
    for (clave, valor) in email.items():
        print(clave + ":", valor)
    print()

    print("====== Ejercicio 4 ======")
    caracteres = caracteresDelUsuario(email)
    for i,c in enumerate(caracteres):
        print("[ ", i, "=> ", c, " ]")
    print()

    print("====== Ejercicio 5 ======")
    F = int(input('Induca el número de filas del triángulo a dibujar: '))
    numeros = imprimeTriangulo(F)    
    print(numeros)

    print("====== Ejercicio 6 ======")
    F = int(input('Indica el número de filas de la pirámide a dibujar: '))
    caden = imprimePiramide(F)
    print(caden)

    print("====== Ejercicio 7 ======")
    eco()
