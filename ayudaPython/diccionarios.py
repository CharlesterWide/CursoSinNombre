"""
    Cuarto archivo de ayuda. Los diccionarios, también conocidos como estructuras, mapeos o pares clave-valor.
    Podriamos definirlo como la herramienta para crear nuestros propios tipos compuestos, ya que dentro podemos tener lo que queramos, desde solamente números hasta tener otros diccionarios.
"""
## Definición ##
""" Como ya hemos visto como se definen todos los demás tipos, el diccionario se reduce a simplemente como los metemos dentro """
diccionario = {
    'Nombre'  : "Charlie",                          # Un string
    'Edad'    : 26,                                 # Un entero
    'Soltero' : False,                              # Un booleano
    'Altura'  : 1.68,                               # Un float
    'Hermanas': ("María","Ana","Paula","Clara")     # Una tupla
}
""" Por norma general, para definir las claves (parte de la izquierda) comillas simples ''. Para asignar el valor NO ES EL '=', se utilizan los ':'. Y separamos los pares clave-valor con ',' """
# Accediendo a un valor
""" Tanto si es para leer como para modificar, accedemos de la misma forma, usando el corchete con la clave dentro entre '' """
print("Sacando un dato simple: ",diccionario['Nombre'])        # Accediendo a un dato simple
print("Sacando un dato dentro de una lista: ",diccionario['Hermanas'][3])   # Accedoemdp a la tupla
print("Mostrando el diccionario completo: ",diccionario)                  # Podemos mostrar la estructura entera
diccionario['Nombre'] = "Charlie Rubio" # Modificamos directamente la variable
print("Valor modificado: ",diccionario)

# Se pueden añadir claves nuevas?
diccionario['Hijos'] = "Un pájaro cuenta?"   # Tan fácil como esto, como si modificasemos una de las claves, aunque no exista, esta se añadirá
print("Clave 'Hijos' añadida: ",diccionario)

## Funciones del diccionario ##
otroDic = diccionario.copy()        # Copia el diccionario en otro
string = diccionario.get('Nombre','Si no existe la clave, este parametro sirve para devolver algo por defecto') # Para obtener, de forma segura, un valor. MUY RECOMENDADO USAR SIEMPRE, NOS EVITAMOS POSIBLES ERRORES
items = diccionario.items()         # Devuelve todos los pares clave valor que hay dentro del diccionario
print("Lista de items del diccionario: ",items)
keys = diccionario.keys()           # Devuelve la lista de las claves del diccionario
print("Las claves del diccionario: ",keys)
diccionario.pop('Hijos')            # Elimina el par indicado por la clave
print("Diccionario con la clave 'Hijos' eliminada: ",diccionario)
parEliminado = diccionario.popitem()# Elimina el último par que encuentre y lo devuelve
print("El par eliminado con popitem(): ", parEliminado)
valores = diccionario.values()      # Devuelve la lista de valores
print("Los valores del diccionario: ",valores)
diccionario.clear()                 # Elimina todo lo que haya en el diccionario
print("Diccionario vaciado", diccionario)
diccionario =  {}.fromkeys(['Nombre','Edad','Soltero','Altura','Hermanas'],"Oh no, es cacota")  # Crea un diccionario con las claves indicadas en la primera lista y todos con el valor indicado en el segundo parámetro
print("Diccionario reconstruido con la funcion: ",diccionario)