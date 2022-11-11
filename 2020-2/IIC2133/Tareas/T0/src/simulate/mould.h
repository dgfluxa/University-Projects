#pragma once
#include "cell.h"
struct mould;
typedef struct mould Mould;
struct mould
{
    Cell* root;
    int id;
};


// Declaración de funciones

/** Inicializa un Mould vacío */
Mould* mould_init();
/** Función para clonar una célula. */
Cell* mould_copy_cell(Mould* mould, Cell* cell);
/** Función para agregar una célula en un determinado índice. */
void mould_add_cell(Mould* mould, Cell* cell, int idx);
/* Función para eliminar mould */
void mould_destroy(Mould* mould);
