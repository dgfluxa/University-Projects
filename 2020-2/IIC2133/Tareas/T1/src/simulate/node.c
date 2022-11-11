#include "node.h"
#include "../engine/math/geometry.h"
#include "../engine/math/vector.h"
#include "../engine/particle.h"
#include <stdbool.h> 
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include "../visualizer/visualizer.h"

// Definimos número máximo de segmentos que tendrá la caja de un nodo hoja
int k = 50;

int partition(Segment* segments, int inicio, int fin, int eje)
{
    int p = rand() % (fin - inicio + 1) + inicio;
    Segment men[fin - inicio + 1]; 
    int num_men = 0;
    Segment may[fin - inicio + 1]; 
    int num_may = 0;

    if (eje == 0)
    {
        for (int s = inicio; s <= fin; s++) 
        {
            if(segments[s].pi.x < segments[p].pi.x)
            {
                men[num_men] = segments[s];
                num_men += 1;
            }
            else 
            {
                may[num_may] = segments[s];
                num_may += 1;
            }
        }
    }
    else
    {
        for (int s = inicio; s <= fin; s++) 
        {
            if(segments[s].pi.y < segments[p].pi.y)
            {
                men[num_men] = segments[s];
                num_men += 1;
            }
            else 
            {
                may[num_may] = segments[s];
                num_may += 1;
            }
        }
    }

    // Concatenar m y M
    for (int i = 0; i < num_men; i++)
    {
        segments[i + inicio] = men[i];
        
    } 
    for (int i = 0; i < num_may; i++)
    {
        segments[i + inicio + num_men] = may[i];
    }
    return inicio + num_men;
}

int median(Segment* segmentos, int numero_segmentos, int eje)
{
    int i = 0;
    int f = numero_segmentos - 1;
    int x = partition(segmentos, i, f, eje);
    //printf("Median:\n  x= %i\n  numero_segmentos/2= %i\n", x, numero_segmentos/2);

    while (x != numero_segmentos/2)
    {
        if (x < numero_segmentos/2)
        {
            i = x + 1;
        }
        else
        {
            f = x - 1;
        }
        x = partition(segmentos, i, f, eje);
    }
    return x;

}

void quicksort(Segment* segments, int i, int f, int eje)
{
    if (i <= f)
    {
        int p = partition(segments, i, f, eje);
        quicksort(segments, i, p - 1, eje);
        quicksort(segments, p + 1, f, eje);
    }
}

/** Inicializa un Node vacío */
Node* node_init(Vector min, Vector max)
{
    Node* node = malloc(sizeof(Node));
    node -> num_seg = 0;
    node -> segments = calloc(k, sizeof(Segment*));
    node -> box.min_point = min;
    node -> box.max_point = max;
    node -> leaf = false;


    return node;
}

void node_delete(Node* node)
{
    if (node -> leaf)
    {
        free(node -> segments);
        free(node);
    }
    else
    {
        node_delete(node -> left);
        node_delete(node -> right);
        free(node -> segments);
        free(node);
    }
    
    
    /*if (node -> leaf == false)
    {
        node_delete(node -> left);
        node_delete(node -> right);
    }

    free(node -> segments);
    free(node -> left);
    free(node -> right);
    free(node);  */
}

Node* kdtree(Segment* segmentos, int depth, int inicio, int fin)
{
    double min_x = segmentos[inicio].pi.x;
    double max_x = segmentos[inicio].pf.x;
    double min_y = segmentos[inicio].pi.y;
    double max_y = segmentos[inicio].pf.y;

    // Declaramos variables que utilizaremos
    double min_x_now;
    double max_x_now;
    double min_y_now;
    double max_y_now;

    if (segmentos[inicio].pf.x < min_x)
    {
        min_x = segmentos[inicio].pf.x;
    }
    if (segmentos[inicio].pf.y < min_y)
    {
        min_y = segmentos[inicio].pf.y;
    }
    if (segmentos[inicio].pi.x > max_x)
    {
        max_x = segmentos[inicio].pi.x;
    }
    if (segmentos[inicio].pi.y < min_y)
    {
        max_y = segmentos[inicio].pi.y;
    }

    for (int s = inicio; s <= fin; s++) 
    {
        // Definimos el x mayor y menor del segmento
        if (segmentos[s].pi.x <= segmentos[s].pf.x)
        {
            min_x_now = segmentos[s].pi.x;
            max_x_now = segmentos[s].pf.x;
        }
        else
        {
            min_x_now = segmentos[s].pf.x;
            max_x_now = segmentos[s].pi.x;
        }
        // Definimos el y mayor y menor del segmento
        if (segmentos[s].pi.y <= segmentos[s].pf.y)
        {
            min_y_now = segmentos[s].pi.y;
            max_y_now = segmentos[s].pf.y;
        }
        else
        {
            min_y_now = segmentos[s].pf.y;
            max_y_now = segmentos[s].pi.y;
        }

        // Chequeamos si cambian los minimos
        if (min_x_now < min_x)
        {
            min_x = min_x_now;
        }
        if (min_y_now < min_y)
        {
            min_y = min_y_now;
        }
        // Chequeamos si cambian los maximos
        if (max_x_now > max_x)
        {
            max_x = max_x_now;
        }
        if (max_y_now > max_y)
        {
            max_y = max_y_now;
        }
    }

    Vector min_vector;
    min_vector.x = min_x;
    min_vector.y = min_y;
    Vector max_vector;
    max_vector.x = max_x;
    max_vector.y = max_y;

    Node* node = node_init(min_vector, max_vector);

    if ((fin - inicio) < k)
    {
        node -> leaf = true;
        //Descomentar para ver todas las cajas de los hijos
        //visualizer_set_color(51.0/255.0, 244.0/255.0, 255.0/255.0);
        //visualizer_draw_box(node -> box);
        node -> num_seg = fin - inicio + 1;
        for (int i = 0; i < node -> num_seg; i++)
        {
            node -> segments[i] = &segmentos[i + inicio];
        }
        
    }
    else
    {
        quicksort(segmentos, inicio, fin, depth%2);
        int mediana = (fin - inicio)/2;
        node -> left = kdtree(segmentos, depth + 1, inicio, mediana + inicio);
        node -> right = kdtree(segmentos, depth + 1, inicio + mediana + 1, fin);
    }
    return node;
}

Segment* check_collision_tree(Node* node, Particle particle)
{
    
    if (node -> leaf)
    {
        for (int s = 0; s < node -> num_seg; s++)
        {
            // Si la particula choca con el segmento
            if (particle_segment_collision(particle, *node->segments[s])) 
            {
                
                // Si es que no ha chocado con nada, o si no desempatamos por ID
                if(particle.intersected_segment == NULL || node->segments[s]->ID < particle.intersected_segment -> ID)
                {
                    particle.intersected_segment = node->segments[s];
                }
            } 
        } 
    }
    else
    {
        Segment* seg = NULL;
        if (particle_boundingbox_collision(particle, node -> left -> box))
        {
            seg = check_collision_tree(node -> left, particle);
            particle.intersected_segment = seg;
        }
        if (particle_boundingbox_collision(particle, node -> right -> box))
        {
            seg = check_collision_tree(node -> right, particle);
            particle.intersected_segment = seg;
        }
    }
    return particle.intersected_segment; 
}
