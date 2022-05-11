""" 
    Antes de leer este ejercicio, te recomiendo que vayas a la carpeta de ayudaPython y mires el archivo extra de ayuda mainYArgumentos.py.
    Ahora con el ejercicio.
    Ya tenemos las funciones en un fichero separado con su main para probar, pero ahora queremos un main de verdad, uno que nos permita usar a voluntad cada una de las funciones.
    -> Crea un archivo nuevo dentro de tu carpeta y llamalo mainBasicos.py.
    -> En este ejercicio vamos a requerir de argumentos, a si que no te olvides de importar la librería que toca.
    -> Nuestro código principal deberá comprobar si tiene argumentos:
        -> No hay ni un argumento: Vamos a tener un "menu" que pedirá por teclado un número. Cada número corresponde a cada una de las funciones en orden. Cuando le demos a un número, el programa deberá pedir
        el resto de cosas necesarias. Por ejemplo, le decimos un 1, que corresponde con el que calcula Pi, el programa nos pedirá el número para las iteraciones que se le pasará a la función y luego enseñará el resultado por pantalla.
        -> Pasamos un número como argumento: El programa saltará directamente a la función que corresponde a la función, pedirá lo que toca, ejecutará la función y saldrá del programa. Para hacer esto te recomiendo crear una variable como 
        flag, si metes un argumento pon a True el flag y que el bucle compruebe al final si está o no a true, si lo está sal del bucle y el programa.
        -> Pasamos un número seguido de la letra S: Ahora, el programa ejecutará la función, pero no saldrá, luego pondrá el menú tal cual, continuando el progama.
        -> Pasamos la letra H sin importar la posición: Esto va a hacer que se ignore por completo todo lo demás. Siempre que aparezca una H, se debe SOLAMENTE mostrar por pantalla un mensaje de ayuda que diga como usar el programa con 
        los argumentos. No debe decirte como funcionan las funciones en sí, solamente como se usa el programa con los argumentos.
        -> Para salir del programa de forma normal, lo haremos por la función del ejercicio 7, al escribir la palabra "salir" se cerrará el programa.

    -> Notas:
        -> El ejercicio 4 se le va a cambiar el nombre a la función. En lugar de listaEmail va a ser stringALista o similar, porque ahora no hay que pasarle un usuaruio de email, cualquier palabra o frase que le pasemos la separará en caracteres.
        -> Si el programa recibe un argumento incorrecto o un orden incorrecto, por ejemplo primero la S y después el número o algo distinto del número de primeras, deberá salir por pantalla un mensaje indicando que es un uso incorrecto seguido del mensaje de ayuda.
        -> Si se reciben más de 2 argumentos, sin que el tercero sea la H, también será error.
        -> Los argumentos deben dar igual que estén en mayus o minus al pasarlos, deberás convertirlos a tu gusto.
"""

"""
    Como conseguir que mi código sea un buen código:
    -> Recuerda que el usuario medio es tonto del culo, por lo tanto tu programa tiene que estar hecho para ello.
    -> Piensa que estás trabajando con un equipo, comenta tu código. No solo viene bien para tus compañeros, si no para ti para saber que has hecho en el pasado.
    -> Nombres de variables y de funciones, sigue un estilo homogéneo con tu propio código y que los nombres sean AUTOEXPLICATIVOS. No me pongas nombres de variables cortos, no te vale a ti tampoco. Los nombres largos no gastan recursos,
    si tienes que poner un nombre tipo variableQueHaceEstaCosaEspecifica, ponlo, es gratis y te va a ayudar mucho.
    -> SANGRIA, que todo esté bonito por dios.
    -> Pon todos los prints que necesites, cuanta más información visual tenga el usuario, más fácil.
"""