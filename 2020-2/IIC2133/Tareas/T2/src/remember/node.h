#pragma once
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h> 
#include "node_ids.h"
//Nodos de lista ligada para colisiones
struct node;
typedef struct node Node;
struct node
{
    u_int64_t hash;
    int alt;
    u_int64_t rep;
    NodeId* ids;
    Node* next;

};

// Declaración de funciones

// Inicializa un Nodo vacío
Node* node_init(u_int64_t hash, int alt, u_int64_t rep);
// Función para eliminar un nodo
void node_delete(Node* node);
// Función para crear el arbol