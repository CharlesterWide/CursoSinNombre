""" 
    Tercer archivo de ayuda de python. Tocan las listas o arreglos, llamados array y tuplas, ambos son similares, pero con sus diferencias.
    La diferencia más importante es muy simple de entender, las tuplas son variables de solo lectura, una vez declaradas, no pueden ser modificadas.
    En este archivo, si ves alguna referencia a modificación, no es aplicable a las tuplas, cualquier otra cosa si.
"""

# Definición de array
array = [1,2,3,4,5,6]
array = [*range(7)]                 # Poniendo un asterisco delante de la función range "desempaquetamos" el range
print("Declaración de array usando range(): ",array)
array += [*range(50)]               # Al igual que con el string, podemos extender sumando más array
print("Declaración de array sumando dos array: ",array)

# Solo números?
arrayDeLetras = ['a','b','c','d','e']
arrayDeStr = ["asd","cvb","txt","csv"]

# Solo un tipo???
arrayMezclado = array + arrayDeLetras + arrayDeStr
print("Array de muchos tipos: ",arrayMezclado)

# Definicion de tuplas
tupla = (1,2,3,4)
#tupla = (*range(10)) ---> No funciona en este caso
tupla = (1,2,3,4) + (5,6,7,8)           # No la estamos modificando, estamos creando una nueva
print("Tupla declarada por suma de tuplas: ",tupla)

tupla1 = ('a','b','c','d')
tupla2 = ("txt","csv","sql","pdf")
tupla3 = (1,2,3,4)
tupla = tupla1 + tupla2 + tupla3        # Podemos seguir usando distintos tipos
print("Tupla multitipo: ",tupla)

# De tupla a array y de array a tupla (ahora tambien con range!)
""" Es importante remarcar que en python a los array se les suele llamar List (lista) """
array = list(tupla)             # Al igual que con los tipos simples, podemos hacer conversiones
tupla = tuple(array)
print("Una lista que viene de una tupla y viceversa",array,tupla)
array = list(range(10))
tupla = tuple(range(10))        # De esta forma si funciona
print("Lista y tupla transformando un range: ",array,tupla)

## Accediendo a una posición de la lista ##
""" Aunque la tupla se declara con parentesis () a la posición se accede igual que el array, con corchetes [] """
array = list(range(100))

print("Valor en la posición 0 del array: ",array[0])                 # RECUERDA QUE LAS POSICIONES EMPIEZAN EN 0 Y NO EN 1
array[0] = "aaaa"               # esto solo lo podemos hacer con los array
print("Valor en la posición 0 del array MODIFICADO: ",array[0])                 # No importa que cambiemos el tipo de dato, recuerda el tipado dinámico

print("Mostrando todos los elementos del array")
for elemento in array:
    print(elemento, end=' ')             # Recorremos todos los elemento 
print()

# Para sacar también el indice
print("Mostrando el indice junto a su elemento")
for indice,elemento in enumerate(array):        # "Transformamos" el objeto a un tipo enumerdo
    print('[',indice,',',elemento,']', end=' ')
print()

for indice,elemento in enumerate(array):
    if indice == 50:
        print("Elemento en la posicion 50: ",elemento)
        array[indice] = "bbbb"
        print("Modificamos el array original, pero no el elemento en el for: ",elemento, array[indice])          # El "elemento" no se ve modificado ya que se cogen sus valores copiados al inicio del bucle, solo podemos modificar directamente en el array original

## FUNCIONES ÚTILES (las de modificar solo valen para array, si está marcada con NT significa que no vale para tupla)##
array = list(range(10))
array.append(list(range(10,20)))        # NT Al igual que el operador + pero en este caso no tenemos que poner el =, puedes añadir cualquier cosa, como un solo elemento
print("Array aumentado con append: ",array)
array.clear()                           # NT Vacia el array
print("Array vaciado: ",array)
array = list(range(10))
array2 = array.copy()                   # Copia el array
print("Array copiado del primero: ",array,array2)
numero = array.count(1)                 # Devuelve el número de elementos iguales al indicado como parámetro
print("Número de numeros 1 que hay en el array: ",numero)
array.extend(['a','b','c'])             # NT extiende el array con un iterable, solo valen iterables
print("Array extendido: ",array)
numero = array.index('a')               # Devuelve el primer índice que encuentre del valor indicado por parámetro, si no encuentra, da error
print("Posición del caracter 'a' en el array: ",numero)
array.insert(5,"patata")                # NT inserta en la posición indicada en el primer parámetro el elemento del segundo, puede ser cualquier tipo, incluso otra lista
print("Hemos añadido en la posición 5 \"patata\": ",array)
array.pop()                             # NT elimina el elemento en la posición indicada (por defecto, sin parámetro, el último)
print("El último elemento ha sido eliminado: ",array)
array.remove(2)                         # NT elimina el primer elemento que encuentre igual al indicado por parámetro, error si no lo encuentra
print("Hemos eliminado el elemento en la posición 2: ",array)
array.reverse()                         # NT da la vuelta a la lista
print("Array dado la vuelta: ",array)
#array.sort()                           NT ordena el array en orden ascendente por defecto. IMPORTANTE: No funciona con elementos de distinto tipo
array = [5,4,9,8,3,4,7,12,1,0,3,89]
array.sort()
print("Array de números ordenados: ",array)
array = ["fgoc","asasdf","vjasdop","poernsd",'b',"ñlksn"]   # Orden alfabético
array.sort()
print("Array de str ordenado: ",array)
