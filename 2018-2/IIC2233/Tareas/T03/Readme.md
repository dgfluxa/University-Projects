# Tarea 03: Electromatic

## Consideraciones generales 

Se calcula la demanda de las elevadoras y luego lo que se pierde en las conexiones con sus padres con el fin de optimizar, pues calcular la demanda de cada central se demoraba mucho.

Al agregar un nodo se asumirá que se ingresará una comuna y provincia existente aun cuando esta no exista en la vida real.

La funcion crear_list_sist tiene como función esta funcion existe por si existiera un nodo sin padres en el sistema, con el fin de que este no afecte el calculo de la demanda.

Importante: Tenía un error en el que se me reiniciaba la lista con las entidades, el cual se soluciona implementando deepcopy para copiar la lista de nodos en el atributo nodos_activos de la clase RedElectrica. El problema es que al utilizar las bases de datos grandes se provoca una recursion que manda un error de programa por lo que hay que realizarlo sin este deep copy (para esto se puede buscar deepcopy y borrar todas las menciones, que no son muchas y estan solo en el archivo clase_grafo.py, pero no se podrán realizar todas las modificaciones a la red, pues se eliminarán todos los nodos inactivos.

Cuando se selecciona realizar prueba en el menú se crea una red secundaria, que después de cada prueba se imprimen los nodos, nodos activos, demanda total y oferta total debido a que no se especificaba en el enunciado. Esta red secundaria también se puede reiniciar, lo que provoca que la red secundaria se iguala a la red real.

El programa indica que acciones se pueden utilizar en cada momento y controla que los inputs ingresados sean válidos.

Referencias a código externo u otros dentro del código como comentarios.

Ningun archivo excede las 600 lineas de código.

Respetado PEP8.


### Cosas implementadas y no implementadas :white_check_mark: :x:

(A partir del feedback)

* Red: Hecho completo
* Calculo potencia: Hecho completo
* Consultas: Hecho completo
* Excepciones: Hecho completo
* Testing: Incompleto. Se empezó a escribir pero no está terminado.

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```copy```-> ```deepcopy (Módulo: clase_grafo)```

2. ```abc```-> ```ABC (Módulo: clases)```

3. ```csv```-> ```reader (Módulo: funciones)```

4. ```sys```-> ```exit (Módulo: funciones)```

5. ```unittest```-> ```(Módulo: testing)```

6. ```os```-> ```(Módulo: testing)```

...

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```estructuras```-> Contiene clases para modelar las estructuras de datos.

2. ```clase_grafo```-> Contiene la clase de RedElectrica utilizada para modelar la red.

3. ```clases```-> Contine las clases utilizadas para simular las entidades presentes en la red.

4. ```funciones```-> Contine funciones que permiten el funcionamiento de la red.

5. ```excepciones```-> Contine las excepciones personalizadas para esta tarea.

6. ```consultas```-> Contine las funciones utilizadas para las consultas.

...

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. Contenidos IIC2233 semana 06: utilizado en parte para realizar la clase Lista.

2. Contenidos IIC2233 semana 02: utilizado para crear la clase Iterador.

3. Ayudantía 8 IIC2233: utilizado en parte para el testing.

