#include "node_ids.h"
#include <stdbool.h> 
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

/** Inicializa un Node vacío */
NodeId* node_id_init(int ID)
{
    NodeId* nodeid = malloc(sizeof(NodeId));
    nodeid -> id = ID;
    nodeid -> next = NULL;

    return nodeid;
}

void node_id_delete(NodeId* nodeid)
{
    if (nodeid -> next){
        node_id_delete(nodeid->next);
    }
    free(nodeid);
}