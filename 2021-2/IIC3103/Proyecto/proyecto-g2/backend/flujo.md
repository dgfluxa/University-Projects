- Sistemas de bodegas -> Nos pasan 1.

La bodega tiene 5 componentes (almacenes):
- Recepcion de productos
- Despacho pizzas
- General
- Cocina
- Pulmon (donde vencen)

-Reglas:
- Todos los productos entran por recepcion
- Todos los productos salen por despacho
- Almacenamientos tienen capacidad
- Recepcion y despacho deben estar siempre libres de productos (* Ver caveats, es una recomendacion)

Objetivo Obtener ingredientes para la pizza, pasos:
-  Pedir ingredientes base a la fabrica (llegan despues de X y quedan automaticamente en recepcion)
-  de Recepcion -> General en intervalos de X
-  de General a Cocina (Usar algo para detectar cada Y si podemos cocinar una pizza, si se puede, pasar los ingredientes a la cocina) (Usar una queue para usar los ingredientes más cercanos a vencer)
(Algoritmo para determinar cuando conviene fabricar un componente (antes que se venza), por espacio, es por tiempo de vencimiento y para poder preparar una pizza) 
-  Cocinar -> Si es componente a General, Si es pizza a despacho

* ESTO ES POR AHORA QUE NO HAY DESPACHO NI SOLICITUD DE COMPONENTES A GRUPOS

Ingredientes:
- Base (se piden a la fabrica)
- Componentes (se cocinan con los base)
- Pizzas

Entregables:
- GET DE STOCK
- POST/PUT DE ORDENES (BDD)
- Elaborar pizzas
- Fabricar 10 SKUS y despachar

######################################################
## Ciclo de vida de una orden de compra

0. PASANDO A PROD O EN DEV, BORRAR TODOS LOS ARCHIVOS

1. Llega orden de compra por sFTP
- Detectar orden nueva cada X minutos, con updater.
- Aceptar o rechazar orden (según posibilidad de cumplimiento en X horas)

*En almacen general, tenemos ingredientes para hacer de todo.

2. Empezar a fabricar EJ: 5 Pizzas de aceituna
Threads ->->->-> 
- Se ejecuta un thread cocinar_pizza_tipo_x que se encarga de, mover, cocinar, esperar, y mover a despacho, y despachar.

## VER COMO HACER QUE CIERTOS SCHEDULERS PARTAN DPS DE CIERTO TIEMPO
por tema de que la base de datos se reiniciara despues de la fecha entrega.


* Hay que hacer migracion al crear nuevas BDD
## POR HACER ENTREGA 3

### RECIBIR ORDENES
- Poder recibir ordenes de compra por API de otros grupos (ingredientes, rechazar si son pizzas).
- Guardar en DB. (PSQL ver como usarla con django)
- Aceptar o rechazar, haciendo patch a ENDPOINT,
- Mandar las cosas -> Mover a despacho y de despacho, "despachar" al grupo.
* FALTA SOLO TESTEAR PARSER DE FECHA | DEFINIR CUANDO RECHAZAR

### ENVIAR ORDENES
- Crear y enviar ordenes a otro grupo por API.
- request a API Profe (crear orden, quiza retorna la info) y Api grupo (enviar orden)  
- ENDPOINT de otro grupo (url_grupo/ordenes-compra/id_compra) con data {}
- Habilitar ENDPOINTS de recibir (copiar clase de OC, y que sea endpoint nuevo)
- Esta en URLS.py la direccion del endpoint
- Ahora esperar el PATCH con aceptar o rechazar.
En oc.py se encuentra, y una func en utilities.py
* FALTA: 
- Crear dict, de SKU -> [URL de Grupos con el SKU]
- Como obtener nuestra Group ID.
- Como obtener el ID de un grupo en base a la URL
- Como manejar cuando nadie tiene el SKU.

POR HACER
- Agregar más pizzas
- Tenemos que ver si es posible fabricar una pizza, ya que si los grupos no nos envian los ingredientes, no podremos fabricar ciertas pizzas. Para eso checkear con un contador los ingredientes base necesarios (que no se cocinan) que esten en el almacen general, sino rechazar la orden.

- Endpoints dashboard