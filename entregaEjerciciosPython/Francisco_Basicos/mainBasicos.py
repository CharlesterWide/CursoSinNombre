from time import sleep
import os
import sys
import Funciones

# mensaje de error por introducción incorrecta de los argumentos
def argumentsError():
    print("\n\t(!) Error (!)")
    print("\nEjecuta el script seguido del argumento [H] para ver la ayuda de argumentos\n")

# muestra la ayuda de los argumentos del script
def showArgumentsHelp():
    print("\n==============================================================================================================")
    print("Esta es la ayuda de argumentos de este programa.")
    print("Aquí podrás encontrar una guia detallada de los argumentos que admite este script, así como su orden correcto.")
    print("==============================================================================================================")
    print("\nARGUMENTOS CON ORDEN OBLIGATORIO:")
    print("\t1º [N] Numero entero      Un número entero comprendido entre el siguiente rango {1-7}")
    print("\t2º [S] Caracter S         El caracter 'S' para indicar que vuelva a aparecer el menu de seleccion de ejercicio")
    print("\nARGUMENTOS SIN ORDEN:")
    print("\t   [H] Caracter H         Muestra la ayuda para los argumentos del script")

# comprueba si se ha requerido la ayuda por paso de argumentos con el script
def helpRequested(longitudArgumentos):

    ayuda = False

    for i in range(longitudArgumentos):
        if(sys.argv[i].lower() == 'h'):
            ayuda = True

    return ayuda

# control de los argumentos introducidos con el script para su ejecucion
def argumentsHandle():

    longitudArgumentos = len(sys.argv)

    menuRepeticionYFuncion = []

    if (longitudArgumentos == 1):
        menuRepeticionYFuncion = [True, False, -1]
        return menuRepeticionYFuncion

    elif (longitudArgumentos == 2):

            if(helpRequested(longitudArgumentos)):
                showArgumentsHelp()
            else:
                try:
                    ejercicio = int(sys.argv[1])

                    if(ejercicio > 0 and ejercicio < 8):
                        menuRepeticionYFuncion = [False, False, ejercicio]
                        return menuRepeticionYFuncion

                    else:
                        argumentsError()

                except:
                    argumentsError()

    elif (longitudArgumentos == 3):

        if(helpRequested(longitudArgumentos)):
            showArgumentsHelp()
        else:
            try:
                ejercicio = int(sys.argv[1])

                if(ejercicio > 0 and ejercicio < 8 and sys.argv[2].lower() == 's'):
                    menuRepeticionYFuncion = [True, True, ejercicio]
                    return menuRepeticionYFuncion

                else:
                    argumentsError()

            except:
                argumentsError()

    elif (longitudArgumentos == 4):

        if(helpRequested(longitudArgumentos)):
            showArgumentsHelp()
        else:
            argumentsError()

# construye el menu
def menuBuilder():
    menu = []
    menu.append("\n==> Menú de selección de ejercicio <==\n")
    menu.append("1. Aproximación de Pi\n")
    menu.append("2. Geometría de la circunferencia\n")
    menu.append("3. Añade un email y separa usuario y demonio\n")
    menu.append("4. Imprime los caracteres de la cadena que texto que introduzcas por teclado\n")
    menu.append("5. Imprime un triángulo\n")
    menu.append("6. Imprime una pirámide\n")
    menu.append("7. Realiza un eco de lo que introduzcas\n")
    menu.append("   · Introduce el número del ejercicio que desees lanzar -> ")
    return menu

# imprime por pantalla el menu
def menuPrint():
    for l in range(len(menuBuilder())):
            print(menuBuilder()[l], end="")

    ejercicio = input()

    try:
        return int(ejercicio)
    except:
        return -1

# segun el numero que se le paso lanza el ejercicio al que equivale
def exercisesLauncher(ejercicio):

    os.system ("cls")

    again = True

    if(ejercicio == 1):
        print("====== Ejercicio 1 ======")
        n = int(input('Dame un número semilla para calcular Pi: '))
        Pi = Funciones.aproximaPI(n)
        print(f"\nLa aproximación al número Pi es: {Pi}\n")

    if(ejercicio == 2):
        print("====== Ejercicio 2 ======")
        R = int(input('Dame radio de la circunferencia: '))
        circunferencia = Funciones.geometriaCircunferencia(R)
        for (clave, valor) in circunferencia.items():
            print(clave + ":", "{0:.2f}".format(valor))
        print()

    if(ejercicio == 3):
        print("====== Ejercicio 3 ======")
        correo = input("\n· Introduce un email \n· (no voy a programar 200 verificaciones de que el correo sea correcto\n asique ajustate al formato ==> usuario@dominio ) : ")
        email = Funciones.incorporaEmail(correo)
        for (clave, valor) in email.items():
            print(clave + ":", valor)
        print()

    if(ejercicio == 4):
        print("====== Ejercicio 4 ======")
        cadena = input("\n· Introduce una cadena de caracteres: ")
        caracteres = Funciones.stringALista(cadena)
        for i,c in enumerate(caracteres):
            print("[ ", i, "=> ", c, " ]")
        print()

    if(ejercicio == 5):
        print("====== Ejercicio 5 ======")
        F = int(input('Induca el número de filas del triángulo a dibujar: '))
        numeros = Funciones.imprimeTriangulo(F)    
        print(numeros)

    if(ejercicio == 6):
        print("====== Ejercicio 6 ======")
        F = int(input('Indica el número de filas de la pirámide a dibujar: '))
        caden = Funciones.imprimePiramide(F)
        print(caden)

    if(ejercicio == 7):
        print("====== Ejercicio 7 ======")
        Funciones.eco()
        again = False
    
    return again

# codigo main que ejecuta la secuancia del programa
if  __name__ == "__main__":

    os.system ("cls")

    menuRepeticionYFuncion = argumentsHandle()

    # compruebo  si se ha solicitado la ayuda de argumentos para no ejecutar nada de la secuencia del programa si es así
    if(menuRepeticionYFuncion != None):

        # ejecucion del script sin argumentos
        if(menuRepeticionYFuncion[2] == -1):

            check = True

            # sin argumentos lo primero es lanzar el menu
            while check:

                ejercicio = menuPrint()

                if(ejercicio > 0 and ejercicio < 8):

                    exercisesLauncher(ejercicio)

                    check = menuRepeticionYFuncion[1]

                else:
                    # reinicio el menu si el usuario introduce un valor no válido
                    os.system ("cls")
                    for c in range(3, 0, -1):
                        print("\n(!) Introduce un valor correcto (!)")
                        print(f"      Reinicio en: {c} segundos")
                        sleep(1)
                        os.system ("cls")

        # ejecucion del script con el argumento numerico y el caracter 'S'
        elif (menuRepeticionYFuncion[0]):

            # con argumentos primero lanzo el ejercicio
            exercisesLauncher(menuRepeticionYFuncion[2])

            check = True

            # y luego muestro el menu
            while check:

                ejercicio = menuPrint()

                if(ejercicio > 0 and ejercicio < 8):

                    check = exercisesLauncher(ejercicio)

                else:
                    # reinicio el menu si el usuario introduce un valor no válido
                    os.system ("cls")
                    for c in range(3, 0, -1):
                        print("\n(!) Introduce un valor correcto (!)")
                        print(f"      Reinicio en: {c} segundos")
                        sleep(1)
                        os.system ("cls")

        # ejecucion del script unicamente con el argumento numerico
        else:

            # solo lanza el ejercicio seleccionado
            exercisesLauncher(menuRepeticionYFuncion[2])

