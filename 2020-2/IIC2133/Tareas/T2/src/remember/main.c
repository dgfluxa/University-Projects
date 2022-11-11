#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "node.h"
#include <math.h>
#include "hash.h"
#include "node_ids.h"

int main(int argc, char** argv)
{
  if(argc != 3)
  {
    printf("Modo de uso: %s input output\nDonde:\n", argv[0]);
    printf("\t\"input\" es la ruta al archivo de input\n");
    printf("\t\"output\" es la ruta al archivo de output\n");
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


  // [Aqui va tu tarea]

  // Definimos variables para leer archivo de input
  int num_nodos;
  int num_consultas;

  //Obtenemos número de nodos del árbol principal
  fscanf(input_stream, "%d", &num_nodos);

  //printf("Num nodos: %d\n", num_nodos);

  //Definimos altura del árbol
  int altura = log(num_nodos + 1)/log(2);

  //printf("Altura: %d\n", altura);

  //Creamos arreglo para todos los nodos del arbol que contenga su color
  int* Arbol = calloc(num_nodos, sizeof(int)); 

  int  color;

  //Agregamos colores de nodos al arreglo
  for (int i=0; i<num_nodos; i++){
    fscanf(input_stream, "%d", &color);
    Arbol[i] = color;
  };

  // Crear Hash table
  Node** table = crear_tabla(altura);

  // Poblar Hash table
  hash_poblar(Arbol, 1, altura, altura, table);

  //Para imprimir número de arboles y/o una representación de la tabla
  /*int num_arboles = 0;
  for (int i=0; i<pow(2, altura) - 1 - altura; i++){
    if(table[i]){
      Node* nodo = table[i];
      //printf("Arbol altura %d, Hash = %lu, Ajustado = %d, IDs =", nodo -> alt, nodo -> hash, i);
      NodeId* nodoid = nodo -> ids;
      int existe_id = 1;
      while (existe_id == 1){
        //printf(" %d", nodoid -> id);
        num_arboles += 1;
        if (nodoid -> next){
          nodoid = nodoid -> next;
        }
        else{
          existe_id = 0;
          //printf("\n");
        }
      }
      if(nodo -> next){
        while (nodo -> next){
          nodo = nodo -> next;
          //printf("   Arbol altura %d, Hash = %lu, Ajustado = %d, IDs =", nodo -> alt, nodo -> hash, i);
          nodoid = nodo -> ids;
          existe_id = 1;
          while (existe_id == 1){
            //printf(" %d", nodoid -> id);
            num_arboles += 1;
            if (nodoid -> next){
              nodoid = nodoid -> next;
            }
            else{
              existe_id = 0;
              //printf("\n");
            }
          }
        }
      }
    }
  }*/
  //printf("Número de árboles: %d\n", num_arboles);
  

  /* Descomentar para ver valor del hash del arbol original
  u_int64_t valor = hash_consulta(Arbol, altura);
  printf("Hash del arbol: %lu\n", valor);*/
  
  //Obtenemos el número de consultas
  fscanf(input_stream, "%d", &num_consultas);

  //printf("Num consultas: %d\n", num_consultas);

  //Procesamos cada consulta
  for (int i = 0; i<num_consultas; i++){
    int num_nodos_c;
    int* ArbolConsulta = calloc(num_nodos, sizeof(int));
    int color_c;

    //Obtenemos número de nodos del árbol de la consulta
    fscanf(input_stream, "%d", &num_nodos_c);

    //Definimos altura del árbol de la consulta
    int altura_c = log(num_nodos_c + 1)/log(2);

    //Agregamos colores de nodos al arreglo del árbol consultado
    for (int i=0; i<num_nodos_c; i++){
      fscanf(input_stream, "%d", &color_c);
      ArbolConsulta[i] = color_c;
    }

    //Obtener hash y hash ajustado del arbol de la consulta
    u_int64_t hash_c = hash_consulta(ArbolConsulta, altura_c);
    int ajustado_c = ajuste(altura, hash_c);

    //Obtener la representacion del arbol
    u_int64_t rep_c = 0;

    for (u_int64_t i=0; i<num_nodos_c; i++){
      rep_c = rep_c << 1;
      rep_c = rep_c ^ ArbolConsulta[i];
    }

    //Buscar si existe el árbol consultado en la tabla y registrar en el output
    if (table[ajustado_c]){
        int existe = 0;
        Node* node = table[ajustado_c];
        while (existe == 0){
            //Si coinciden las representaciones y alturas corresponderán al mismo arbol
            if (node -> rep == rep_c && node -> alt == altura_c){
                existe = 1;
                //Se agrega el nuevo id de coincidencia al final de la lista ligada de ids
                NodeId* nodeid = node->ids;
                fprintf(output_stream, "%d", nodeid -> id);
                while (nodeid->next){
                  nodeid = nodeid->next;
                  fprintf(output_stream, " %d", nodeid -> id);
                }
                fprintf(output_stream, "\n");
            }
            // Si no coinciden, se revisa si exite un nodo siguiente
            else{
                //Si existe nodo siguiente se repite el proceso con este
                if (node -> next){
                    node = node->next;
                }
                //Si no existe el siguiente nodo se sale del while con existe = -1
                else{
                    existe = -1;
                }
            }
        }
        //Si no se encontró coincidencia, se aregistra un -1 en el archivo de output
        if (existe == -1){
            fprintf(output_stream, "-1\n");
        }
    }
    else{
        fprintf(output_stream, "-1\n");
    }

    //Liberamos arreglo del arbol consultado
    free(ArbolConsulta);
  }


  // Cerrar archivo de input
  fclose(input_stream);

  // Cerrar archivo de output
  fclose(output_stream);

  // Destruimos la tabla
  destroy_table(table, altura);

  return 0;
}
