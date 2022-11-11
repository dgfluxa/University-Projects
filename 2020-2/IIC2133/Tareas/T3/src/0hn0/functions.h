#pragma once
#include "node.h"


// Se definirán múltiples funciones para el correcto funcionamiento del solver

// Función que cuenta el número de casillas que ve un nodo
int calcular_grado(int** matriz, int N, int row, int col);

// Función para calcular el grado máximo posible que podría llegar a tomar un nodo (numero de azules + grises que ve)
int calcular_posibles(int** matriz, int N, int row, int col);

//Función para pintar todos los vecinos de un nodo
void pintar_posibles(int** matriz, int N, int row, int col);

//Función para pintar todos los caminos de un nodo lleno de rojo
void pintar_llenos(int** matriz, int N, int row, int col);

// Función que verifica si un nodo se encuentra conectado a otro
int conexion(int** matriz, int N, int row, int col);

// Función que verifica sin podas si es válido colocar un color a una casilla
int valido1(int** matriz, int N);

// Función que verifica con podas si es válido colocar un color a una casilla
int valido2(int** matriz, int N, int row, int col);

// Función que verifica si una matriz terminada es válida
int matriz_valida(int** matriz, int N);

// Función que aplica la heuristica de comenzar por aquellos nodos en los que su posibilidad de grado es igual a su grado
int heuristica1(int** matriz, int N);

// Función que cierra todos los caminos de un nodo que ya llegó a su grado
int heuristica2(int** matriz, int N);

// Función que aplica la heuristica de comenzar por aquellos nodos en los que existe un único camino posible
int heuristica3(int** matriz, int N);

// Función que aplica las heurísticas al inicio del proceso
void aplicar_heuristicas(int** matriz, int N);

// Función que determina los grados de cada nodo azul y cambia azules de grado 0 a rojos asignado al finalizar
void finalizar_matriz(int** matriz, int N);

// Función que imprime la matriz
void print_matriz(int** matriz, int N);

// Función que elimina la matriz
void destroy_matriz(int** matriz, int N);

// Función que modifica las variables row y col para encontrar el proximo lugar sin asignar
int* find_coords(int** matriz, int N, int row, int col);

// Función para copiar una matriz a otra
void copiar_matriz(int** matriz1, int** matriz2, int N);

// Función de backtracking para resolver el puzzle
int oh_yes(int** matriz, int N, int* posibles, int row, int col);

// Funciones para resolver tests hard

// Función para crear lista ligada de nodos azules asignados
Node* crear_lista(int** matriz, int N);

// Función que encuentra las coordenadas del proximo nodo a asignar en nuevo modelamiento
int* find_better(int** matriz, int N, Node* node);

// Función que verifica si una matriz terminada es válida en nuevo modelamiento
int matriz_yeah(int** matriz, int N, Node* last);

// Función que determina los grador de los nodos azules determinados y le asigna color rojo al resto
void finalizar_yeah(int** matriz, int N);

// Función de backtracking con nueva modelación
int oh_yeah(int** matriz, int N, Node* node, int* posibles, Node* last);
