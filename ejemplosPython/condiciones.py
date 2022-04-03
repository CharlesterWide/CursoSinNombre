manzanas = 10

manzanas = manzanas - 1

if manzanas == 10:
    manzanas = manzanas - 1
elif manzanas < 10:
    manzanas = manzanas + 1
else:
    manzanas = 10

print(manzanas) 

if manzanas == 10 or manzanas != 20:
    manzanas = manzanas - 1
elif manzanas >= 5 and manzanas < 9:
    while manzanas < 10:
        manzanas = manzanas + 1
else:
    manzanas = 10

print(manzanas)

lista = ['a','b','c','s']

for i,valor in enumerate(lista):
    print(i,valor)

diccionario = {
    'valor1': 1,
    'valor2': 2,
    'valor3': 3
}

for valor in diccionario.keys():
    print(valor)

for valor in diccionario.values():
    print(valor)

for (clave, valor) in diccionario.items():
    print(clave,valor)

print(range(10))
for i in range(10):
    print(i)

for i in range(10,-10,-1):
    print(i)

letra = ''

while letra != 'f':
    letra = input("Mete una letra: ")

sumador = 0

while sumador < 10:
    sumador = sumador + 1

while sumador > 0:
    sumador = sumador - 1
    if sumador == 5:
        continue
    elif sumador < 5:
        break
    else:
        pass
        print(sumador)

