""" 
    Esta va a ser la clase básica de la que heredarán todas las demás que haréis en vuestro ejercicio.
    Cada sub clase nueva vendrá descrita más abajo como debe de ser.
"""

class Aventurero:
    # Cada una de las características básicas de todo aventurero
    caracteristicas = {
        "fuerza" : 0,
        "destreza" : 0,
        "constitucion" : 0,
        "inteligencia" : 0,
        "sabiduria" : 0,
        "carisma" : 0
    }
    
    __nombreCaracteristicas = (("fuerza","destreza","constitucion","inteligencia","sabiduria","carisma"))

    # A cada característica le corresponde un bonificador extra (esto es típico de los juegos)
    bonificadores = {
        "fuerza" : 0,
        "destreza" : 0,
        "constitucion" : 0,
        "inteligencia" : 0,
        "sabiduria" : 0,
        "carisma" : 0
    }


    # ¿Qué clase de aventurero serías sin un nombre?
    nombre = ""
    raza = ""
    
    # Un par más de características adicionales
    velocidad = 0
    armadura = 0
    vida = 0

    # Lista privada de atributos para luego manejarla en cada clase
    __listaAtributos = [0,0,0,0,0,0]

    # En el constructor tenemos que pasarle nombre y raza obligatorios, pero la lista de atributos es opcional, asignadose los valores por defecto
    def __init__(self,nombre,raza,atributos = [15, 14, 13, 12,10, 8]):
        self.__listaAtributos = atributos
        self.nombre = nombre
        self.raza = raza

    # Devuelve el valor del bonificador en base a la lista de correspondencias
    """
        Valor del atributo ---> Bonificador
                1                   -5
               2-3                  -4
               4-5                  -3
               6-7                  -2
               8-9                  -1
              10-11                 +0
              12-13                 +1
              14-15                 +2
              16-17                 +3
              18-19                 +4
              20-21                 +5
              22-23                 +6
              24-25                 +7
              26-27                 +8
              28-29                 +9
               30                   +10
    """
    def calculoBonificador(self,atributo):
        for i in range(-5,30):
            atributo -= 2
            if(atributo < 0):
                return i

    # En caso de que no se quiera asignar a mano, se llama a esta función y asigna los huecos por defecto
    def defaultAsing(self):
        for i,valor in enumerate(self.__listaAtributos):
            self.caracteristicas[self.__nombreCaracteristicas[i]] = valor


    def __buscaLista(self,lista,valor):
        print(lista,valor)
        try:
            return lista.index(valor)
        except:
            print("Ese valor no está en la lista")
            return -1

    # Asignación manual de cada característica
    def asignaCaracterística(self):
        copiaLista = self.__listaAtributos.copy()
        for caracteristica in self.__nombreCaracteristicas:
            print("Tienes disponibles estos valores de característica:", copiaLista)
            index = -1
            while index == -1:
                valor = int(input(f"Que valor quieres asignarle a la {caracteristica}: "))
                index = self.__buscaLista(copiaLista,valor)
                if index != -1:
                    self.caracteristicas[caracteristica] = copiaLista[index]
                    copiaLista.pop(index)

        print("Has escogido:")
        for caracteristica in self.__nombreCaracteristicas:
            print(caracteristica.capitalize() + ":", self.caracteristicas[caracteristica])


        response = input("¿Quieres calcular los bonificadores? \"Y\"/\"n\"") or 'Y'     # De esta forma hacemos un valor por defecto en el imput, si le damos al enter sin más se pasará siempre el 'Y'
        if response.lower() == 'y':
            self.calculoBonificadores()
        
         

    # Calcula cada bonificador de cada característica
    def calculoBonificadores(self):
        for caracteristica in self.__nombreCaracteristicas:
            self.bonificadores[caracteristica ] = self.calculoBonificador(self.caracteristicas[caracteristica])


    # Imprime toda la información de nuestro aventurero (habrá que sobrecargarla)
    def imprimeAventurero(self):
        print("Hola, soy",self.nombre,"y soy",self.raza)

        print("Mis atributos son:")
        for caracteristica in self.__nombreCaracteristicas:
            print(caracteristica.capitalize() + ':', self.caracteristicas[caracteristica],'+' if self.bonificadores[caracteristica] >= 0 else '-', self.bonificadores[caracteristica] if self.bonificadores[caracteristica] >= 0 else self.bonificadores[caracteristica]*-1)

        print("Mi velocidad es de:",self.velocidad)
        print("Mi armadura es de:",self.armadura)


