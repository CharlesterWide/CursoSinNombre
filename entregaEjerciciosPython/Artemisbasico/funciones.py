"calculo pi"

def calculoPi(numero):  
    
    numero = numero * 1000000
    k = 1
    pi = 0
    for i in range(numero): 
    
        
        if i % 2 == 0: 
            pi += 4/k 
        else: 
    
            
            pi -= 4/k 
    
        
        k += 2
        
    return (pi)


"calcular circunferencia"
def calculocircunferencia(r, pi= 3.14): 
    l = 2 * pi * r
    a = pi * r**2
    v = 4*(pi*r**3)/3

    circunferencia = {'longitud' : l, 'area' : a, 'volumen': v}
    return circunferencia



"correo"
def email (mail):
    tupla = mail.partition("@") 
    email = {'usuario' : tupla[0], 'dominio' : tupla[2]}
    return email

"correo por caracter"
def email (email):
    for caracter in email['usuario']:
        return caracter

"triangulo"
def alturatriangulo (altura):
    numeros = ""
    for i in range(1,altura+1):
        for j in range(1,i+1):
            numeros = numeros + str(j)
        numeros = numeros + "\n"

    return(numeros)

"piramide"
def alturapiramide (numer):
    caden = ""
    for fila in range(1,numer + 1):
        for esp in range(1,(numer - fila) + 1):
            caden = caden + " "
    
        for dec in range(fila, 0,-1):
            caden = caden + str(dec)
        
        for inc in range(2, fila+1 ,1):
            caden = caden + str(inc)

        caden = caden + "\n"
    return(caden)

"frase"
def frase ():
    frase = ""
    while frase!="salir":
        frase = input("Introduce una frase en mayusculas: ")
        frase = frase.lower()
        if frase == "salir":
            print("Saliendo del programa, adios")
        else:
            print(frase)




if __name__ == "__main__":
    numero = int(input("introduce numero: "))
    print (calculoPi(numero))

    r = int(input("introduce radio: "))
    print (calculocircunferencia(r, pi= 3.14))

    mail = (input("introduce email: "))
    print (email (mail))

    print (email (email))

    numero = int(input("ingresa numero de filas: "))
    print (alturatriangulo (numero))

    numero = int(input("introduce el numero de lineas: "))
    print (alturapiramide (numero))

    frase = input ("introduce palabra: ")
    print (frase ())
