# Repositorio base Tarea 0
Este es el repositorio base para tu tarea 0, en el cual deberás subir tu tarea en la rama **master**.
### Ejecución
Para ejecutar tu programa, se seguirán los siguientes pasos:
1. Clonar tu repositorio
2. Ir a la carpeta principal de tu repositorio
3. Compilar tu programa con `make`
4. Por cada test de input `<input>`:
5.  Ejecutarlo con `./simulate <input> <output>`
6.  Verificar que `<output>` sea **exactamente igual** al output esperado.

En el repositorio viene un ejemplo de archivo de input, y su respectivo output. Puedes comparar tu output con el output esperado, o bien, 
puedes ejecutar el programa en `python3` en la consola `bash` para verificar que tus resultados sean los mismos a los esperados. Un ejemplo con un test:

- Ejecutar `make`
- Ejecutar `./simulate tests/test.txt out_C.txt`
- Opción 1:
  * Ejecutar `python3 python/simulate.py tests/test.txt out_python.txt`
  * Ejecutar `diff --strip-trailing-cr out_C.txt out_python.txt`
- Opción 2:
  * Ejecutar `diff --strip-trailing-cr out_C.txt solutions/test.txt`

- Si la ejecución de `diff --strip-trailing-cr` no imprime nada en consola, significa que **ambos archivos son iguales**.

Recuerda revisar la guía de instalación de C en tu computador [aquí](https://github.com/IIC2133-PUC/2020-2/tree/master/Gu%C3%ADas/Setup), y revisar ejemplos básicos del uso de C [aquí](https://github.com/IIC2133-PUC/2020-2/tree/master/Ayudant%C3%ADas/Ayudant%C3%ADa%200%20-%20Intro%20a%20C/Aprende%20C).
