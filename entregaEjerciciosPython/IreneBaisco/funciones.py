"""Calcular Pi"""
def CalcularPi(numero):
    multiplicacion = numero * 1000000
    k = 1
    pi = 0

    for i in range (multiplicacion):
        if i % 2 == 0:
            pi += 4/k
        
        else:
            pi -= 4/k

        k += 2

    return pi

"""Circuferencia"""
def Circuferencia(radio):
    longitud = 2 * 3.1416 * radio
    area = 3.1416 * (radio)**2
    volumen = 4 * (3.1416 * (radio)**3)/3

    circunferencia = {
        'Longitud' : longitud,
        'Area'     : area,
        'Volumen'  : volumen
    } 
    return circunferencia 

"""E-mail"""
def Email(correo):
    tupla = correo.partition("@")
    email = {
        'Usuario' : tupla[0],
        'Dominio' : tupla[2]
    }
    return email['Usuario'] 
    return email['Dominio'] 

"""Lista email"""
def ListaEmail(usuario):
    caracteres=list(usuario)
    return usuario

"""Triangulo izquierda"""
def Triangulito(altura):
    numeros = ""
    for i in range(1,altura+1):
        for j in range(1,i+1):
            numeros = numeros + str(j)
        numeros = numeros + "\n"
    return numeros

"""Piramide"""
def Piramide(numer):
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

"""Salir"""
def QuieroSalir(frase):
    frase=""
    while frase!='salir':
        frase = frase.lower()            
        if frase == "salir":
            print('Bye Bye')
        else:
            return frase

if __name__ == """__main__""":
    numero = int(input('escribe un numero, por favor: '))
    print(CalcularPi(numero))

    radio = int(input('dime el radio de la circunferencia: '))
    print(Circuferencia(radio))

    correo = input('Escribe un email: ')
    email = Email(correo)
    print(email)

    print(ListaEmail(email['Usuairo']))

    altura = int(input("Introduce la altura del triangulo: "))
    print(Triangulito(altura))

    numer = int(input("Introduce un numero: "))
    print(Piramide(numer))

    frase = input ("introduce palabra o frase: ")
    print(QuieroSalir(frase))