"""
    Quinto archivo de ayuda. Vamos a hablar de las funciones, una herramienta de lo más útil.
    A partir de ahora, debes de aprenderte esta regla: Si lo escribo dos veces, se va a una función.
    ¿Qué significa esto? Repetir código es una práctica poco eficiente, si vas a usar dos veces algo exactamente igual, lo normal es que solo lo escribas una vez y lo "llames"
    Las funciones las puedes declarar cuando quieras, pero solo puedes invocarlas después de ello.
"""
import random

def funcionDeEjemplo():                         # Usando la palabra reservada "def" definimos la función
    print("Me llamas desde otra parte")         # Todo el código que esté dentro del bloque se ejecutará solo cuando se invoque la función

funcionDeEjemplo()                              # Aquí llamamos a la función previamente declarada

def funcionConParametro(unParametro):           # Podemos pasar variables externas a la función y usarlas dentro como queramos
    print(f"El parámetro que has pasado {unParametro}")

funcionConParametro("Este parámetro")

# Referencia o valor
""" 
    Por referencia o por valor? Que es?
    Un parámetro por referencia significa que la variable que introduzcas puede ser modificada dentro de la función y se verá afectada fuera de ella.
    Por valor simplemente se pasa una copia y puede ser usado dentro de la función sin que su valor sea modificado fuera de ella.
"""

def porValor(parametro):                                    # Los tipos simples SOLO pueden pasar por valor, nunca puedes modificarlos dentro
    print(f"El valor del parámetro es: {parametro}")
    parametro += 15                                         # Aunque aquí se esté modificando, no es afectado por fuera
    print(f"Le he añadido 15 y ahora vale: {parametro}")

unInt = 15
print(f"La variable antes de ser pasada vale: {unInt}")
porValor(unInt)                                             # Llamo a la función pasando la variable
print(f"La variable después de ser pasada vale: {unInt}")


def porReferencia(array):                                   # Los tipos compuestos SOLO se pasan por referencia, puedes modificarlos dentro
    print(f"La función por referencia ha recibido: {array}")
    array.append(15)                                        # Estoy añadiendo un elemento nuevo al array
    print(f"He añadido un valor, ahora es: {array}")

unArray = [1,2,3,4]
print(f"El array que he declarado es: {unArray}")
porReferencia(unArray)                                      # Al pasar el array si se modifica
print(f"Después de pasarlo por la función, se ha modificado: {unArray}")

""" Pero, ¿Como modifico entonces un valor simple?"""
unInt = 1
def usandoGlobal():
    global unInt                                            # Declaramos que es una variable externa
    print("Si uso la palabra clave global puedo acceder a variables externas")
    unInt += 1

print(f"Antes de pasar por la función vale: {unInt}")
usandoGlobal()
print(f"Después vale: {unInt}")

## No recomiendo usar realmento eso, puede ser peligroso si se usa mal

# El return
""" 
    Como bien indica el nombre, la palabra clave "return" sirve para devolver un valor.
    Importante, una vez que se llama a return, se sale directamente de la función.
"""

def usandoElReturn(parametro1,parametro2):      # Se pueden pasar tantos parametros como se quiera
    if parametro1 > parametro2:
        return True                             # Puedo devolver un valor directamente, no necesito que sea una variable
                                                # Si se ejecuta el return, esta parte del código se salta
    print("El parametro2 es mayor, el código continua")
    variable = False
    return variable                             # En este caso he querido devolver una variable

resultado = usandoElReturn(random.randint(1, 10), random.randint(1, 10))    # La salida de la función se almacena en la variable.Estoy pasando por referencia una función, pero como solo estoy pidiendo un int, no importa
print(f"El return me ha dado un: {resultado}")

""" Con el return puedes devolver lo que quieras, cualquier tipo de variable"""
def salidaDeInt():
    return random.randint(1, 15)

print(f"La salida de la función es: {salidaDeInt()}")   # Usandola dentro de un print es como ya hemos visto


# Parametros por defecto y opcionales
""" 
    Existe la posibilidad de declarar parámetros por defecto o dejarlos como opcionales para no tener que siempre meterlos o que simplemente, como indica, sean opcionales
"""

def parametroOpcional(parametro="Soy lo por defecto"):  # Al igualar un parámetro a algo, ya haces que sea opcional. En caso de no ponerlo, se cogerá el valor que se ha puesto en la igualdad.
    print(parametro)

parametroOpcional()                                     # Llamada sin parámetro a la función
parametroOpcional("Este no es por defecto")             # Poniendo un parámetro

def parametroObligatorioYOpcional(obligatorio,opcional="Opcional soy"): # Se pueden combinar obligatorios con opcionales PERO los obligatorios siempre van primero declarados
    print(f"Este es obligatorio {obligatorio}, este no {opcional}")

parametroObligatorioYOpcional("obligatorio")
parametroObligatorioYOpcional("obligatorio","Opcional pero ahora si me han metido")