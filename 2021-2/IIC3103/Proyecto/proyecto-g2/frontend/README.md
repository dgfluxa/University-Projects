# Frontend Proyecto IIC3103 Grupo 2
## Link Heroku: https://proyectoiic3103g2.herokuapp.com/
## Ejecutar localmente:
Para ejecutar el proyecto localmente se deben realizar los siguientes pasos:

`yarn` o `yarn install` para instalar todas las librerías necesarias

`yarn start` para iniciar el servidor local en localhost:3000

**Importante que corra en el puerto 3000 debido a que es el único habilitado por la API de Django sin levantar CORS ERROR**

Además, se debe correr el backend localmente en el puerto 8000. Cuando se conecte al servidor, se puede cambiar la API_URL de variables.js para conectarlo al almacen.

## Consideraciones:
- Se utilizó Material UI v4
- Para realizar el deploy a Heroku se debe correr: ` git subtree push --prefix frontend heroku main `
- La página de Heroku no posee la conexión al backend. Se agregará cuando se suba este al servidor.