#paco = Aventurero("Paco","Humano")
#paco.defaultAsing()
#paco.asignaCaracterística()
#paco.calculoBonificadores()
#paco.imprimeAventurero()

""" 
    Ahora te toca a ti extender esta clase con la "clase" de aventurero que te toque.
    Abajo vas a ver la descripción de cada una de ellas y la que te ha tocado asignada. Puedes hacerlo en este fichero, pero prefiero que cojas tu cachito de descripción y te lo lleves a un archivo con el nombre de 
    esa clase.
"""
""" 
    Aquí están las clases junto a su asignado
    Guerrero:   Raul
    Hechicero:  Fran
    Bárbaro:    Lorena
    Paladín:    Jose
    Explorador: Irene
    Pícaro:     Javi
    Tirador:    Clara
    Clerigo:    Laura
"""

""" 
    Cada uno de las clases debe tener dos características principales que deberán tener asignada siempre los dos valores más altos, siempre en el orden que te indico.
    Luego cada una tendrá diferentes modificadores, que habrá que sumar o restar, esto solo cuando se crea al aventurero.
    Cada uno tendrá sus propias armas y armaduras, pero se lo vas a tener que asignar tu.
    Habrá que crearles unas funciones para asignar todo lo que se diga.
    Habrá unas clases con habilidades y otras con hechizos o ambas a la vez.
    Si tiene hechizos, tiene maná (un número que indique su cantidad de maná)
    También necesitarán funciones para esto.
    Habrá que tener en el __init__ inicializadas todas las variables y luego una función extra que haga eso también.
    Todas las clases van a tener un inventario, una lista de objetos con su cantidad de cada.
    Recuerda que todo debe ser lo más sencillo para el usuario. Si quiero cambiar el arma, que haya una función para ello.
    Y recuerda que si se actualiza una característica, se deben actualizar las características que dependenden de ello (vida, velocidad, armadura...)

    HAY QUE HACER UN MAIN QUE LO PRUEBE TODO 
""" 

### Gerrero ------> Raul
""" 
    Sus caracteristicas más altas: Fuerza y destreza.
    Podrá usar varias armas, por lo que tendrás que tener una variable (o un diccionario) con todas las armas que tengas (un strign con el nombre, no te compliques mas) y otra variable más que indique que arma estás usando.
    Tendrá escudo que sumará directamente a la armadura (Diccionario con nombre del escudo y valor de armadura) con valor entre 1 y 3.
    Llevará equipada una armadura ligera con un valor entre 5 y 10 que se sumará a su valor de armadura total (Diccionario con nombre de la armadura y valor de armadura).
    Las armas que usa (todo una mano): espada, hacha, lanza, porra, martillo, estoque y látigo.
    Tendrá tanto hechizos como habilidades.
    No tiene ni modificador bueno ni malo.
    Su vida se calcula: Su constitución + 2 * bonificador de constitución.
    La velocidad es 3 * bonificador de destreza.
"""

### Hechicero ------> Fran
""" 
    Sus características más altas: Inteligencia y sabiduria.
    Solo puede usar un objeto mágico (un báculo, un grimorio, un medallón) como arma.
    Llevará una túnica que le dará entre 1 y 3 de armadura y se sumará al valor total de armadura (Diccionario con nombre de la armadura y valor de armadura).
    Tendrá dos huecos de invocación que serán de la clase "Aventurero" completo.
    Tendrá solamente hechizos.
    Gana de forma aleatoria entre 2 y 5 en inteligencia, 1 y 3 en sabiduría y pierde entre 1 y 3 de fuerza.
    Su vida se calcula: solo es su constitución.
    La velocidad es 2 * bonificador de destreza.
"""

