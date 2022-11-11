#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <cairo-pdf.h>
#include "drawing.h"

#define WINDOW_MAX_SIZE 640.0



/** Los colores para cada tipo de celda */
Color colors[4];
Color dark_colors[4];
Color light_colors[4];
Color unsat_colors[4];

Color background_color = (Color) 
{
  .R = 1,
  .G = 1,
  .B = 1
};

Color unassigned_color = 
{
  .R = 238.0 / 255.0,
  .G = 238.0 / 255.0,
  .B = 238.0 / 255.0
};

Color visible_color = (Color)
{
  .R = 28.0 / 255.0,
  .G = 192.0 / 255.0,
  .B = 224.0 / 255.0
};

Color obstacle_color = (Color)
{
  .R = 255.0 / 255.0,
  .G = 56.0 / 255.0,
  .B = 75.0 / 255.0
};

void cairo_dip(cairo_t* cr, Color color)
{
  cairo_set_source_rgb(cr, color.R, color.G, color.B);
}

/** Indica que tipo de votante tiene esta celda */
void drawing_cell_value(Content* cont, int row, int col, uint8_t value)
{
  cont -> value_matrix[row][col] = value;
}

/** Indica que número tiene esta celda */
void drawing_cell_number    (Content* cont, int row, int col, uint8_t number)
{
  cont -> number_matrix[row][col] = number;
}

/** Destaca o deja de destacar una celda */
void     drawing_cell_highlight (Content* cont, int row, int col, bool highlight)
{
  cont -> highlight_matrix[row][col] = highlight;
}

void cairo_circle(cairo_t* cr, int cx, int cy, double radius)
{
  cairo_arc (cr, cx, cy, radius, 0, 2*M_PI);
}

/** Dibuja el problema en la ventana */
bool drawing_draw(cairo_t* restrict cr, Content* restrict cont)
{
  /* Para prevenir cambios mientras dibujamos */
  pthread_mutex_lock(&drawing_mutex);

  cairo_dip(cr, background_color);

  cairo_paint(cr);

  /* Numbers */
  cairo_text_extents_t te;
  cairo_select_font_face (cr, "monospace",
      CAIRO_FONT_SLANT_NORMAL, CAIRO_FONT_WEIGHT_NORMAL);
  cairo_set_font_size (cr, cont -> cell_size / 2.5);
  char text[4];

  for(int row = 0; row < cont -> matrix_height; row++)
  {
    for(int col = 0; col < cont -> matrix_width; col++)
    {

      double cx = (col + 1) * cont -> cell_size;
      double cy = (row + 1) * cont -> cell_size;

      double radius = 0.45 * cont -> cell_size;

      switch(cont -> value_matrix[row][col])
      {
        case 1: cairo_dip(cr, visible_color); break;
        case 2: cairo_dip(cr, obstacle_color); break;
        default: cairo_dip(cr, unassigned_color); break;
      }
      cairo_circle(cr, cx, cy, radius);
      if(cont -> highlight_matrix[row][col])
      {
        cairo_fill_preserve(cr);
        cairo_set_source_rgb(cr, 0, 0, 0);
        cairo_set_line_width(cr, cont -> cell_size / 20);
        cairo_stroke(cr);
      }
      else
      {
        cairo_fill(cr);
      }
      


      if(cont -> number_matrix[row][col])
      {
        sprintf(text,"%u",cont -> number_matrix[row][col]);
        
        cairo_text_extents (cr, text, &te);
        
        double x = cont -> cell_size + cont -> cell_size * col - te.width / 2 - te.x_bearing;
        double y = cont -> cell_size + cont -> cell_size * row - te.height / 2 - te.y_bearing;
        cairo_move_to (cr, x, y);
        cairo_text_path(cr, text);
        cairo_set_source_rgb(cr, 1, 1 , 1);
        cairo_fill(cr);
      }
    }
  }

  pthread_mutex_unlock(&drawing_mutex);

	return true;
}

/** Genera los contenedores para las dos imagenes superpuestas */
Content* drawing_init(int height, int width)
{
  Content* cont = malloc(sizeof(Content));

  pthread_mutex_init(&drawing_mutex, NULL);

  /* Dimensiones de la matriz */
  cont -> matrix_height = height;
  cont -> matrix_width = width;

  /* Las dimensiones de la ventana deben ajustarse a la matriz */
	cont -> cell_size = WINDOW_MAX_SIZE / fmax(height + 1, width + 1);

  /* Dimensiones de la ventana */
	cont -> window_height = cont -> cell_size * (height + 1);
	cont -> window_width  = cont -> cell_size * (width + 1);

  /* Inicializamos las matrices */
  cont -> value_matrix = calloc(height, sizeof(uint8_t*));
  cont -> number_matrix = calloc(height, sizeof(uint8_t*));
  cont -> highlight_matrix = calloc(height, sizeof(bool*));
  for(int row = 0; row < height; row++)
  {
    cont -> value_matrix[row] = calloc(width, sizeof(uint8_t));
    cont -> number_matrix[row] = calloc(width, sizeof(uint8_t));
    cont -> highlight_matrix[row] = calloc(width, sizeof(bool));
  }

  return cont;
}

/** Geenera una imagen en pdf para un estado en particular */
void drawing_snapshot(Content* cont, char* filename)
{
	double width = cont -> matrix_width * 64;
	double height = cont -> matrix_height * 64;

	/* Imprimimos las imagenes del tablero */
	cairo_surface_t* surface;
	cairo_t *cr;

  surface = cairo_image_surface_create(CAIRO_FORMAT_RGB24, width, height);

	/* Reseteamos los parámetros para generar correctamente la imagen */
	Content aux = *cont;

  aux.cell_size = 64;
  aux.window_height = height;
  aux.window_width = width;

  cr = cairo_create(surface);

	/* Dibuja el estado actual */
	drawing_draw(cr, &aux);

  cairo_surface_write_to_png(surface, filename);

	cairo_surface_destroy(surface);
	cairo_destroy(cr);
}

/** Libera los recursos asociados a las herramientas de dibujo */
void drawing_free(Content* cont)
{
  for(int row = 0; row < cont -> matrix_height; row++)
  {
    free(cont -> value_matrix[row]);
    free(cont -> number_matrix[row]);
  }
  free(cont -> value_matrix);
  free(cont -> number_matrix);

  free(cont);
}
