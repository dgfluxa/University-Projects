#include "hash.h"
#include <stdbool.h> 
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include "node.h"
#include <math.h>

Node** crear_tabla(int altura) 
{
    Node** tabla = calloc(pow(2, altura) - 1 - altura, sizeof(Node*));
    return tabla;
}

int ajuste(int altura, u_int64_t hash){
    int m = pow(2, altura) - 1 - altura;
    return hash % m;
}

u_int64_t hash_consulta(int* arbol, int altura)
{
    u_int64_t indice = 0;
    u_int64_t valor = arbol[indice];
    indice += 1;

    for (u_int64_t i=2; i<=altura; i++){
        u_int64_t nivel = 0;
        for (u_int64_t j = 0; j < pow(2, i - 1); j++){
            nivel = nivel << 1;
            nivel = nivel ^ arbol[indice];
            indice += 1;
        }
        valor = valor ^ nivel;
    }
    return valor;
}

void agregar(int ajustado, u_int64_t hash, int id, int altura, Node** tabla, u_int64_t rep){
    if (tabla[ajustado]){
        int existe = 0;
        Node* node = tabla[ajustado];
        while (existe == 0){
            //Si coinciden las representaciones y alturas corresponderán al mismo arbol
            if (node -> rep == rep && node -> alt == altura){
                existe = 1;
                //Se agrega el nuevo id de coincidencia en posición ascendente en la lista ligada de ids
                NodeId* nodeid = node->ids;
                NodeId* new_nodeid = node_id_init(id);
                //Si es menor que el primer nodo se agrega al inicio
                if (nodeid -> id > new_nodeid -> id){
                    node->ids = new_nodeid;
                    new_nodeid -> next = nodeid;
                }
                //Si es mayor al primero se revisa en los siguientes
                else{
                    int added = 0;
                    while (added == 0){
                        //si hay nodo siguiente se revisa si es menor a ese
                        if (nodeid -> next){
                            NodeId* next_node = nodeid -> next;
                            //Si es menor se agrega entremedio
                            if (next_node -> id > new_nodeid -> id){
                                nodeid -> next = new_nodeid;
                                new_nodeid -> next = next_node;
                                added = 1;
                            }
                            //Si es mayor se avanza al siguiente
                            else{
                                nodeid = next_node;
                            }
                        }
                        //Si no existe nodo siguiente se agrega al final de la lista ligada
                        else{
                            nodeid -> next = new_nodeid;
                            added = 1;
                        }
                    }
                }
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
        //Si no se encontró coincidencia, se crea un nuevo nodo y se agrega al final de la lista ligada de las colisiones
        if (existe == -1){
            Node* new_node = node_init(hash, altura, rep);
            NodeId* new_nodeid = node_id_init(id);
            new_node -> ids = new_nodeid;
            node -> next = new_node;
        }
    }
    else{
        Node* node = node_init(hash, altura, rep);
        NodeId* new_nodeid = node_id_init(id);
        node -> ids = new_nodeid;
        tabla[ajustado] = node;
    }
}

void hash_poblar(int* arbol, int id, int altura, int altura_original, Node** tabla)
{
    u_int64_t indice = 0;
    u_int64_t rep = 0;
    u_int64_t valor = arbol[indice];
    rep = rep << 1;
    rep = rep ^ arbol[indice];
    indice += 1;

    for (u_int64_t i=2; i<=altura; i++){
        u_int64_t nivel = 0;
        for (u_int64_t j = 0; j < pow(2, i - 1); j++){
            nivel = nivel << 1;
            nivel = nivel ^ arbol[indice];
            rep = rep << 1;
            rep = rep ^ arbol[indice];
            indice += 1;
        }
        valor = valor ^ nivel;
        int ajustado = ajuste(altura_original, valor);
        agregar(ajustado, valor, id, i, tabla, rep);
    }

    if (altura > 2){
        altura -= 1;
        u_int64_t idx = 1;
        int* subarbol1 = calloc(pow(2, altura) - 1, sizeof(int));
        int* subarbol2 = calloc(pow(2, altura) - 1, sizeof(int));
        int id1 = id * 2;
        int id2 = id * 2 + 1;
        int idx1 = 0;
        int idx2 = 0;
        //Dividir arbol en 2 sub arreglos
        for (u_int64_t i=1; i<=altura; i++){
            for (u_int64_t j = 0; j < pow(2, i - 1); j++){
            subarbol1[idx1] = arbol[idx];
            idx += 1;
            idx1 += 1;
            }
            for (u_int64_t k = 0; k < pow(2, i - 1); k++){
            subarbol2[idx2] = arbol[idx];
            idx += 1;
            idx2 += 1;
            }
        }
        //Liberar arreglo original
        free(arbol);
        //Aplicar hash_poblar a subarreglo1
        //printf("Recursión ID: %d!!!\n", id);
        hash_poblar(subarbol1, id1, altura, altura_original, tabla);
        //Aplicar hash_poblar a subarreglo2
        hash_poblar(subarbol2, id2, altura, altura_original, tabla);
    }
    else{
        free(arbol);
    }
}

void destroy_table(Node** table, int altura){
    for (int i=0; i<pow(2, altura) - 1 - altura; i++){
        if(table[i]){
            node_delete(table[i]);
        }
    }
    free(table);
}