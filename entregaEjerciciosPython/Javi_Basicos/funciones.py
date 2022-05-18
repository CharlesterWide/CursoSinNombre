def calcularPi(numero):
    numero = (numero*100000)
    k = 1
    Pi = 0

    for i in range(numero):
        if i%2 == 0:
            Pi = Pi + (4/k)
        else:
            Pi = Pi - (4/k)
        k = k + 2

    return Pi

def calcularParametros(radio):
    longitud = 2 * 3.14 * radio
    area = 3.14 * (radio**2)
    volumen = (4 * (3.14 * (radio**3))) / 3

    Circunferencia = {
        'Radio' : radio,
        'Longitud' : longitud,
        'Area' : area,
        'Volumen' : volumen
    }

    return Circunferencia

def mostrarCorreo(correo):
    cadenas = correo.partition('@')
    usuario = cadenas[0]
    dominio = cadenas[2]
    Email = {
        'Usuario' : usuario,
        'Dominio' : dominio
    }

    return Email

def stringALista(frase):
    letra = ''
    usua = ""
    usua2 = ""
    cont = 0
    while cont < len(frase):
        usua = frase[cont] + ", "
        usua2 = usua2 + usua
        cont = cont + 1
    return usua2

def trianguloNumeros(altura):
    numeros = ""
    for i in range(1,altura+1):
        for j in range(1,i+1):
            numeros = numeros + str(j)
        numeros = numeros + "\n"
    return numeros

def piramideNumeros(numer):
    caden = ""
    for fila in range(1,numer + 1):
        for esp in range(1,(numer - fila) + 1):
            caden = caden + " "
 
        for dec in range(fila, 0,-1):
            caden = caden + str(dec)
    
        for inc in range(2, fila+1 ,1):
            caden = caden + str(inc)

        caden = caden + "\n"

    return caden

def convierteFrase():
    palabra = ""
    while palabra != "salir":
        palabra = input("Escribe una palabra: ")
        palabra = palabra.lower()
        print(palabra)
        if(palabra=="salir"):
            exit(1)

if __name__ == "__main__":
    print("Ejercicio Pi")
    numero = int(input("Introduce el numero: "))
    print(f"Su aproximacion a Pi es: {calcularPi(numero)}")

    print("Ejercicio Parametros")
    radio = int(input("Introduce el radio: "))
    print(f"Sus parametros son: ", calcularParametros(radio))

    print("Ejercicio Email")
    correo = input("Introduce tu email: ")
    print(f"Los parametros de su correo son: ",mostrarCorreo(correo))

    print("Ejercicio Frase Separada")
    frase = input("Introduzca su frase: ")
    print(f"Los parametros de su frase son: ",stringALista(frase))

    print("Ejercicio Triangulo")
    altura = int(input("Introduce la altura del triangulo: "))
    print(trianguloNumeros(altura))

    print("Piramide de numeros")
    numer = int(input("Introduce la altura del triangulo: "))
    print(piramideNumeros(numer))

    print("Ejercicio Frase")
    convierteFrase()





    