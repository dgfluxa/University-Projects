#include "cell.h"
#include <stdlib.h>
#include <stdio.h>

/** Inicializa un Cell vacío */
Cell* cell_init(int cell_id)
{
    Cell* cell = malloc(sizeof(Cell));
    cell -> id = cell_id;
    cell -> children = calloc(10, sizeof(Cell*));

    return cell;
}
/** Función para guardar en un archivo el estado de una célula y sus hijas, recursivamente. */
void cell_observe(Cell* cell, int spacing, int idx, FILE* file)
{
    /** Escribimos el espaciado */
    for (int i = 0; i < spacing; i += 1)
    {
        fprintf(file, "   ");
    }

    /** Escribimos el índice de la célula y su identificador */
    if (idx == -1)
    {
        fprintf(file, "r:0\n");
    }
    else
    {
        fprintf(file, "%i:%i\n", idx, cell -> id);
    }

    /** Por cada hija */
    for (int i = 0; i < 10; i += 1)
    {
        /** Obtenemos a la hija */
        Cell* child = cell -> children[i];

        /** Si existe*/
        if (child != NULL)
        {
            /** La observamos */
            cell_observe(child, spacing + 1, i, file);
        }
    }
}
/** Función para eliminar una célula hija en índice 'idx'.*/
void cell_delete(Cell* cell, int idx)
{
    Cell* cell2 = cell -> children[idx];
    for (int i = 0; i < 10; i += 1)
    {
        if (cell2 -> children[i] != NULL || cell2 -> children[i] != 0)
        {
            cell_delete(cell2, i);
            free(cell2 -> children[i]);
        }
    }

    cell -> children[idx] = NULL;
    free(cell2 -> children);
    free(cell2);  
}