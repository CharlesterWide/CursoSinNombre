# **Chuleta de control de versiones con git**

## 1. Definiciones

* **Control de versiones**: El control de versiones es un sistema que registra los cambios realizados sobre un archivo o conjunto de archivos a lo largo del tiempo, de modo que puedas recuperar versiones específicas más adelante

* **Conceptos:**
    *  **Repositorio local**: Es una base de datos centralizado donde se guardan las distintas versiones de los ficheros sometidos a control de versiones.

    * **Copia local**: Es la copia que hacen los usuarios de un fichero sometido a control de versiones. El **DIRECTORIO LOCAL (working directory/working tree/workspace)** es el que contiene todas las copias locales. 

    * **Repositorio remoto**: Es una base de datos centralizada donde se guardan las distintas versiones de los ficheros sometidos a control de versiones, y reside en el servidor centralizado. 

    * ***Log***:  Registro de todos los cambios que se han producido en el repositorio. Es responsabilidad del cliente añadir información al log cuando se produce un cambio. También llamado histórico.

    * **Conflicto**: Problema que surge cuando los clientes realizan cambios incompatibles entre sí.
    
* **Operaciones**:
    * **Clone**: Realiza una copia de un repositorio remoto en un directorio local.
    
    * **Add**: Añade un archivo al siguiente commit.
    
    * **Commit**: Confirma los cambios en el repositorio local.
    
    * **Push**: Envía al repositorio remoto los cambios correspondientes a los commits realizados desde el último push.
    
    * **Pull**: Descarga desde el repositorio remoto los archivos actualizados en commits que hayan realizado otros usuarios, y los integra (realiza un merge) con el repositorio local.
    
    * **Fork**: Crear una copia de un repositorio. Esto es especialmente útil para modificar proyectos sin afectar al proyecto original.
    
    * **Pull Request**: Petición de un pull, para que un nivel superior a una rama u otra rama distinta incorpore cambios (commits) de esta.
    
* **Servicios de repositorio remoto**: GitHub, GitLab, BitBucket, etc.

* **Clientes gráficos para el control de versiones**: gitg, gitkraken, gitblade, etc.

## 2. Comandos

Consideraciones generales:
* **\*** : es sustituido por una lista con todos los nombres de lo ficheros del directorio actual.
* **..** : directorio padre.

### 2.1. Comandos básicos del terminal

Comando    | Argumentos              | Función 
-----------|-------------------------|------------
**pwd**    |                         | Muestra el directorio actual (Print Working Directory).
**mkdir**  | &lt;dir>                | Crea un directorio.
**cd**     | &lt;dir>                | Cambia de directorio (*'cd -': directorio previo*).
**ls**     | [-l] [-a]               | Muestra los archivos del directorio *(l: detallado; a: incluye ficheros ocultos).*
**rm**     | &lt;file>               | Elimina un fichero.
**mv**     | &lt;source> &lt;dest>   | Mueve o renombra un archivo.


### 2.2. Control de versiones local

Comando        | Argumentos         | Función 
---------------|--------------------|------------
**git init**   |                    | Crea un repositorio local en el directorio actual.
**git add**    | &lt;file>          | Prepara ficheros para ser confirmados en un repositorio local.
**git commit** | [-m &lt;message>]  | Confirma cambios en un repositorio local. *(m: permite escribir el mensaje del commit sin abrir el editor de texto).*
**git diff**   | &lt;file>          | Muestra los cambios de un archivo "modificado" con respecto al que hay en el repositorio.
**git reset**  | [--soft]           | Deshace el add. *(soft: deshace el commit)*
**git status** |                    | Muestra el estado actual del repositorio.


### 2.3 Control de versiones centralizado

Comando        | Argumentos                                      | Función 
---------------|-------------------------------------------------|------------
**git config** | [--global][--local] http.proxy &lt;domain:port> | Configura distintos aspectos de git, en todo el PC o en el repositorio actual. Por ejemplo, el servidor proxy.
**git clone**  | &lt;URL>                                        | Realiza una copia de un repositorio remoto en un directorio local.
**git remote** | add &lt;URL>                                    | Enlaza nuestro repositorio local con un repositorio remoto, donde se subirán los cambios al realizar push.
**git pull**   | &lt;remote> &lt;branch>                         | Descarga los archivos actualizados del repositorio remoto y realiza un merge entre el repositorio local y el remoto.
**git merge**  | &lt;branch>                                     | Incorpora los cambios  realizados en los commits de otra rama al repositorio local.
**git push**   | &lt;remote> &lt;branch>                         | Actualiza el repositorio remoto con los cambios realizados en los commits locales que se han realizado desde el último push.


### 2.4 Control de versiones distribuido

Comando              | Argumentos                   | Función 
---------------------|------------------------------|------------
**git branch**       | &lt;branch_name>             | Crea una rama nueva en el repositorio local.
**git checkout**     | &lt;branch_name>             | Cambia de rama en el repositorio local.
**git push**         | [-u] &lt;remote> &lt;branch> | Envía la rama al repositorio remoto.

Operaciones de Github:

Operacion                                 | Descripción
------------------------------------------|------------
**pull request** (entre ramas)            | En la página principal del repositorio: "New pull request" y se selecciona la rama deseada
**pull request** (entre repositorios)     | Dentro de la misma opción anterior, seleccionando: "compare across forks"

## 3. Formato Markdown (.md)

Comando                |   Función
-----------------------|-------------------------------
**#** (Encabezado)     | Encabezado grande.(Va precedido de una sola almohadilla)  
**##**(Encabezado)     | Encabezado segundo mas grande.(Va precedido de dos almohadillas)
**####**(Encabezado)   | Encabezado mas pequeño.(Va precedido de cuatro almohadillas)                       |
un* un* (estilo)           | Las palabras que queden comprendidas entre estos asteriscos aparecerán en cursiva.
dos* dos* (estilo)         | Las palabras que queden comprendidas entre estos dos asteriscos aparecerán en negrita.
tres* tres* (estilo)       | Las palabras que queden comprendidas entre estos tres asteriscos aparecerán en negrita y cursiva. 
** _ _ ** (estilo)     | Las palabras que queden compendidas entre los asterisco apareceran en negrita y las que quedan comprendidas entre los guiones bajos, a parte de negrita aparecerán en cursiva.
~~ ~~ (estilo )        | Las palabras que van comprendidas entre los apostrofes  aparecerán tachados.                       |
> (citas)              | El simbolo de mayor se utiliza para citar una frase.
'' (citas)             | Las comillas simples se usan para citar comandos.                       |
[]() (enlaces)         | Esto sirve para hacer un hipervinculo, entre los corchetes hay que poner las palabras que queremos que aparezcan como enlace y entre los parentesis la dirección a la que nos mandara.                       |
![]()(imagenes)        | Esto sirve para poner una imágen, poniendo la exclamacion lo primero, entre corchetes el texto alternativo y entre parentesis el enlace de la imágen.                       | 
*, -, número           | Usando cualquiera de los tres puedes crear una lista. Si dejas una sangria combinando estos simbolos se crearán listas anidadas. 
