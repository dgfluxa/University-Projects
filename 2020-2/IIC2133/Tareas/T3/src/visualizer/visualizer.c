#include "visualizer.h"

#include <locale.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>

#define VISUALIZER "./visualizer_core"

#define USECS_PER_FRAME 16667

static FILE* visualizer = NULL;

static clock_t previous_frame;

static bool disabled = false;

/** Desactiva las siguientes llamadas al visualizador */
void visualizer_disable()
{
  disabled = true;

  if(visualizer)
  {
    fprintf(stderr, "No puedes desactivar el visualizador si ya lo abriste!\n");
  }
}

/** Abre una ventana para mostrar un tablero de las dimensiones dadas */
void visualizer_open(int height, int width)
{
  if(disabled) return;

  setlocale(LC_ALL, "C");

  char command[256];

  sprintf(command, "%s %d %d", VISUALIZER, height, width);

  if (visualizer) visualizer_close();

  visualizer = popen(command, "w");

  previous_frame = clock();
}

/** Indica el color de una celda en la matriz */
void visualizer_set_cell_color   (int row, int col, Color color)
{
  if (visualizer) {
    if (fprintf(visualizer, "C %d %d %u\n", row, col, color) < 0) {
      visualizer_close();
    } else {
      fflush(visualizer);
    }
  }
}

/** Resetea el color asignado a una celda */
void visualizer_clear_cell_value (int row, int col)
{
  if (visualizer) {
    if (fprintf(visualizer, "C %d %d\n", row, col) < 0) {
      visualizer_close();
    } else {
      fflush(visualizer);
    }
  }
}

/** Indica la cantidad de celdas azules que puede ver una celda */
void visualizer_set_cell_degree  (int row, int col, int number)
{
  if (visualizer) {
    if (fprintf(visualizer, "N %d %d %d\n", row, col, number) < 0) {
      visualizer_close();
    } else {
      fflush(visualizer);
    }
  }
}


/** Destaca o deja de destacar una celda de la matriz. */
void visualizer_set_cell_highlight (int row, int col, bool highlight)
{
  if (visualizer) {
    if (fprintf(visualizer, "H %d %d %u\n", row, col, highlight ? 1 : 0) < 0) {
      visualizer_close();
    } else {
      fflush(visualizer);
    }
  }
}


/** Redibuja el contenido de la ventana */
void visualizer_redraw()
{
  if (visualizer) {
    if (fprintf(visualizer, "D\n") < 0) {
      visualizer_close();
    } else {
      fflush(visualizer);
    }
  }
}

/** Genera una imagen PNG con el contenido actual de la ventana */
void visualizer_snapshot(char* filename) {
  if (visualizer) {
    if (fprintf(visualizer, "S %s\n", filename) < 0) {
      visualizer_close();
    } else {
      fflush(visualizer);
    }
  }
}

/** Cierra y libera los recursos de la ventana */
void visualizer_close() {
  if (visualizer) {
    if (fprintf(visualizer, "%s\n", "X") >= 0) {
      fflush(visualizer);
      pclose(visualizer);
    }
    visualizer = NULL;
  }
}
