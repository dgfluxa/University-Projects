#include "mould.h"
#include "cell.h"
#include <stdlib.h>
#include <stdio.h>

/** Inicializa un Mould vacío */
Mould* mould_init()
{
    Mould* mould = malloc(sizeof(Mould));
    mould -> root = cell_init(0);
    mould -> id = 1;

    return mould;
}

/** Función para clonar una célula. */
Cell* mould_copy_cell(Mould* mould, Cell* cell)
{
    /** Si la célula existe */
    if (cell != NULL)
    {
        /** Creamos una nueva célula */
        Cell* new = cell_init(mould -> id);

        /** Aumentamos el identificador global */
        mould -> id += 1;

        /** Por cada una de las células */
        for (int i = 0; i < 10; i += 1)
        {
            /** Clonamos la hija */
            new -> children[i] = mould_copy_cell(mould, cell -> children[i]);
        }

        /** Retornamos el clon */
        return new;
    }
    else
    {
        return NULL;
    }
}

/** Función para agregar una célula en un determinado índice. */
void mould_add_cell(Mould* mould, Cell* cell, int idx)
{
    /** Agregamos la célula */
    cell -> children[idx] = cell_init(mould -> id);
    

    /** Aumentamos el identificador global */
    mould -> id += 1;
}

/** Función para eliminar mould */
void mould_destroy(Mould* mould)
{
    for (int i = 0; i < 10; i += 1)
    {
        if (mould -> root -> children[i] != NULL || mould -> root -> children[i] != 0)
        {
            cell_delete(mould -> root, i);
        }
    }
    free(mould -> root -> children);
    free(mould -> root);
    free(mould);
}