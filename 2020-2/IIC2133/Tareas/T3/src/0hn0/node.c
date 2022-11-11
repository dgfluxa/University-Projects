#include "node.h"
#include <stdbool.h> 
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <math.h>

/** Inicializa un Node vacío */
Node* node_init(int grado, int row, int col)
{
    Node* node = malloc(sizeof(Node));
    node -> grado = grado;
    node -> row = row;
    node -> col = col;
    node -> next = NULL;
    node -> prev = NULL;

    return node;
}

void node_delete(Node* node)
{
    if (node -> next){
        node_delete(node->next);
    }
    free(node);
}