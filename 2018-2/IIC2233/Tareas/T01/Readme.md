# Tarea 01: Cruncher Flights

## Consideraciones generales

Se puede cambiar la carpeta de la cual se extraeran los archivos (Para cambiar el tamaño de estos) en la funcion crear_path ubicada en la linea 30 de funciones.py.

Al seleccionar múltiples consultas se considerarán solo los que sean válidos a pesar de que se hayan ingresado datos erróneos.

En favourite_airports, de haber 2 o mas aeropuertos que se hayan visitado la misma cantidad de veces, se retorna el cual esta relacionado a la linea que aparece mas arriba en el archivo flights-passengers2.csv (Lo mismo sucede para otras fucniones en casos similares).

En furthest_distance, se entregarán los primeros (topn) pasajeros, priorizando aquellos que aparezcan antes en el archivo "flights-passengers2.csv"

Respetado PEP-8.

Ningun archivo excede las 600 lineas de código.

Ninguna función supera las 15 líneas de código (No se considera la definicion de la función debido a que se priorizó que estas queden definidas claramente a ahorrar lineas, ya sea utilizando type hinting o variables declarativas. 

Existen comentarios dentro del código.


### Cosas implementadas y no implementadas :white_check_mark: :x:

* Lectura Archivo: Hecho completo
* Consultas: Creadas todas las funciones pedidas.
* Interacción con consola: Hecho completo.
* Uso de Funcional: Respetadas las reglas.


## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  main.py


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```datetime```-> ```datetime (Módulo: funciones.py)``` 
2. ```iic2233_utils```-> ```parse (Módulo: funciones.py), foreach (Módulo: funciones.py)``` 
3. ```itertools```-> ```tee (Módulo: funciones.py)``` 
4. ```collections```-> ```namedtuple (Módulo: funciones.py)``` 
5. ```typing```-> ```Union (Módulo: funciones.py), Generator (Módulo: funciones.py)```
6. ```math```-> ```sqrt, sin, cos, asin (Módulo: funciones.py (Todos))``` 
7. ```operator```-> ```eq, ne, lt, gt (Módulo: funciones.py (Todos))```
8. ```os```-> ```path.isfile (Módulos: main.py y funciones.py)```


### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```funciones.py```-> Contine a las funciones mostrar_menu, abrir_consulta, ingresar_consulta y leer_output, las cuales son implementadas en main.py. Además contiene las funciones solicitadas en la tarea y otras que permiten el correcto funcionamiento del programa.

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

Las consultas se ingresaran correctamente. Es válido debido a que se menciona en el enunciado.

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. https://es.stackoverflow.com/questions/512/c%C3%B3mo-verificar-que-un-archivo-exista-en-python: Aquí encontre la función os.path.isflie(archivo), que permite revisar si existe o no un archivo ingresado.
2. Tarea 00 IIC2233 2018 2° Semestre Diego Fluxá: De aquí rescate la función transformar_a_datetime que cree para la Tarea 00.
