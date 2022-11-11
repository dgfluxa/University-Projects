#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h> 
#include "simulation.h"
#include "node.h"
#include "../visualizer/visualizer.h"


int main(int argc, char** argv) 
{
  // Por defecto se abre la ventana
  bool visualize = true;
  if (argc == 4 && !strcmp(argv[3], "--novis"))
  {
    visualize = false;  
  }
  else if(argc < 3|| argc >= 4)
  {
    printf("Modo de uso: %s INPUT OUTPUT [--novis]\n", argv[0]);
    printf("Donde:\n");
    printf("\tINPUT es la ruta al archivo de input que describe la escena\n");
    printf("\tOUTPUT es la ruta al archivo en donde se reportarán las colisiones\n");
    printf("\tEl flag opcional --novis indica que no se debe abrir la visualización del programa\n");
    // Exit code 1: Programa llamado sin todos los argumentos
    return 1;
  }
  
  // Inicializa los elementos de la simulación, y abre la ventana si visualize es true
  Simulation* sim = simulation_init_from_file(argv[1], visualize);

  // El archivo donde iremos reportando las colisiones
  FILE* output_file = fopen(argv[2], "w");


  // Crear nodo raiz [Descomentar]
  Node* root = kdtree(sim -> segments, 0, 0, sim -> segment_count - 1);

  /*for (int i = 0; i < root-> left -> num_seg; i++)
  {
      visualizer_set_color(1, 0, 0);
      visualizer_draw_segment(*root -> left -> segments[i]);
  }
    for (int i = 0; i < root -> right -> num_seg; i++)
  {
      visualizer_set_color(0, 1, 0);
      visualizer_draw_segment(*root -> right -> segments[i]);
  }*/


  // Para cada frame
  for (int f = 0; f < sim->frames; f++) 
  {
    // Para cada particula
    for (int p = 0; p < sim->particle_count; p++) 
    {
      // Inicialmente, esta particula no ha chocado con ningun segmento
      sim->particles[p].intersected_segment = NULL;
      // Por cada segmento
      // TODO: No revisar todos los segmentos, usar BVH para descartar los que estén muy lejos
      /*for (int s = 0; s < sim->segment_count; s++) 
      {
         Si la particula choca con el segmento
        if (particle_segment_collision(sim->particles[p], sim->segments[s])) {
          // Si es que no ha chocado con nada, o si no desempatamos por ID
          if(!sim->particles[p].intersected_segment || sim->segments[s].ID < sim->particles[p].intersected_segment->ID)
          {
            sim->particles[p].intersected_segment = &sim->segments[s];
          }
        }
      } */
      //printf("Leaf: %i \n", root -> leaf);
      sim->particles[p].intersected_segment = check_collision_tree(root, sim->particles[p]);
      //if (sim->particles[p].intersected_segment == NULL){printf("Hola\n");}
      // Si hubo intersección
      if(sim->particles[p].intersected_segment)
      {
        // Desviamos la partícula según el segmento con el que chocó
        particle_bounce_against_segment(&sim->particles[p], *sim->particles[p].intersected_segment);
        // Reportamos la colisión en el archivo de output
        fprintf(output_file, "%d %d %d\n", f, sim->particles[p].ID, sim->particles[p].intersected_segment->ID);
      }
      // Finalmente, la particula avanza 
      particle_move(&sim->particles[p]);
    }
    // Si la ventana está abierta, dibujar las particulas en sus nuevas posiciones
    visualizer_draw_particles(sim->particles, sim->particle_count);

    // Visualizar caja inicial
    //visualizer_set_color(51.0/255.0, 244.0/255.0, 255.0/255.0);
    //visualizer_draw_box(root -> box);

  }
  // Hace free de todo lo que se creo en simulation_init. Cierra la ventana.
  simulation_destroy(sim);

  // Borrar arbol
  node_delete(root);

  fclose(output_file);

  return 0;
}
