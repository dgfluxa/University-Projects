#pragma once
#include <stdbool.h>
/****************************************************************************/
/*                              Visualizer                                  */
/*                                                                          */
/* Módulo a cargo de la visualización del problema.                         */
/****************************************************************************/

/** Representa el color de una celda */
typedef enum
{
  NONE,
  BLUE,
  RED
} Color;

/** Desactiva las siguientes llamadas al visualizador */
void visualizer_disable            ();
/** Abre una ventana para mostrar un tablero de las dimensiones dadas */
void visualizer_open               (int height, int width);
/** Indica el color de una celda en la matriz */
void visualizer_set_cell_color     (int row, int col, Color color);
/** Indica la cantidad de celdas azules que puede ver una celda */
void visualizer_set_cell_degree    (int row, int col, int number);
/** Destaca o deja de destacar una celda de la matriz. */
void visualizer_set_cell_highlight (int row, int col, bool highlight);
/** Redibuja el contenido de la ventana */
void visualizer_redraw             ();
/** Genera una imagen PNG con el contenido actual de la ventana */
void visualizer_snapshot           (char* filename);
/** Cierra y libera los recursos de la ventana */
void visualizer_close              ();
