#pragma once
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "node.h"

//Declaración de funciones

//Crear tabla de hash
Node** crear_tabla(int altura);

//Función de ajuste
int ajuste(int altura, u_int64_t hash);

//Calcular el hash para consultas (No agrega cada subarbol)
u_int64_t hash_consulta(int* arbol, int altura);

//Hashear arbol de manera incremental agregando cada subarbol a la tabla
void hash_poblar(int* arbol, int id, int altura, int altura_original, Node** tabla);

//Función donde se verifica si se
void agregar(int ajustado, u_int64_t hash, int id, int altura, Node** tabla, u_int64_t rep);

//Eliminar tabla
void destroy_table(Node** table, int altura);
