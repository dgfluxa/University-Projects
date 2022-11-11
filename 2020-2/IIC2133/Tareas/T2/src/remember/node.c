#include "node.h"
#include <stdbool.h> 
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <math.h>

/** Inicializa un Node vacío */
Node* node_init(u_int64_t hash, int alt, u_int64_t rep)
{
    Node* node = malloc(sizeof(Node));
    node -> hash = hash;
    node -> rep = rep;
    node -> alt = alt;
    node -> next = NULL;

    return node;
}

void node_delete(Node* node)
{
    if (node -> next){
        node_delete(node->next);
    }
    node_id_delete(node->ids);
    free(node);
}