#pragma once
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h> 
//Nodos de lista ligada para colisiones
struct node;
typedef struct node Node;
struct node
{
    int grado;
    int row;
    int col;
    Node* next;
    Node* prev;

};

// Declaración de funciones

// Inicializa un Nodo vacío
Node* node_init(int grado, int row, int col);
// Función para eliminar un nodo
void node_delete(Node* node);
// Función para crear el arbol