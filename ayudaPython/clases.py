"""
    Septimo archivo de ayuda. Vamos con las clases.
    ¿Qué es una clase? Desde el principio hemos estado hablando de "objetos" y los hemos estado usando sin saber que eran realmente.
    Los string, los array o los diccionarios, entre otros tipos de datos, ya son objetos. Python es un lenguaje orientado a objetos y va siendo hora que hagamos uso de eso.
    Una clase no es más que una colección de atributos (variables) y métodos (funciones) bajo un nombre.
    Por ejemplo, la persona. Una persona tiene como atributos su nombre, su altura, su peso, su edad y otros atributos que "no vemos" como su energía o hidratación, y tiene funciones 
    como comer y beber agua que restauran energia e hidratación o puede decir su nombre.
    Lo mejor será verlo con ejemplos.
"""

class Persona:                         # Como norma no establecida, los nombres de las clases empiezan en mayus
    nombre =        ''                 # De esta forma declaramos un atributo público, es una variable normal y corriente
    altura =        0
    peso =          0
    edad =          0                  # Que estén puestas aquí a '' o a 0 es simplemente por tenerlas inicializadas a algo
    __energia =     0                  # Al usar __ delante de un nombre de variable la declaramos como "privada", de esta forma no podrá ser accedida desde fuera y
    __hidratacion = 0                  # Solo podrá ser modificada dentro de la misma clase

    def __init__(self,nombre,altura,peso,edad,energia = 100,hidratacion = 100 ):    # La funcion que definamos con __init__ es el "constructor de clase". La función que se lanza siempre que creemos una "instancia" de la clase. El parametro self siempre hay que ponerlo dentro de una función si queremos acceder a sus atributos en la misma. pero al llamarla desde fuera no tenemos que pasarlo
        self.nombre = nombre                                                        # Al usar self. podemos acceder a cualquier cosa de nuestra clase
        self.altura = altura
        self.peso = peso
        self.edad = edad
        self.__energia = energia                                                    # Los atributos privados los podemos setear aquí porque estamos dentro de la clase
        self.__hidratacion = hidratacion
        self.colorDePelo = "Rubio"                                                  # Aunque arriba no hayamos definido esta variable, aquí la instanciamos, es decir, la creamos aquí dentro y puede ser accedida en todas partes

    def diNombre(self):                                                             # Las funciones se declaran igual que hasta ahora, solo que dentro de la clase
        print(f"Me llamo {self.nombre}")
        self.__energia -= 5
        self.__hidratacion -= 2
        
    
    def diPesoYAltura(self):
        print(f"Peso {self.peso} y mido {self.altura}")
        self.__energia -= 5
        self.__hidratacion -= 2

    def nivelCansancio(self):
        if self.__energia > 90:
            return "Energico"
        elif self.__energia > 60:
            return "Normal"
        elif self.__energia > 35:
            return "Cansado"
        else:
            return "Critico"
    
    def comer(self,comida):
        self.__energia = 100 if self.__energia + comida >= 100 else self.__energia + comida # Esta es un tipo de if fancy en linea que nos puede ayudar a reducir codigo, digamos que es un "este valor si se cumple esta condicion y si no este valor"

    def diColorPelo(self):
        print("Mi pelo es",self.colorDePelo)            # Hemos accedido a la variable instanciada dentro del __init__
            
###############################################################################    
    
# Como lo instanciamos
paco = Persona("Paco", 1.80, 82, 35)                        # Lo declaramos como una variable normal, pero como en el __init__ le hemos dicho que tiene que tener parametros, aquí se los pongo
paco.diNombre()                                             # Aunque en la definición tengamos puesto el self, aquí NO SE PONE
paco.diPesoYAltura()
print("Soy",paco.nombre,"y estoy",paco.nivelCansancio())
paco.comer(100)                                             # La única manera de interactuar con variables privadas es mediante funciones
print("El cansancio ahora es",paco.nivelCansancio())

""" 
    Otro concepto muy importante y de lo más útil/importante es la herencia. Como he dicho varias veces, escribir dos veces el mismo código está mal, por lo que si vamos a crear una clase que comparte todo lo que ya tiene con otra,
    es mejor usar la herencia.
    Esta vez vamos a usar los vehículos como ejemplo
"""

class Vehiculo:
    cilindradaMotor = 0
    tamaño = 0
    ruedas = 0
    capacidad = 0

    def __init__(self):
        self.cilindradaMotor = 500
        self.tamaño = 2.50
        self.ruedas = 4
        self.capacidad = 4
    
    def arranca(self):
        print("Bruuummmm dice el coche al arrancar")

class Coche(Vehiculo):                  # Poniendo entre parentesis otra clase estamos heredando de ella todas sus propiedades
    capacidadMaletero = 0               # Podemos poner tantos atributos nuevos como queramos
    def __init__(self): 
        super().__init__()              # Usando super() podemos invocar a cualquier método de la clase padre
        self.cilindradaMotor = 1200     # Editamos propiedades de la clase padre porque ahora son propiedad de esta clase tambien
        Vehiculo.arranca(self)              # De esta forma también podemos acceder a las funciones


coche = Coche()

""" 
    ¿Que pasa si queremos heredar de más de una clase? Podemos hacer herencia múltiple, es decir, heredar de todas las clases que queramos.
    Eso si, si heredamos de más de una clase, el super() no lo podemos usar, realmente si, pero hay que tener cuidado, no lo recomiendo.
"""

class Clase1:
    clase1ID = 1
    def __init__(self):
        print("Soy la clase 1")
    
    def printClase1(self):
        print("Este es mi print de la clase 1")

class Clase2:
    clase2ID = 2
    def __init__(self):
        print("Soy la clase 2")
    
    def printClase2(self):
        print("Este es mi print de la clase 2")

class Clase3(Clase1,Clase2):
    clase3ID = 3
    def __init__(self):
        print("Soy la clase 3 y he heredado")
        Clase1.__init__(self)                       # Al igual que antes, hemos accedico a la función especifica de la clase 1
        Clase2.__init__(self)
    
    def printClase1(self):                              # Podemos crear funciones con el mismo nombre que hagan cosas diferentes, esto se llama sobrecarga
        print("Esto es una sobrecarga de la primera clase")
        Clase1.printClase1(self)                        # No es necesario que se llame a la función original

clase3 = Clase3()
clase3.printClase1()