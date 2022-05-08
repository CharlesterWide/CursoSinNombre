"""Èjercicio 1"""
def calculaPi(numer):
    numer *= 1000000
    k = 1
    Pi = 0
    for i in range(numer + 1):
        if i % 2 == 0:
            Pi = Pi + 4/k
        else:
            Pi = Pi - 4/k
        k = k + 2
    return Pi

"""Ejercicio 2"""
def claculaCircunferencia(radio,Pi=3.1416):
    
    return {
        'radio' : radio,
        'longitud' : 2 * Pi * radio,
        'area' : Pi * radio ** 2,
        'volumen' : 4 * (Pi * (radio ** 3)) / 3
    }

"""Ejercicio 3"""
def guardaEmail(mail):
    pos = mail.find("@")
    us = ""
    dom = ""
    for car in range(pos):
        us += mail[car]
    for i in range(pos+1,len(mail),1):
        dom += mail[i] 
    return {
        'usuario' : us,
        'dominio' : dom
    }
    
"""Ejercicio 4"""
def listaEmail(us):
    caracteres = [*range(len(us))]
    for c in caracteres:
        caracteres[c] = us[c]
    return caracteres

"""Ejercicio 5"""
def triangulo(base):
    numeros = ""
    for i in range(1,base+1):
        for j in range(1,i+1):
            numeros = numeros + str(j)
        numeros = numeros + "\n"
    return numeros
"""Ejercicio 6"""
def piramide(numer):
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
"""Ejercicio 7"""
def bucle():
    palabra = ""
    while palabra != "salir":
        palabra = input("Escribe una palabra: ")
        palabra = palabra.lower()
        print(palabra)
        
if __name__ == "__main__":
    num = int(input("Introduce un numero para calcular pi: "))
    print(calculaPi(num))
    
    rad = float(input("Introduce el radio para calcular la circunferencia: "))
    print(claculaCircunferencia(rad))
    mail = input ("Introduce un email: ")
    emailSepado = guardaEmail(mail)
    print(emailSepado)
    
    print(listaEmail(emailSepado["usuario"]))
    base = int(input("Introduce la altura del triangulo: "))
    print(triangulo(base))
    numer = int(input("Introduce la altura de la piramide: "))
    print(piramide(numer))
    bucle()

