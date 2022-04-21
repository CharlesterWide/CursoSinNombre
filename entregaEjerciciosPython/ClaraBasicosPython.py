# Ejercicio 1, Calcular Pi
numero = int(input("Por favor, introduce un numero para aproximar pi: "))
numero = numero * 1000000
k = 1
pi = 0
for i in range(numero):
    if i%2 == 0:
        pi = pi + (4/k)
    else:
        pi = pi - (4/k)
    k = k + 2
print(f"La aproximacion de pi con {numero} iteraciones ha sido: {pi}")

# Ejercicio 2, El área de una circunferencia, la longitud del perímetro y el volumen de la esfera de radio R
radio = int(input("Por favor, introduce ahora el radio de una circunferencia: "))
circunferencia = {
    'radio' : radio,
    'longitud': 2 * pi * radio,
    'area': pi * (radio**2),
    'volumen': (4/3) * (pi * (radio**3))
}
print(f"La longitud de la circunferencia de radio {circunferencia['radio']} es: {circunferencia['longitud']}")
print(f"El area de la circunferencia de radio {circunferencia['radio']} es: {circunferencia['area']}")
print(f"El volumen de la circunferencia de radio {circunferencia['radio']} es: {circunferencia['volumen']}")

# Ahora strings y listas
# Ejercio 3, un correo
mail = input("Introduzca su correo electronico en formato 'usuario'@'dominio': ")
info = mail.split("@") #devuelve un array con en cada posicion las palabras separadas por el elemento puesto
email = {
    'usuario' : info[0],
    'dominio' : info[1]
}
print(f"El usuario es {email['usuario']} y el dominio es {email['dominio']}")

# Ejercicio 4, a una lista
#he sacado la funcion list() de aqui: https://www.delftstack.com/es/howto/python/split-string-to-a-list-of-characters/
caracteres = list(email['usuario'])
print(f"Este es el array caracteres: {caracteres}")

# Bucles
# Ejercico 5, el triangulo de números
lineas = int(input("Introduzca ahora el numero de lineas que desea ver: "))
for i in range(1, lineas + 1): #de 1 a +1 para eliminar la linea correspondiente al 0
    for j in range(1, i + 1):
        print(j, end = "")
    print('')

# Ejercicio 6, ahora en versión piramidal!
print("Ahora en forma de piramide!")
for i in range(1, lineas + 1): #de 1 a +1 para eliminar la linea correspondiente al 0
    cadena = ""
    for j in range(i, 1, - 1):
        cadena = cadena + str(j)
    for j in range(1, i + 1):
        cadena = cadena + str(j)
    print(cadena.center((lineas * 2)-1,' '))
    
# Ejercicio 7, salimos de aquí
palabra = ''
while palabra != "salir":
    palabra = input("Introduzca una palabra o frase (solo podra salir si escribe 'salir' y todo lo que escriba sera puesto en minuscula, sino lo estaba): ")
    palabra = palabra.lower()
    print(f"Ha escrito: {palabra}")

print("FIN DEL EJERCICIO!!!")