# Guia de instalación de la aplicación web Mentor Mirror (1.0)
En el presente documento se muestra como es el procedimiento de instalación del aplicativo Mentor Mirror mediante una serie de comandos preestablecidos.

## Instalación de Python 3.8.10
Mentor Mirror trabaja sobre la versión 3.8.10 de Python por cuestiones de librerias, es necesario ir al siguiente enlace y descargar el instalador (Dependiendo del sistema operativo y su arquitectura):

[Python 3.8.10](https://www.python.org/downloads/release/python-3810/)



## Instalación de compilador C++
Para la correcta ejecución de la aplicación, es necesario contar con el compilador de C++ en nuestro entorno; la libreria de face recognition hace uso de la libreria dlib, y está a su vez está compilada en C++, por lo que es necesaria la instalación del compilador.

### Pasos para la instalación
1. Entrar al siguiente enlace de Microsoft: [Visual Studio Downloads](https://visualstudio.microsoft.com/es/downloads/)
2. Descargar la versión comunidad de Visual Studio.
3. Una vez descargado, abrir el .exe y esperar que se prepare el instalador.
4. Con el instalador listo, nos desplazamos a la sección de móviles y escritorio y seleccionamos desarrollo para el escritorio con C++. (Importante tener espacio en el disco)
5. Click en el botón instalar ubicado en la parte inferior derecha y esperar que termine la instalación.

## Instalación de librerias y entorno virtual
El aplicativo Mentor Mirror está compuesto por una variada cantidad de librerias, para esto es necesario instalar estás dentro de un entorno virtual.

### Creación del entorno virtual
Para la creación del entorno virtual, necesitamos de la libreria de virtualenv, para instalarla, se necesita entrar al terminal (CMD) e introducir el siguiente comando:

- `pip install virtualenv`

Instalada la libreria, se procede a entrar a la ruta dónde está ubicado el aplicativo web haciendo uso del terminal:

* Ruta de ejemplo
    `cd C:/Usuario/Carpeta/MentorMirror`

Cuando se esté úbicado en la ruta del aplicativo, se ejecuta la siguiente linea de comando:

- `python -m venv .venv`

Una vez creado el entorno, se accede a la ruta de este para activarlo, la linea de comandos es la siguiente:

- `cd .venv/Scripts`
- `.activate`
- `cd..`
- `cd..`

### Instalación de librerias
Con la activación anterior del entorno, se procede con la instalación de las librerias necesarias para el funcionamiento del aplicativo web, para esto, hay un archivo pre-definido en formato .txt llamado *requisitos*, el cual contiene las librerias y sus respectivas versiones, para proceder con la instalación, se procede en el terminal con el siguiente comando:

- `python -m pip install -r requisitos.txt`

Ejecutado el comando, se procede con la instalación de cada una de las dependencias, el proceso demorará dependiendo de la red

## Ejecución del aplicativo web Mentor Mirror
Después de haber seguido todo lo anterior, se procede con la ejecución del aplicativo, para eso, se hace uso del terminal nuevamente dentro de la ruta del proyecto (Necesario tener el entorno activado), se introduce el siguiente comando en el terminal:

- `python manage.py runserver (número de puerto opcional)`

El aplicativo realizará comprobaciones del sistema, y si todo está bien, ejecutará el servicio web en un servidor de pruebas (Normalmente, el host local).

* Dirección (Por defecto): 
    http://127.0.0.1:8000/
