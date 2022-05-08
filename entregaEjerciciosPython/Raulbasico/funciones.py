def calcularPi (numero):

    numero = numero*1000000

    k = 1
    pi = 0

    for i in range(numero):
        if i%2 == 0:
            pi = pi + 4/k
        else:
            pi = pi - 4/k
        k = k+2
    return pi

def AreaLongiturVolumen(radio,pi=3.1416):

    diccionario ={
    'radio' : radio,
    'longitud' : 2*pi*radio,
    'area': pi*radio**2,
    'volumen' : 4*(pi * radio**3)/3
    }
    return diccionario

def DevuelveCorreo (correo):

    posicion = correo.find("@")

    aux = posicion + 1

    usuario = ""
    dominio = ""

    if posicion != -1:

        for i in range(posicion):
            usuario = usuario + correo[i]

        while(aux < len(correo)):
            dominio = dominio + correo[aux]
            aux = aux + 1

        email ={
            'usuario' : usuario,
            'dominio' : dominio
        }
    return email

def CaracteresPorSeparadoEmail (usuario):

    caracteres = []

    i = 0
    while i < len(usuario):
        caracteres.append(usuario[i])
        i = i+1

    return caracteres

def PiramideV1 (altura):
    
    numeros = ""
    for i in range(1,altura+1):
        for j in range(1,i+1):
            numeros = numeros + str(j)
        numeros = numeros + "\n"
    return numeros

def PiramideV2(numer):

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
    
def SalirDelJuego():
    
    salir = False
    while (salir == False):
        ayuda = input("Introduce la palabra 'salir' para escapar de aqui: ")
        ayuda = ayuda.lower()
        if(ayuda == "salir"):
            salir = True


if __name__ == "__main__":
    print(calcularPi(3))
    print(AreaLongiturVolumen(4))
    print(DevuelveCorreo("raulfdez@uma"))
    print(CaracteresPorSeparadoEmail("raulfdez"))
    print(PiramideV1(5))
    # sale lo que quiere el siguiente
    print(PiramideV2(3))
    SalirDelJuego()


