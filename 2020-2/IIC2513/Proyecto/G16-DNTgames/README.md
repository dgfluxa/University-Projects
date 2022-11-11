# Grupo 16 "DNTgames" - Tarea 6
### PUC IIC2513 - Tecnologías y Aplicaciones Web - Repositorio de Proyecto de Curso
## Integrantes

| Nombre                | Email       | Usuario de Github |
|:--------------------- |:-------------|:-------------|
| Tairon Garrido | tngarrido@uc.cl | [@tngarrido](https://www.github.com/tngarrido) |
| Nicolás Karlezi | nkarlezi@uc.cl | [@nkarlezib](https://www.github.com/nkarlezib) |
| Diego Fluxá | dgfluxa@uc.cl | [@dgfluxa](https://www.github.com/dgfluxa) |

## Enlace Repositorio backend: https://github.com/PUCIIC2513/2020-2-G16-DNTgames-backend
## Descripción de la distribución del repositorio

El repositorio esta constituido en primer lugar por una carpeta documents la cual contiene nuestra Tarea 1, el archivo de protocolo, **el diagrama E/R de la Tarea 6** y la documentación de la API de la Tarea 5. \
Además existe un archivo llamado index.html que corresponde a la "landing page" de nuestra aplicación web. Luego, existe una carpeta llamada src que dentro de ella esta la carpeta views la cual contiene todos los archivos .html de las distintas secciones de la pagina. También en src se encuentra la carpeta assets que contiene 2 carpetas: assets, donde está la carpeta con todas las imágenes utilizadas en la pagina,  carpeta styles que contiene todos los archivos CSS que le dan estilo a la pagina y la carpeta scripts con todos los archivos .js, y la carpeta views que contiene todas los documentos HTML de la aplicación.
A continuación se muestra la organización de nuestro repositorio:

+-- documents/ \
+-- src/ \
|   +-- assets/ \
|    |  +-- imagenes/ \
|    |  +-- scripts/ \
|    |  +-- styles/ \
|    +-- views/ \
+-- index.html \
+-- index.js \
+-- views.html \
+-- .gitignore \
+-- README.md

## Novedades Tarea 6
Para esta sexta Tarea, se han arreglado detalles del proyecto y mejorado su documentación para darle un cierre.

Se arreglaron múltiples detalles en las vistas de index, reglas, espera de partida y juego principalmente.

Se esconde el botón de "Continuar partida" si el jugador no posee una partida activa.

Sincronizados tiempos de jugadores y actualizados nombres en el lobby de espera para la partida.

Se ha mejorado la documentación de nuestra API , donde se muestran todas las rutas del servidor con su explicación para un correcto funcionamiento (Enlace disponible más abajo).

Se ha actualizado el Modelo de Entidad-Relación (Disponible en carpeta documents del repositorio).

Para ejecutar la aplicación (lado cliente) debe crearse un servidor local utilizando index.html como página de inicio. Desde ahí, se podrá navegar por toda nuestra aplicación web de una manera fácil e intuitiva. Para esto se puede y se recomienda utilizar live-server (disponible como add-on de Visual Studio Code).

## Enlace Repositorio Backend: 
https://github.com/PUCIIC2513/2020-2-G16-DNTgames-backend

## Enlace Servidor: 
https://dntgames.herokuapp.com

## Enlace Documentacion API:
https://documenter.getpostman.com/view/13716573/TVmMfxbL#b8373ae7-4cd5-4b75-98c0-dbef21175899

## Descripción del proyecto

Nuestro proyecto consiste en una aplicación web en la cual se podrá jugar un videojuego multijugador basdo en turnos.

El objetivo del juego es poseer la mayor cantidad del mapa conquistado cuando se terminen los turnos determinados al crear la partida. En caso de que exista un empate, ganará el con más dinero y si también empataran en esto ganará quien haya creado la partida.

Actualmente, para nuestra Tarea 6, hemos implementado todo lo relacionado al diseño de la página, es decir, archivos .html para la estructura y archivos .css para el estilo de las páginas. Además se implementó funcionalidad mediante archivos .js, con el fin de habilitar el inicio de sesión, registro de usuario, la navegación para hacer y enviar una jugada. Luego, se implementó un servidor y una base de datos anclados en heroku los cuales sirven para llevar a cabo los procesamientos y distintas funcionalidades necesarias para la aplicación. Por último, se utilizó JWT para implementar tokens para el manejo de sesiones.

## Tecnologías empleadas

En esta entrega, como hemos mencionado, se aplicó HTML, CSS y Javascript para desarrollar la capa visual de nuestra aplicación web y ciertas funcionalidades de manera local. También se implemento un servidor y una base de datos anclados en Heroku para realizar el procesamiento de las jugadas y el inicio y cierre de sesión (manualmente).

Primero, con respecto al HTML, solo se utilizaron elementos relacionados con la estructura de la página, de entre los cuales se pueden mencionar div, a href=.., span, p, li, img src=..., entre otros.
  
Luego, con respecto a CSS, solo se utilizaron elementos para darle el diseño deseado a nuestros elementos de los archivos .html. Algunos de estos elementos corresponden a hover, focus, grid, background, borders, transitions, entre otros.

Además, con respecto a Javascript, se utilizaron múltiples elementos para otorgar funcionalidad a nuestra página y, de esta mnanera, hacerla interactiva. Algunos de estos elementos y funcionalidades corresponden a localStorage para almacenar información de manera local, funciones, manejo de flujo, JQuery, document.createElement(), documento.getElementById(), funciones de JSON para transformar elementos a JSOn y parsear elementos JSON, funciones de Math, entre otros.

También, se implementó un servidor y una base de datos desplegados en Heroku. Para el servidor, se utilizó Nodejs, Koa y Sequelizer para su implementación. En cuanto a la base de datos, se utilizó Postgresql mediante Heroku Postgres. En cuanto al manejo de sesiones, se utilizó koa-session y bcrypto para encriptar las contraseñas de los usuarios.

Se utilizaron endpoints para realizar la comunicación del lado del cliente con el servidor.

Se utilizó Bearer Token con JWT para implementar el manejo de sesiones.

## ¿Cómo ejecutar la aplicación?

Para ejecutar la aplicación debe crearse un servidor local utilizando index.html como página de inicio. Desde ahí, se podrá navegar por toda nuestra aplicación web de una manera fácil e intuitiva.

Puede ser de interés mencionar que al realizar nuestra aplicación se utilizó live-server (la versión add-on de vscode), razón por la cual se recomienda su utilización.

## Navegación por la aplicación

Al ingresar al landing page de nuestra aplicación web (index.html), se encontrará con una página de bienvenida que posee una barra de navegación superior para moverse a distintas secciones de la aplicación, una columna lateral a la izquierda con enlaces a otras secciones representados por imágenes, un botón para comenzar a jugar, una sección de motivación bajo el mensaje de bienvenida y finalmente una sección de "Nosotros", donde se presenta el grupo con su número, nombre e integrantes, donde se podrá ingresar a sus respectivos perfiles de github al hacer click en sus usuarios que se encuentran entre paréntesis.

Para la página de juego (index -> jugar -> continuar partida) , se muestra un mapa y dos barras laterales, a la izquierda y derecha. 
En la barra izquierda se muestra el estado dentro del juego del usuario que esta jugando y a en la derecha todas aquellas opciones que pueden realizar. Es importante mencionar que, al implementar javascript, se limitará el uso de estos botones para cuando se puedan realizar de acuerdo a las reglas del juego.

Luego, en el mapa se puede observar un sector sombreado debido a que el jugador no ha avanzado lo suficiente para visualizarlo, multiples casillas en azul que corresponden a aquellas donde se puede mover el ejército del usuario (simbolizado por una estrella verde en el mapa aen la esquina inferior derecha) y al realizar hover y click en estas cambiarán a color rojo para seleccionarla. Además, se presenta un icono de cada tipo de lugar y el icono del ejército, donde se puede realizar hover para que se destaquen y se muestre su nombre. Tanto para los iconos de los poblados y del ejército, estos tomarán el color del jugador al cual pertenecen, y, n el caso de los poblados, si aún no pertenecen a ningún jugador serán de color gris.

Por último, bajo el mapa, se encuentra el botón que para terminar el turno del jugador, donde al apretarlo se mostrarán otros dos botones "Modificar jugada" y "Mostrar resultados". Al presionar el primero, se podrá modificar desde el principio la jugada recién realizada, mientras que con el segundo se enviará al servidor que procesará la jugada y luego se mostrarán los resultados en la pantalla. Tras esto, se tendrá que esperar a que el siguiente jugador realice su jugada para poder continuar

El ingreso a la página de perfil se puede realizar tras haber ingresado a un usuario mediante el link que aparecerá en el navbar o mediante la página "juego" o "crear_partida" al hacer click en la imagen de perfil. En este tambien podemos ver las partidas ganadas, perdidas y el ranking del jugador, todo respecto a su historial que se encuentra guerdado en la base de datos.

## Ingreso, Registro de Usuarios y partidas

En la esquina superior derecha, si es que aún no se ha ingresado a un usuario, se pueden encontrar dos links "Iniciar Sesión" y "Registrarse" que te llevarán a las páginas para realizar el ingreso a un usuario ya creado y a crear un usuario del juego, respectivamente. Estas cuentas serán almacenadas en la base de datos del servidor, por lo que uno puede ingresar a una cuenta previamente creada. Si un jugador crea una partida, esta de inmediato quedara almacenadas en la base de datos junto a todas las partidas creadas con toda la informacion necesaria de la partida. De este modo, al ir a la seccion de unirse a una partida, aparecerán todas las que estan creadas y nos ofrecerá la opción de unirnos, lo que lleva a la sala de espera, con todos los jugadores que están esperando a que comience la partida. P

Si vamos a la seccion de mejores jugadores tambien aplicamos funcionalidades de javascript para mostrar todos los jugadores existentes en la base de datos con su respectiva informacion y ranking en el juego, permitiendo una interacción mas completa y entretenida entre todos los usuarios. 

Por último la sección de novedades tambien recivio algunas implementaciones. Ahora esta totalmente conectada los eventos que suceden en el juego. Por ejemplo cambios relevantes en el ranking de mejores jugadores.

## Realizar una jugada

Actualmente, en el juego se puede realizar y enviar una jugada en partidas de 2 jugadores donde los lugares serán distribuidos aleatoriamente.

Para realizar una jugada, uno comienza en la esquina inferior derecha. Desde aquí uno puede comprar unidades sin la necesidad de moverse previamente. Además, al seleccionar el botón "moverse" se mostraran las casillas disponibles para el movimiento en color azul y al seleccionar una se tornará roja para indicar que uno se moverá a esta. Además, en caso de seleccionar un lugar, se habilitarán los botones correspondientes a las acciones que se pueden realizar en estos. Estas son:
- Minas: Interactuar 
- Bosques: Interactuar
- Ruinas: Interactuar
- Poblados Neutros: Conquistar y Comprar
- Poblados Conquistados: Interactuar (Para invadir)
- Fortaleza: Comprar

Otras consideraciones:
En todo momento uno puede seleccionar el botón de curar y el próximo turno sus doctores procederan a curar al ejército en una cantidad que depernderá del número de doctores.
Si se termina un turno en la fortaleza, el ejército se recuperará 1500 puntos de vida
Al utilizar la acción de "interactuar" existe la posibilidad de que no sea exitoso y se dañe al ejército.

Al presionar "Terminar Turno" se mostrará un resumen del turno y al cerrar esta ventana se encontrará con las opciones de modificar turno, donde se podrá reiniciar dicho turno para volver a realizarlo, y mostrar resultado, donde se enviará la jugada el servidor y se mostrará el resultado de las acciones en la jugada.

Al seleccionar "Mostrar resultado" se mostrará un mensaje con los resultados de la jugada realizada por el jugador. Después de cerrar esta ventana, habrán cambiado todos los stats y carácteristicas del mapa de acuerdo con los resultados y, luego que el otro jugador realice su jugada, se podrá realizar una nueva jugada desde ese punto.

Es importante mencionar que se podrá salir de la pantalla del juego y la partida continuará como la dejaste.

Luego de que concluyan los turnos, se mostrará al ganador con el número de poblados que posee y se podrá salir de la partida. Una vez que se sale de esta, no se podrá volver.

## Otros

## Novedades Tarea 5
Para esta quinta Tarea, se ha implementado la conexión entre servidor y cliente.

Además, se ha utilizado JWT para el manejo de sesiones.

Se han habilitado las interacciones con ruinas y para atacar poblados conquistados por otros usuarios. También, se ha habilitaado el multijugador para 2 jugadores.

Se han realizado algunos cambios a las reglas. Estos son:
- Multijugador de sólo 2 jugadores
- Vida perdida al ganar un enfrentamiento es directamente 0,4 * j2
- Poblados solo se pierden al morir
- Unidades mueren al perder enfrentamientos o al morir
- Al ganar un combate, la vida mínima con la que se puede quedar es 1
- Eliminadas partidas privadas

Para ejecutar el juego, debe ejecutarse un servidor local con los archivos de este repositorio (lado cliente) con index.html como landing page.

## Novedades Tarea 4
Para esta cuarta Tarea, se ha implementado un servidor y una base de datos desplegados en heroku para realizar el procesamiento de las jugadas. Por esta razón, se ha deshabilitado la simulación automática de las jugadas desde el lado del cliente. Por lo tanto, esto se debe realizar manualmente de manera cuidadosa utilizando la consola del navegador y el localStorage para que se muestre el resultado de la jugada correctamente (Ver sección "Simular una jugada"). 

Las reglas se han modificado levemente, cambiando el tiempo de partida, es decir el tiempo que estaba definido para que terminara la partida y se definiera a un ganador, por un número de turnos de la partida que corresponderán al número de turnos que durará esta. Es decir, cuando se realice el número de turnos establecidos a un inicio, se terminará la partida y se definirá al ganador.

Además, se pueden crear usuarios, iniciar y cerrar sesión mediante el servidor. Esta funcionalidad se implementó utilizando koa-sessions y bcrypt.

## Cambios de las reglas iniciales
- Multijugador de sólo 2 jugadores
- Vida perdida al ganar un enfrentamiento es directamente 0,4 * j2
- Poblados solo se pierden al morir
- Unidades mueren al perder enfrentamientos o al morir
- Al ganar un combate, la vida mínima con la que se puede quedar es 1
- Eliminadas partidas privadas
- Tiempo de partida cambiado por número de turnos 
- En caso de empate gana el jugador con mas dinero y si empatan en esto se elije al primero que se haya unido a la partida
- No se agotan los recursos
- No se puede abandonar una partida
- No se muestra el ranking en la vista del juego 
- Se eliminaron enfrentamientos entre directos (Se enfrentarán sólo mediante invasiones a poblados conquistados)
