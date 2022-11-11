#pragma once

#include <cairo.h>
#include <stdbool.h>
#include "color.h"
#include <pthread.h>


pthread_mutex_t drawing_mutex;

/** Contiene la información de lo que ha de ser dibujado en el canvas */
struct content
{
	/** Ancho de la ventana */
	int window_width;
	/** Alto de la ventana */
	int window_height;
	/** Matriz con el valor de cada celda */
	uint8_t** value_matrix;
	/** Matriz con el número de cada celda */
	uint8_t** number_matrix;
	/** Matriz destacación */
	bool**    highlight_matrix;
	/** Ancho de la matriz */
	int matrix_width;
	/** Alto de la matriz */
	int matrix_height;
	/** Indica el tamaño de una celda */
	int cell_size;
};
/** Contiene la información de lo que ha de ser dibujado en el canvas */
typedef struct content Content;

/** Inicializa las herramientas de dibujo */
Content* drawing_init           (int height, int width);
/** Dibuja sobre el canvas dado */
bool     drawing_draw           (cairo_t* cr, Content* cont);
/** Indica que valor tiene esta celda */
void     drawing_cell_value     (Content* cont, int row, int col, uint8_t value);
/** Indica que número tiene esta celda */
void     drawing_cell_number    (Content* cont, int row, int col, uint8_t number);
/** Destaca o deja de destacar una celda */
void     drawing_cell_highlight (Content* cont, int row, int col, bool highlight);
/** Genera una imagen en PNG para un estado en particular */
void     drawing_snapshot       (Content* cont, char* filename);
/** Libera los recursos asociados a las herramientas de dibujo */
void     drawing_free           (Content* cont);