### Bárbaro ------> Lorena
""" 
    Sus caracrísticas más altas: Fuerza y constitución.
    Podrá usar varias armas, por lo que tendrás que tener una variable (o un diccionario) con todas las armas que tengas (un strign con el nombre, no te compliques mas) y otra variable más que indique que arma estás usando.
    No usa armadura, pero tiene una armadura natural que es 2 veces su bonificador de constitución.
    Las armas que usa (todo dos manos): Hacha dos manos, espadón, martillo de guerra y maza grande.
    Tendrá solo habilidades.
    Gana de forma aleatoria entre 2 y 5 en fuerza, 2 y 5 de constitución, pierde entre 2 y 5 de inteligencia y 1 y 3 de sabiduria.
    Su vida es 3 veces su constitución.
    La velocidad es 2 * bonificador de destreza.
"""

### Paladín ------> Jose
"""
    Sus características más altas: Constitución y carisma.
    Podrá usar un gran espadon.
    Usa un gran escudo que sumará directamente a la armadura (Diccionario con nombre del escudo y valor de armadura) con valor entre 3 y 6.
    Usa una gran armadura con un valor entre 10 y 20 que se sumará a su valor de armadura total (Diccionario con nombre de la armadura y valor de armadura) pero le da -3 a la velocidad.
    Tendrá tanto hechizos como habilidades.
    Gana de forma aleatoria entre 3 y 6 de constitución, 1 y 3 de carisma, pierde entre 2 y 5 de destreza.
    Su vida es 2 veces su constitución + 2 * bonificador de constitución.
    Su velocidad es 2 * el bonificador de destreza.
"""

### Explorador ------> Irene
"""
    Sus características más altas: Destreza y sabiduría.
    Usará un arco y una gran daga solamente, pudiendo usar ambas a la vez.
    Llevará equipada una armadura ligera con un valor entre 5 y 10 que se sumará a su valor de armadura total (Diccionario con nombre de la armadura y valor de armadura).
    Tendrá solo habilidades.
    Gana de forma aleatoria entre 3 y 6 de destreza.
    Su vida es 2 veces su constitución.
    Su velocidad es 4 veces su destreza.
"""

### Pícaro ------> Javi
""" 
    Sus características más altas: Destreza y carisma.
    Usará solo dagas, pero tendrá un segundo inventario con cosas robadas, por lo que podrá robar (una funcion basicamente que meta cosas en ese inventario).
    Llevará una túnica que le dará entre 1 y 3 de armadura y se sumará al valor total de armadura (Diccionario con nombre de la armadura y valor de armadura).
    Tendrá hechizos y habilidades.
    Gana de forma aleatoria entre 3 y 6 en destreza y 1 y 3 en carisma, pero perderá en una característica aleatoria entre 1 y 3.
    Su vida es solo su constitución. 
    Su velocidad es 4 veces su destreza.
"""

### Tirador ------> Clara
"""
    Sus características más altas: Destreza y sabiduría.
    Podrá usar solo armas a distancia.
    Llevará equipada una armadura ligera con un valor entre 5 y 10 que se sumará a su valor de armadura total (Diccionario con nombre de la armadura y valor de armadura).
    Podrá usar tanto hechizos como habilidades.
    Tendrás un inventario extra para la munición (flechas o balas según el arma que use).
    Gana de forma aleatoria entre 2 y 5 de destreza y 2 y 5 de sabiduría, pero pierde entre 1 y 3 de inteligencia.
    Su vida es 2 veces su constitución.
    Su velocidad es 3 veces su destreza.
"""

### Clérigo ------> Laura
"""
    Sus características más altas son: Constitución e inteligencia.
    Solo puede usar un mazo de guerra como arma.
    Tendrá una variable extra que indica la deidad a la que reza. Su deidad le da extra +5 en una característica aleatoria.
    Llevará equipada una armadura ligera con un valor entre 5 y 10 que se sumará a su valor de armadura total (Diccionario con nombre de la armadura y valor de armadura).
    Podrá usar tanto hechizos como habilidades.
    Gana de forma aleatoria entre 3 y 6 de constitución, pierde entre 2 y 5 de destreza.
    Su vida es 4 veces su constitución.
    Su velocidad es 2 veces su destreza.
"""