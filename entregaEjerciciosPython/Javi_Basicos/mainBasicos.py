import sys
import funciones

def mostrarMenu():                                                                                      #Subprograma para mostrar el menu y ahorrar lineas de codigos ya que se usaran varias veces
            print("BIENVENIDO AL MENU DE SELECCION DE FUNCIONES DE PYTHON!!")
            print("Por favor, lea las opciones e introduzca a continuacion la opcion que desee\n")
            print("1. Calcular Pi: Calcula el valor de Pi usando el metodo de Leibniz.")
            print("2. Calcular área, longitud y volumen de una esfera a partir del radio.")
            print("3. Diccionario de un email introducido: Se pedira un email a introducir y se separara en usuario y dominio.")
            print("4. Separar frase: Se separará una frase caracter a caracter.")
            print("5. Triangulo de numeros.")
            print("6. Piramide de numeros.")
            print("7. Convertir una frase en a su homónima en mayusculas.")
            print("IMPORTANTE: Mientras usted no introduzca <salir> en la opcion 7 del menu, el menu se repetira indefinidamente.\n")

def seleccionarOpcion(opcion):                                                                           #Selector de la opcion que ejecuta una opcion dependiendo de la introducida puediendo mostrar error, si el argumento introducido no es valido
            if(opcion=="1"):
                print("Calcular Pi")
                iteraciones = int(input("Introduce el numero de iteraciones: "))
                print(f"Su aproximacion a Pi es: {funciones.calcularPi(iteraciones)}\n")
            
            elif(opcion=="2"):
                print("Ejercicio Parametros de una Esfera")
                radio = int(input("Introduzca el radio de su esfera: "))
                print(f"Los parametros su esfera son: ", funciones.calcularParametros(radio), "\n")

            elif(opcion=="3"):
                print("Ejercicio Email")
                correo = input("Introduzca su email para crear el diccionario: ")
                print(f"Los parametros de su email son: ",funciones.mostrarCorreo(correo), "\n")
            
            elif(opcion=="4"):
                print("Ejercicio Frase Separada")
                frase = input("Introduzca su frase a seprara por caracteres: ")
                print(f"Su frase separada por caracteres es: ", funciones.stringALista(frase), "\n")

            elif(opcion=="5"):
                print("Ejercicio Triangulo de numeros")
                altura = int(input("Introduzca la altura de su triangulo: "))
                print(funciones.trianguloNumeros(altura))

            elif(opcion=="6"):
                print("Ejercicio Piramide de numeros")
                numer = int(input("Introduzca su email para crear el diccionario: "))
                print(funciones.piramideNumeros(numer))

            elif(opcion=="7"):
                print("Ejercicio Conversión a mayusculas")
                funciones.convierteFrase()
            else:
                print("Opcion introducida erronea\n")


if __name__ == "__main__":
    longitudArgumentos = len(sys.argv)                                                              #Miro cuantos argumentos hay escritos
    for indice,argumento in enumerate(sys.argv):                                                    #Recorro los argumentos
        if(argumento=="H"):                                                                         #Si hay una 'H' muestra la ayuda y nada mas sin importar los demas argumentos
            print("Para que el programa funciones debe introducir lo siguiente: ")
            print("Lo primero ./mainBasicos para ejecutar el programa")
            print("Si no introduce nada mas, mostrara el menu de manera repetitiva hasta que usted marque la opcion 7 introduzca <salir>")
            print("Si lo que desea es ejecutar solo 1 opcion, puede usar ./mainBasicos 6, que indica que solo quiere ejecutar la opcion 6 una unica vez. Asegurese de que es una opcion valida por favor")
            print("Si lo que desea es ejecutar solo 1 opcion, pero tras ello usar el menu indefinidamente como si no hubiese puesto ningun argumento debe introducir una 'S' tras el numero de la opcion")
            print("Si desea mostrar esta ayuda basta con que ponga una 'H' sin importar la posicion del argumento")
            print("Muchas gracias")
        else:                                                                                   #Si no hay ninguna H se procede a ejecutar las funciones
            #Atencion el menu solo se muestra si no hay argumentos
            if(longitudArgumentos==1):
                while(1):                                                                       #Si no hay argumento en el terminal
                    mostrarMenu()                                                               #Llamo a la opcion de mostrar menu
                    opcion=input(f"Introduzca su opcion deseada: ")
                    seleccionarOpcion(opcion)

            elif(longitudArgumentos==2):                                                        #Si hay un argumento mas en el terminal 
                arg=(sys.argv[1])                                                               #Declaro variable arg donde se almacena el valor del argumento de la posicion 1
                if(arg=="1" or arg=="2" or arg=="3" or arg=="4" or arg=="5" or arg=="6" or arg=="7"): #Si es un valor valido
                    seleccionarOpcion(arg)
                    exit(1)                                                                     #Salgo tras ejecutar la opcion
                else:                                                                           #Si he introducido un argumento no valido, muestra error
                    print("El argumento introducido es erroneo se esperaba un numero entre 1 y 7")
            
            #Parte un poco liosa e intentare explicarme todo lo que pueda
            elif(longitudArgumentos==3):                                                        #Si hay 3 argumentos              
                arg=(sys.argv[2])                                                               #Y tras el numero va una 'S'. EJ: ./programa 4 S
                if(arg=="S"):
                    arg2=(sys.argv[1])                                                          #Declaro una variable llamada arg2 donde guardare la posicion anterior de la S osea el numero que ejecutara la opcion correspondiente
                    if(arg2=="1" or arg2=="2" or arg2=="3" or arg2=="4" or arg2=="5" or arg2=="6" or arg2=="7"): #Si efectivamente es una opcion valida
                        seleccionarOpcion(arg2)                                                 #Ejecuto la opcion
                        while(1):                                                               #Tras ello muestro menu y se ejecuta indefinidamente hasta escribir salir en la opcion 7
                            mostrarMenu()
                            opcion=input(f"Introduzca su opcion deseada: ")
                            seleccionarOpcion(opcion)
                    else:
                        print("Fallo en la introduccion de argumentos se esperaba un numero entre 1 y 7 antes de la S")
            else:
                print("Demasiados argumentos introudcidos")


