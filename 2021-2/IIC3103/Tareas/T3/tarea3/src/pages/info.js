import React from 'react';
import { Typography } from '@material-ui/core';
import 'leaflet/dist/leaflet.css'

function Info() {

  return (
    <div>
      <div style={{marginTop: '2%', marginBottom: '5%'}}>
        <Typography variant="h3">
            Información
        </Typography>
        <Typography style={{marginTop: '3%', marginLeft: '10%', marginRight: '10%'}} variant="subtitle1">
          En la página de Inicio se encuentra todo lo solicitado para la tarea, es decir, el mapa con los camiones, 
          la información detallada de los camiones y el centro de control. Estos pueden ser accedidos mediante la barra de navegación superior. 
          Se puede acceder a la página de Inicio al hacer click en "Tarea 3" en la barra superior, o en alguno de los botónes a la derecha de la barra 
          a expeción de "Información", que conduce a esta página. A continuación se presentan algunas consideraciones de la tarea para entender su uso 
          y los supuestos realizados. 
        </Typography>
        <Typography style={{marginTop: '3%', marginLeft: '10%', marginRight: '10%'}} variant="subtitle1">
          Para el "Mapa", cada ícono corresponde a un camión y al hacer hover con el cursos sobre este se despliega su información (código y posición).
          Además, las lineas rojas representan la ruta de un camión al conectar sus puntos de origen y de destino. Por su parte, las lineas verdes correponden
          al camino que ha recorrido un camión desde que se conectó a la página web (conexión al websocket). Estas líneas verdes podrían demorar un tiempo en 
          ser visibles, pero al hacer zoom puede ser más fácil divisarlas. Al hacer hover sobre ambas líneas se púede obtener información detallada de estas con
          el código de camión asociado, Origen y Destino para roja y Posición inicial y actual para verde (Actual se refiere a la posición de cuando se conectó
          al websocket. Cabe mencionar que la dirección del ícono de camión no tiene relación con el sentido en el cual se encuentra avanzando, solo es 
          utilizado para representar un camión gráficamente. El centro inicial del mapa corresponde al punto de origen del primer camión enviado por el 
          websocket, por lo que el mapa no se renderizará hasta que se obtenga el primer camión. Por último, los camiones comienzan en su punto de origen 
          y tras recibir un cambio de posición se muestran en su posición actual, por esto se puede ver como si los camiones "saltaran" en un principio.
        </Typography>
        <Typography style={{marginTop: '3%', marginLeft: '10%', marginRight: '10%'}} variant="subtitle1">
          En cuanto a la "Información Camiones", aquí se despliega toda la información de los camiones horizontalmente. Cada cuadrado representa un camión. 
          Si este es verde significa que no presenta fallas y si es rojo si lo hace. En este último caso, se puede ver el mótivo de la falla en la sección de "Estado".
          Para esto, se considera solo el primer evento "FAILURE" recibido desde el websocket para que este motivo no cambie en caso de llegar otro evento para 
          ese mismo camión. Además, dado que la información inicial de los camiones no posee su estado, se asume que todos los camiones comienzan sin fallas.
        </Typography>
        <Typography style={{marginTop: '3%', marginLeft: '10%', marginRight: '10%'}} variant="subtitle1">
          Por último, para la sección de "Centro de Control", uno comenzará como "Anónimo". Por esto, precisará ingresar un nombre en la barra sobre el chat para
          determinar un nickname. Se anuncia en rojo cuando uno está como anónimo. Además, es importante notar que, por el momento, el chat no posee auto-scroll, 
          por lo que uno debe hacer esto manualmente cuando hay muchos mensajes para poder visualizar los nuevos.
        </Typography>
      </div>
    </div>
  );
}

export default Info;