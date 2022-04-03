numero = int(input("De cuanto el triangulo"))

cadena = ""

for i in range(numero):
    for j in range(i + 1):
        cadena = cadena + "* "
    cadena = cadena + "\n"

print(cadena)
