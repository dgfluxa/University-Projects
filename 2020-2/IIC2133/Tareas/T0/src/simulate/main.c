#include "mould.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>


/* Retorna true si ambos strings son iguales */
bool string_equals(char *string1, char *string2)
{
  return !strcmp(string1, string2);
}

/* Revisa que los parámetros del programa sean válidos */
bool check_arguments(int argc, char **argv)
{
  if (argc != 3)
  {
    printf("Modo de uso: %s INPUT OUTPUT\n", argv[0]);
    printf("Donde:\n");
    printf("\tINPUT es la ruta del archivo de input\n");
    printf("\tOUTPUT es la ruta del archivo de output\n");
    return false;
  }

  return true;
}

/* Programa principal */
int main(int argc, char **argv)
{
  /* Si los parámetros del programa son inválidos */
  if (!check_arguments(argc, argv))
  {
    /* Salimos del programa indicando que no terminó correctamente */
    return 1;
  }

  /* Para leer las instrucciones */
  char command[32];
 
  /* Para obtener la profundidad e índice de los comandos */
  int depth;
  int idx;

  /* [IMPLEMENTADO] Inicalizamos el MOULD */
  Mould* mould = mould_init();

  /* Abrimos el archivo de input */
  FILE *input_file = fopen(argv[1], "r");

  /* Abrimos el archivo de output */
  FILE *output_file = fopen(argv[2], "w");

  /* Número de líneas a leer */
  int n_lines;
  fscanf(input_file, "%d", &n_lines);

  /* Mientras existan líneas */
  while (n_lines > 0)
  {

    /* Disminuímos el número de líneas por leer en 1 */
    n_lines -= 1;

    /* Leemos la línea y lo guardamos en comando */
    fscanf(input_file, "%s", command);

    /* Caso 1: Comando GROW */
    if (string_equals(command, "GROW"))
    {
      /* [IMPLEMENTADO] Partimos desde la raíz */
      Cell* cur = mould -> root;

      /* Obtenemos la profundidad de la célula que crecerá */
      fscanf(input_file, "%d", &depth);

      /* Iteramos hasta encontrar dicho nodo */
      for (int level = 0; level < depth; level++)
      {
        /* Obtenemos el índice */
        fscanf(input_file, "%d", &idx);

        /* [IMPLEMENTADO] Cambiamos la célula actual */
        cur = cur -> children[idx];
      }

      /* Obtenemos en qué posición crear un nueva célula */
      fscanf(input_file, "%i", &idx);

      /* [IMPLEMENTADO] La creamos */
      mould_add_cell(mould, cur, idx);
    }

    /* Caso 2: Comando CLONE */
    else if (string_equals(command, "CLONE"))
    {
      /* [IMPLEMENTADO] Partimos desde la raíz */
      Cell* cell_to_clone = mould -> root;
      
      /* Obtenemos la profundidad de la célula a clonar */
      fscanf(input_file, "%d", &depth);

      /* Iteramos hasta encontrar la célula */
      for (int level = 0; level < depth; level++)
      {

        /* Obtenemos el índice */
        fscanf(input_file, "%d", &idx);

        /* [IMPLEMENTADO] Cambiamos la célula actual */
        cell_to_clone = cell_to_clone -> children[idx];
      }

      /* [IMPLEMENTADO] Partimos desde la raíz */
      Cell* parent = mould -> root;

      /* Obtenemos la profundidad de la célula donde será clonada */
      fscanf(input_file, "%d", &depth);

      /* Iteramos hasta dicha profundidad */ 
      for (int level = 0; level < depth; level++)
      {

        /* Obtenemos el índice */
        fscanf(input_file, "%d", &idx);

        /* [IMPLEMENTADO] Cambiamos la célula actual */
        parent = parent -> children[idx];
      }

      /* Obtenemos la posición donde será clonado */
      fscanf(input_file, "%d", &idx);

      /* [IMPLEMENTADO] La clonamos (liberamos antes)*/
      parent -> children[idx] = mould_copy_cell(mould, cell_to_clone);
    }

    /* Caso 3: Comando CROSSOVER */
    else if (string_equals(command, "CROSSOVER"))
    {
      int child_1_idx;
      int child_2_idx;

      /* [IMPLEMENTADO] Partimos desde la raíz */
      Cell* parent_1 = mould -> root;

      /* Obtenemos la profundidad de la célula madre 1 */
      fscanf(input_file, "%d", &depth);

      /* Iteramos hasta dicha profundidad */
      for (int level = 0; level < depth; level++)
      {

        /* Obtenemos el índice */
        fscanf(input_file, "%d", &idx);

        /* [IMPLEMENTADO] cambiamos la célula actual */
        parent_1 = parent_1 -> children[idx];
      }

      /* Obtenemos el índice de la primera hija */
      fscanf(input_file, "%d", &child_1_idx);

      /* [IMPLEMENTADO] Obtenemos dicha hija */
      Cell* child_1 = parent_1 -> children[child_1_idx];

      /* [IMPLEMENTADO] Partimos desde la raíz */
      Cell* parent_2 = mould -> root;

      /* Obtenemos la profundidad de la célula madre 2 */
      fscanf(input_file, "%d", &depth);

      /* Iteramos hasta dicha profundidad */
      for (int level = 0; level < depth; level++)
      {
        /* Obtenemos el índice */
        fscanf(input_file, "%d", &idx);

        /* [IMPLEMENTADO] Cambiamos la célula actual */
        parent_2 = parent_2 -> children[idx];
      }

      /* Obtenemos el índice de la segunda hija */
      fscanf(input_file, "%d", &child_2_idx);
      
      /* [IMPLEMENTADO] Obtenemos dicha hija */
      Cell* child_2 = parent_2 -> children[child_2_idx];

      /* [IMPLEMENTADO] hacemos el intercambio */
      parent_1 -> children[child_1_idx] = child_2;
      parent_2 -> children[child_2_idx] = child_1;
    }

    /* Caso 4: Comando BUD */
    else if (string_equals(command, "BUD"))
    {
      /* [IMPLEMENTADO] Partimos desde la raíz */
      Cell* cur = mould -> root;

      /* Obtenemos la profundidad de la célula */
      fscanf(input_file, "%d", &depth);

      /* Iteramos hasta dicha célula */
      for (int level = 0; level < depth; level++)
      {

        /* Obtenemos el índice */
        fscanf(input_file, "%d", &idx);

        /* [IMPLEMENTADO] Cambiamos la célula actual */
        cur = cur -> children[idx];
      }

      /* Obtenemos el índice de la hija eliminar */
      fscanf(input_file, "%d", &idx);

      /* [IMPLEMENTADO] La eliminamos */
      cell_delete(cur, idx);
    }

    /* Caso 5: Comando ABSORB*/
    else if (string_equals(command, "ABSORB"))
    {

      /* [IMPLEMENTADO] Partimos desde la raíz */
      Cell* parent_1 = mould -> root;

      /* Obtenemos la profundidad */
      fscanf(input_file, "%d", &depth);

      /* Iteramos hasta dicha profundidad */
      for (int level = 0; level < depth; level++)
      {
        /* Obtenemos el índice */
        fscanf(input_file, "%d", &idx);

        /* [IMPLEMENTADO] Cambiamos la célula actual */
        parent_1 = parent_1 -> children[idx];
      }
      
      /* Obtenemos el índice de la hija que reemplazaremos */
      int new_idx;
      fscanf(input_file, "%d", &new_idx);
      
      /* [IMPLEMENTADO] Obtenemos dicha hija */
      Cell* parent_2 = parent_1 -> children[new_idx];

      /* Obtenemos la profundidad del camino a continuar */
      fscanf(input_file, "%d", &depth);

      /* Iteramos por ese camino hasta la penúltima célula */
      for (int level = 0; level < depth - 1; level++)
      {

        /* Obtenemos el índice */
        fscanf(input_file, "%d", &idx);

        /* [IMPLEMENTADO] Cambiamos la célula actual */
        parent_2 = parent_2 -> children[idx];
      }

      /* Obtenemos el índice de la célula que quedará */
      fscanf(input_file, "%d", &idx);

      /* [IMPLEMENTADO] Obtenemos dicha célula */
      Cell* child = parent_2 -> children[idx];

      /* [IMPLEMENTADO] Desvinculamos a la madre */
      parent_2 -> children[idx] = NULL;
      cell_delete(parent_1, new_idx);

      /* [IMPLEMENTADO] Reemplazamos */
      parent_1 -> children[new_idx] = child;

      /*Liberamos memoria */
    }

    /* Caso 6: Comando OBSERVE */
    else if (string_equals(command, "OBSERVE"))
    {

      /* Definimos el índice inicial */
      idx = -1;

      /* [IMPLEMENTADO] Partimos desde la raíz */
      Cell* current = mould -> root;

      /* Obtenemos la profundidad de la célula a observar */
      fscanf(input_file, "%d", &depth);
      
      /* Iteramos hasta dicha profundidad */
      for (int level = 0; level < depth; level++)
      {

        /* Obtenemos el índice */
        fscanf(input_file, "%d", &idx);

        /* [IMPLEMENTADO] Cambiamos la célula actual */
        current = current -> children[idx];
      }

      /* Distinguimos el estado */
      fprintf(output_file, "STATE\n");

      /* [IMPLEMENTADO] Obtenemos los datos de nuestra célula */
      cell_observe(current, 0, idx, output_file);
    }
  }
  
  /* Cerramos archivo de lectura */
  fclose(input_file);

  /* Cerramos archivo de escritura */
  fclose(output_file);

  /* Eliminamos el mould y liberamos memoria */
  mould_destroy(mould);
  
  return 0;
}
