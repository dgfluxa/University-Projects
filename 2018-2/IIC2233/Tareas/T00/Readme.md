# Tarea 00: DCCorreos

## Consideraciones generales 

Tras ingrasar a un usuario válido se dan las opciones de crear correo (crear nuevo correo), ingresar a la bandeja de entrada (leer correos recibidos), e ingresar al calendario. Dentro de este ultimo es donde se pueden realizar todas las acciones referentes a eventos.

Inicialmente se mostrarán los eventos por orden de creación del más reciente al más antiguo y luego se da la opción de filtrarlos de acuerdo a lo que quiera el usuario.

Se pueden filtrar los eventos por más de una categoría pero debe ir creandose el filtro de a uno (Aparecerán los eventos filtrados de acuerdo al primer parámetro y luego se debe volver a seleccionar filtrar eventos para agregar otro).

Al filtrar eventos por fecha se considera la fecha de inicio y se dará la opción de filtrar solo por año, año-mes, y año-mes-día (para esto se pedirá ingresar año, mes y dia por separado).

Al ingresar a un evento en la lista de eventos filtrados se volverá al calendario con todos los eventos.

Al crear un correo o evento no se puede salir hasta el final donde se da la opcion de guardar y enviar o borrar.

El programa indica que acciones se pueden utilizar en cada momento y controla que los inputs ingresados sean válidos.

Referencias a código externo u otros dentro del código como comentarios.

Ningun archivo excede las 600 lineas de código.

Al parecer se encuentra todo implementado correctamente, y el programa en consola es a prueba de errores.

Respetado PEP8.


### Cosas implementadas y no implementadas :white_check_mark: :x:

* Registro e inicio de sesión: Hecho completo
* Correos: Hecho completo
* Calendario: Hecho completo
* Encriptación: Hecho completo

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```Tarea_0.py```


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```collections```-> ```namedtuple (Módulos: crear, eventos_1 y eventos_2), defaultdict (Módulos: crear, eventos_2)```

2. ```datetime```-> ```datetime (Módulo: crear), timedelta (Módulo: eventos_1)```

3. ```random```-> ```randint (Módulo: correos)```

...

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```crear```-> Contine funciones para leer archivos y crear estructuras de datos que serán utilizadas posteriormente a partir de estos. También contiene namedtuples Correo y Evento.

2. ```verificar```-> Contiene funciones que cumplen el fin de verificar y comprobar usuarios, contraseñas, fechas, entre otros.

3. ```correos```-> Contine las funciones básicas para el funcionamiento de la bandeja de entrada y la creación de correos.

4. ```eventos_1```-> Contine parte de las funciones para el funcionamiento de el calendario, que serán importadas en eventos_2.py para definir las funciones finales. También contiene namedtuple Evento.

5. ```eventos_2```-> Contine las funciones finales para el funcionamiento del calendario, que serán importadas al módulo principal. También contiene namedtuple Evento.

...

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. No se utilizarán comillas simples al crear un correo o crear/editar un evento. Es válido debido a que se mencionó en el issue #152

2. En el archivo db_emails.csv los correos enviados se encuentran ordenados del más antiguo al más reciente. Es válido ya que se mencionó en el issue #36

3. De manera similar al punto anterior, se considera que en el archivo dv_events.csv los eventos se encuentran por orden de creación del más antiguo al más reciente. Es válido debido a que se asemeja a lo mencionado en el issue #36 pero aplicado a eventos.


## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. https://stackoverflow.com/questions/47676424/python-3-6-converting-8-bit-binary-to-decimal (binario_a_numero): este transforma numeros binarios de 8 digitos a numeros enteros, está implementado en el archivo crear.py linea 195 al definir la funcion binario_a_numero, y en el archivo correos.py se utiliza en la linea 53 para decodificar el mensaje de binario a ASCII.

2. ord(caracter) encontrado en https://stackoverflow.com/questions/227459/ascii-value-of-a-character-in-python: Entrega ASCII del caracter. Utilizado en el archivo correos.py linea 8 en la codificación para transformar cada caracter del cuerpo del correo en su código ASCII.

3. '{0:08b}'.format(num) encontrado en https://stackoverflow.com/questions/10411085/converting-integer-to-binary-in-python: Transforma un número(ASCII) a binario de 8 digitos. Utilizado en el archivo correos.py linea 8 en la codificación para transformar el código ASCII de cada caracter del cuerpo del correo en un binario de 8 digitos.

4. chr(ASCII) encontrado en https://stackoverflow.com/questions/227459/ascii-value-of-a-character-in-python: Entrega caracter del código ASCII. Utilizado en el archivo correos.py linea 56 en la decodificación para transformar el código ASCII entregado a su carácter equivalente.

5. http://www.linuxhispano.net/2016/11/24/calcular-ano-bisiesto-python-3/ (año_bisiesto): Retorna True si el año ingresado es bisiesto y False si no lo es. Implrmrntado en el archivo verificar.py linea 105 al definir la función año_bisiesto, y en la linea 163 del archivo verificar.py para revisar si el año ingresado es bisiesto en caso de que se haya ingresado el dia 29 de febrero.

6. En archivo correos.py linea 157 hay código recuperado en parte de Tarea 3 IIC1103, 2017, Diego Fluxá.


