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

## 3. Uso del formato .md

### 3.1 Definición

El **Markdown** es un lenguaje de marcado con sintaxis en texto plano para generar textos con formato.

Los archivos en Markdown se guardan con la extensión <code class="language-plaintext highlighter-rouge">.md</code> y se pueden abrir en cualquier editor de texto. 

### 3.2 Uso del lenguaje Markdown

#### 3.2.1 Encabezados

Markdown dispone de cuatro niveles de encabezados definidos por el número de <code class="language-plaintext highlighter-rouge">#</code> antes del texto del encabezado.

| #     | Primer nivel de encabezado    |
| ##    | Segundo nivel de encabezado   |
| ###   | Tercer nivel de encabezado    |
| ####  | Cuarto nivel de encabezado    |

#### 3.2.2 Párrafos y saltos de línea

Los párrafos son simplemente texto plano escrito sin ninguna peculiaridad propia del lenguaje, para escribir un párrafo simplemente teclea como lo haría en un archivo <code class="language-plaintext highlighter-rouge">.txt</code>. 



De igual modo, para un salto de línea simplemente hay que introducir un salto de línea como lo haces normalmente en cualquier editor de texto como puede ser **Microsoft Word**, pulsando el botón <code class="language-plaintext highlighter-rouge">Enter</code> de tu teclado. Este párrafo por ejemplo, tiene tres saltos de línea de separación en lugar de uno con respecto al anterior.

El texto se puede poner en cursivas encerrándolo entre los símbolos <code class="language-plaintext highlighter-rouge">*</code> o <code class="language-plaintext highlighter-rouge">-</code>. De la misma forma, el texto en negritas se escribe encerrando la palabra entre <code class="language-plaintext highlighter-rouge">**</code> o <code class="language-plaintext highlighter-rouge">__</code>.

* **Ejemplo de texto en negrita**
* *Ejemplo de texto en cursiva*

#### 3.2.3 Listados

Markdown soporta la creación de listas ordenadas y sin ordenar.

Para la creación de una lista sin orden simplemente debemos utilizar el caracter <code class="language-plaintext highlighter-rouge">*</code> delante del parráfo o línea que queramos listar y un espacio entre el caracter y el texto y, para crear distintos niveles solo tenemos que aumentar la sangría de las líneas. Es tan sencillo como se muestra a continuación:

* Padre
    * Hijo 1
    * Hijo 2
    * Hijo 3
* Madre

Para listas ordenadas es tan sencillo como listar mediante números y un punto, como se muestra a continuación:

1. tarea 1
2. tarea 2
3. tarea 3

#### 3.2.4 Fragmentos de código

Dado que Markdown no distingue las tipografías involucradas los fragmentos de código se representan encerrados entre dos signos de acento grave <code class="language-plaintext highlighter-rouge">`</code>. Y cuando queramos representar un bloque completo de código lo debemos encerrar entre dos líneas de tres acentos graves. 

```
...
Fragmento de código
...
```

#### 3.2.4 Bloques de citas

Los bloques de citas se representan usando el caracter <code class="language-plaintext highlighter-rouge">></code> delante del párrafo que queramos convertir en un bloque de citas. Como se muestra a continuación:

> Éste es un párrafo de texto incluido como un bloque de cita




**Ejemplo de tabla en marcado .md**
| / | Titulo A | Titulo B | Titulo C | Titulo D |
|--:|----------|----------|----------|----------|
| 1 | cell 1,a | cell 1,b | cell 1,c | cell 1,d |
| 2 | cell 2,a | cell 2,b | cell 2,c | cell 2,d |
| 3 | cell 3,a | cell 3,b | cell 3,c | cell 4,d |