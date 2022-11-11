#pragma once
#include "../engine/math/geometry.h"
#include "../engine/math/vector.h"
#include "../engine/particle.h"
#include <stdbool.h> 

struct node;
typedef struct node Node;
struct node
{
    int num_seg;
    Segment** segments;
    BoundingBox box;
    bool leaf;
    Node* left;
    Node* right;

};

// Declaración de funciones

// Inicializa un Nodo vacío
Node* node_init(Vector min, Vector max);
// Función para eliminar un nodo
void node_delete(Node* node);
// Función para crear el arbol
Node* kdtree(Segment* segmentos, int depth, int inicio, int fin);

Segment* check_collision_tree(Node* node, Particle particle);