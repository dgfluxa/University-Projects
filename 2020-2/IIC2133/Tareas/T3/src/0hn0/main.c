#include "../visualizer/visualizer.h"
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>
#include "functions.h"
#include "node.h"

bool check_arguments(int argc, char** argv)
{
  if(!(argc == 3 || argc == 4)) return false;
  if(argc == 4)
  {
    if(!strcmp(argv[3], "--novis"))
    {
      visualizer_disable();
    }
    else return false;
  }  
  return true;
}

int main(int argc, char** argv)
{
  if(!check_arguments(argc,argv))
  {
    printf("Modo de uso: %s input output [--novis]\nDonde:\n", argv[0]);
    printf("\t\"input\" es la ruta al archivo de input\n");
    printf("\t\"output\" es la ruta al archivo de output\n");
    printf("\t\"--novis\" es el flag opcional que desactiva el visualizador\n");
    return 1;
  }

  // Abrimos el archivo de input
  FILE* input_stream = fopen(argv[1], "r");

  // Abrimos el archivo de output
  FILE* output_stream = fopen(argv[2], "w");

  // Si alguno de los dos archivos no se pudo abrir
  if(!input_stream)
  {
    printf("El archivo %s no existe o no se puede leer\n", argv[1]);
    return 2;
  }
  if(!output_stream)
  {
    printf("El archivo %s no se pudo crear o no se puede escribir\n", argv[2]);
    printf("Recuerda que \"fopen\" no puede crear carpetas\n");
    fclose(input_stream);
    return 3;
  }


  // leemos el tamaño del tablero
  int N;
  fscanf(input_stream, "%d", &N);

  // TAREA: Creamos matriz que represente el tablero
  int** Tablero = calloc(N, sizeof(int*));

  // inicializamos la interfaz
  visualizer_open(N,N);

  // leemos el numero en cada celda del tablero
  int cell;
  // leemos cada valor del tablero: cada fila
  for (int row = 0; row < N; row++)
  {
    // TAREA: Creamos fila de la matriz
    Tablero[row] = calloc(N, sizeof(int*));

    // y cada columna dentro de esa fila
    for (int col = 0; col < N; col++)
    {
      fscanf(input_stream, "%d", &cell);

      // TAREA: Agregamos el nodo a la matriz
      Tablero[row][col] = cell;

      if (cell == -1)
      {
        // indicamos que la celda (row,col) tiene color rojo
        visualizer_set_cell_color(row, col, RED);
      }
      else if (cell > 0)
      {
        // indicamos que la celda (row,col) tiene color azul
        visualizer_set_cell_color(row, col, BLUE);
        // asignamos el grado a la celda (row,col)
        visualizer_set_cell_degree(row, col, cell);
      }
      else
      {
        // indicamos que la celda (row,col) no tiene color (aun)
        visualizer_set_cell_color(row, col, NONE);
      }
      
    }
  }
  // actualizamos el contenido de la ventana
  visualizer_redraw();

  // -------------------------- TAREA ----------------------------------

  // Imprimimos matriz para ver que se ha creado bien
  
  //printf("Inicial: \n");
  //print_matriz(Tablero, N);

  // Aplicamos heurísticas iniciales
  aplicar_heuristicas(Tablero, N);

  /*// Creamos matriz de respaldo
  int** respaldo = calloc(N, sizeof(int*));
  for (int row = 0; row < N; row++)
  {
    respaldo[row] = calloc(N, sizeof(int*));

    for (int col = 0; col < N; col++)
    {
      respaldo[row][col] = Tablero[row][col];
    }
  }*/

  // Imprimimos matriz para ver el efecto de las heurísticas
  //printf("\nHeurísticas: \n");
  //print_matriz(Tablero, N);

  // Creamos lista ligada
  //if (matriz_valida(Tablero, N) == 0){
    Node* root = crear_lista(Tablero, N);

    Node* last = root;
    while (last -> next){
      last = last -> next;
    }

    /*// Imprimimos lista
  printf("\nLista:\n");
  Node* actual = root;
  printf("%i, (%i, %i)\n", actual -> grado, actual -> row, actual -> col);
  while(actual -> next){
    actual = actual -> next;
    printf("%i, (%i, %i)\n", actual -> grado, actual -> row, actual -> col);
  }*/

  // Definimos array de posibles valores que puede tomar un nodo (-2: azul, -1: rojo)
  int* posibles = calloc(2, sizeof(int));
  posibles[0] = -2;
  posibles[1] = -1;

  // Resolvemos el problema utilizando backtracking
  //oh_yes(Tablero, N, posibles, 0, 0);
  oh_yeah(Tablero, N, root, posibles, last);

  // Agregamos grados y eliminamos puntos azules de grado 0
  //finalizar_matriz(Tablero, N);
  finalizar_yeah(Tablero, N);

  // Imprimimos matriz para ver que se ha resuelto bien


    // Liberamos array de posibles
  free(posibles);

  // Liberamos lista ligada
  node_delete(root);

  //}

  //printf("\nFinal: \n");
  //print_matriz(Tablero, N);

  

  // Escribimos en el output
  for (int i=0; i<N; i++){
    fprintf(output_stream, "%i", Tablero[i][0]);
    for (int j=1; j<N; j++){
      fprintf(output_stream, " %i", Tablero[i][j]);
    }
    fprintf(output_stream, "\n");
  }

  // Liberamos la matriz
  destroy_matriz(Tablero, N);
  //destroy_matriz(respaldo, N);

  // ------------------------ END TAREA --------------------------------

  // cerramos el archivo de input
  fclose(input_stream);

  //sleep(4);

  // cerramos la ventana
  visualizer_close();

  // acá escribes tu tarea en output
  // cerramos el archivo de output
  fclose(output_stream);

  return 0;
}