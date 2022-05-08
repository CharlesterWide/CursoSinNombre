#Ejercicio 1

def calculoPi(numero):
    numero *= 100000
    
    K = 1
    Pi = 0

    for i in range(numero):
        if(i%2 == 0):
            Pi = Pi + 4/K
        if(i%2 != 0):
            Pi = Pi - 4/K
        K = K +2

    return Pi


#Ejercicio 2

def calculoCircunferencia(Radio, Pi= 3.1416):
    Longitud = 2*Pi*Radio
    Área = Pi*Radio**2
    Volumen = 4*(Pi*Radio**3)/3

    Circunferencia = {
    'Radio'    : Radio,
    'Longitud' : Longitud,
    'Área'     : Área,
    'Volumen'  : Volumen
    }

    return Circunferencia 

#Ejercicio 3

def correoElectronico(Correo):
    Array = Correo.split('@')                   

    Usuario = Array[0]                          
    Dominio = Array[1]

    Email = {
        'Usuario'  : Usuario,
        'Dominio' : Dominio
    }

    return Email

#Ejercicio 4

def nombreUsuario(Usuario):
    listaCaracteres = list(Usuario)

    return listaCaracteres


#Ejercicio 5

def altura(altura):
    
    numeros = ""
    for i in range(1,altura+1):
        for j in range(1,i+1):
            numeros = numeros + str(j)
        numeros = numeros + "\n"

    return numeros 


#Ejercicio 6

def generaUnaPiramide(numeroFilas):

    caden = ""
    for fila in range(1,numeroFilas + 1):
            for esp in range(1,(numeroFilas - fila) + 1):
                caden = caden + " "
        
            for dec in range(fila, 0,-1):
                caden = caden + str(dec)
            
            for inc in range(2, fila+1 ,1):
                caden = caden + str(inc)

            caden = caden + "\n"

    return caden


#Ejercicio 7

def palabra():
        palabra = ""
        while palabra != "salir":
            palabra = input("Escribe una palabra: ")
            palabra = palabra.lower()
            print (palabra) 


if __name__ == "__main__":

    #1
    num = int(input("numero: "))
    Pi = calculoPi(num)
    print(Pi)

    #2
    Radio = int(input("meter el radio "))
    circunferencia = calculoCircunferencia(Radio)
    print (circunferencia)

    #3
    Correo = input("correo electrónico: ")
    Email = correoElectronico (Correo)
    print (Correo)

    #4
    nombreDeUsuario = Email['Usuario']
    listaCaracteres = nombreUsuario(nombreDeUsuario)
    print (listaCaracteres)

    #5
    numero = int(input("Introduce un numero: "))
    numeros = altura (altura)
    print (numeros)

    #6
    numeroFilas = int(input("Introduce un numero: "))
    caden = generaUnaPiramide(numeroFilas)
    print (caden)


    #7
    palabra()


