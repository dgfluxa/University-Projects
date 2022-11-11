#pragma once
#include <stdio.h>
struct cell;
typedef struct cell Cell;
struct cell
{
    int id;
    Cell** children;
};

// Declaración de funciones

/** Inicializa un Cell vacío */
Cell* cell_init(int id);
/** Función para guardar en un archivo el estado de una célula y sus hijas, recursivamente. */
void cell_observe(Cell* cell, int spacing, int idx, FILE* file);
/** Función para eliminar una célula hija en índice 'idx'.*/
void cell_delete(Cell* cell, int idx);
