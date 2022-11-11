#pragma once
#include <stdbool.h> 
//Nodos de lista ligada para colisiones
struct node_id;
typedef struct node_id NodeId;
struct node_id
{
    int id;
    NodeId* next;

};

// Declaración de funciones

// Inicializa un Nodo vacío
NodeId* node_id_init(int ID);
// Función para eliminar un nodo
void node_id_delete(NodeId* node);
// Función para crear el arbol