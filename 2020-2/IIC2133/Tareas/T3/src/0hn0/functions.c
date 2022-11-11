#include "functions.h"
#include "node.h"
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include "../visualizer/visualizer.h"

// Función que cuenta el número de casillas que ve un nodo
int calcular_grado(int** matriz, int N, int row, int col){
    int contador = 0;
    for (int i=col-1; i >= 0; i--){
        if (matriz[row][i] != 0 && matriz[row][i] != -1){
            contador += 1;
        }
        else{
            break;
        }
    }
    for (int i=col+1; i < N; i++){
        if (matriz[row][i] != 0 && matriz[row][i] != -1){
            contador += 1;
        }
        else{
            break;
        }
    }
    for (int i=row-1; i >= 0; i--){
        if (matriz[i][col] != 0 && matriz[i][col] != -1){
            contador += 1;
        }
        else{
            break;
        }
    }
    for (int i=row+1; i < N; i++){
        if (matriz[i][col] != 0 && matriz[i][col] != -1){
            contador += 1;
        }
        else{
            break;
        }
    }
    return contador;
}

// Función para calcular el grado máximo posible que podría llegar a tomar un nodo (numero de azules + grises que ve)
int calcular_posibles(int** matriz, int N, int row, int col){
    int contador = 0;
    for (int i=col-1; i >= 0; i--){
        if (matriz[row][i] != -1){
            contador += 1;
        }
        else{
            break;
        }
    }
    for (int i=col+1; i < N; i++){
        if (matriz[row][i] != -1){
            contador += 1;
        }
        else{
            break;
        }
    }
    for (int i=row-1; i >= 0; i--){
        if (matriz[i][col] != -1){
            contador += 1;
        }
        else{
            break;
        }
    }
    for (int i=row+1; i < N; i++){
        if (matriz[i][col] != -1){
            contador += 1;
        }
        else{
            break;
        }
    }
    return contador;
}

// Función que verifica si un nodo se encuentra conectado a otro
int conexion(int** matriz, int N, int row, int col){
    if (row + 1 < N && matriz[row+1][col] != 0){
        return 1;
    }
    else if (row - 1 >= 0 && matriz[row-1][col] != 0){
        return 1;
    }
    else if (col + 1 < N && matriz[row][col + 1] != 0){
        return 1;
    }
    else if (col - 1 >= 0 && matriz[row][col-1] != 0){
        return 1;
    }
    return 0;
}

//Función para pintar todos los vecinos de un nodo
void pintar_posibles(int** matriz, int N, int row, int col){
    for (int i=col-1; i >= 0; i--){
        if (matriz[row][i] != -1){
            if (matriz[row][i] == 0){
                matriz[row][i] = -2;
                visualizer_set_cell_color(row, i, BLUE);
                visualizer_redraw();
                //usleep(100000);
            }
        }
        else{
            break;
        }
    }
    for (int i=col+1; i < N; i++){
        if (matriz[row][i] != -1){
            if (matriz[row][i] == 0){
                matriz[row][i] = -2;
                visualizer_set_cell_color(row, i, BLUE);
                visualizer_redraw();
                //usleep(100000);
            }
        }
        else{
            break;
        }
    }
    for (int i=row-1; i >= 0; i--){
        if (matriz[i][col] != -1){
            if (matriz[i][col] == 0){
                matriz[i][col] = -2;
                visualizer_set_cell_color(i, col, BLUE);
                visualizer_redraw();
                //usleep(100000);
            }
        }
        else{
            break;
        }
    }
    for (int i=row+1; i < N; i++){
        if (matriz[i][col] != -1){
            if (matriz[i][col] == 0){
                matriz[i][col] = -2;
                visualizer_set_cell_color(i, col, BLUE);
                visualizer_redraw();
                //usleep(100000);
            }
        }
        else{
            break;
        }
    }
}

//Función para pintar todos los caminos de un nodo lleno de rojo
void pintar_llenos(int** matriz, int N, int row, int col){
    for (int i=col-1; i >= 0; i--){
        if (matriz[row][i] != -1){
            if (matriz[row][i] == 0){
                matriz[row][i] = -1;
                visualizer_set_cell_color(row, i, RED);
                visualizer_redraw();
                //usleep(100000);
                break;
            }
        }
        else{
            break;
        }
    }
    for (int i=col+1; i < N; i++){
        if (matriz[row][i] != -1){
            if (matriz[row][i] == 0){
                matriz[row][i] = -1;
                visualizer_set_cell_color(row, i, RED);
                visualizer_redraw();
                //usleep(100000);
                break;
            }
        }
        else{
            break;
        }
    }
    for (int i=row-1; i >= 0; i--){
        if (matriz[i][col] != -1){
            if (matriz[i][col] == 0){
                matriz[i][col] = -1;
                visualizer_set_cell_color(i, col, RED);
                visualizer_redraw();
                //usleep(100000);
                break;
            }
        }
        else{
            break;
        }
    }
    for (int i=row+1; i < N; i++){
        if (matriz[i][col] != -1){
            if (matriz[i][col] == 0){
                matriz[i][col] = -1;
                visualizer_set_cell_color(i, col, RED);
                visualizer_redraw();
                //usleep(100000);
                break;
            }
        }
        else{
            break;
        }
    }
}

// Función que verifica sin podas si es válido colocar un color a una casilla
int valido1(int** matriz, int N){
    for(int i = 0; i < N; i++)
    {
        for(int j = 0; j < N; j++)
        {
            if (matriz[i][j] != 0 && matriz[i][j] != -1 && matriz[i][j] != -2){
                if (matriz[i][j] < calcular_grado(matriz, N, i, j)){
                    return 0;
                }
            }
        }
    }
    return 1;
}

// Función que verifica con podas si es válido colocar un color a una casilla
int valido2(int** matriz, int N, int row, int col){
    for (int i=col-1; i >= 0; i--){
        // Primero se verifica que el grado asignado sea mayor o igual que al grado actual del nodo
        // Luego se verifica que el grado asignado sea menor o igual al grado posible del nodo
        if (matriz[row][i] != 0 && matriz[row][i] != -1 && matriz[row][i] != -2){
            if (matriz[row][i] < calcular_grado(matriz, N, row, i) || matriz[row][i] > calcular_posibles(matriz, N, row, i)){
                return 0;
            }
        }
    }
    for (int i=col+1; i < N; i++){
        if (matriz[row][i] != 0 && matriz[row][i] != -1 && matriz[row][i] != -2){
            if (matriz[row][i] < calcular_grado(matriz, N, row, i) || matriz[row][i] > calcular_posibles(matriz, N, row, i)){
                return 0;
            }
        }
    }
    for (int i=row-1; i >= 0; i--){
        if (matriz[i][col] != 0 && matriz[i][col] != -1 && matriz[i][col] != -2){
            if (matriz[i][col] < calcular_grado(matriz, N, i, col) || matriz[i][col] > calcular_posibles(matriz, N, i, col)){
                return 0;
            }
        }
    }
    for (int i=row+1; i < N; i++){
        if (matriz[i][col] != 0 && matriz[i][col] != -1 && matriz[i][col] != -2){
            if (matriz[i][col] < calcular_grado(matriz, N, i, col) || matriz[i][col] > calcular_posibles(matriz, N, i, col)){
                return 0;
            }
        }
    }
    return 1;
}

// Función que verifica si una matriz terminada es válida
int matriz_valida(int** matriz, int N){
    //Recorremos desde el final para mejorar la eficiencia (Es más probable que hayan ceros al final)
    for(int i = N - 1; i >= 0; i--)
    {
        for(int j = N - 1; j >= 0; j--)
        {
            if (matriz[i][j] == 0){
                return 0;
            }
            else if (matriz[i][j] != -1 && matriz[i][j] != -2){
                if (matriz[i][j] != calcular_grado(matriz, N, i, j)){
                    return 0;
                }
            }
        }
    }
    return 1;
}

// Función que determina los grados de cada nodo azul y cambia azules de grado 0 a rojos asignado al finalizar
void finalizar_matriz(int** matriz, int N){
    for(int i = 0; i < N; i++)
    {
        for(int j = 0; j < N; j++)
        {
            if (matriz[i][j] == -2){
                int grado = calcular_grado(matriz, N, i, j);
                if (grado == 0){
                    matriz[i][j] = -1;
                    visualizer_set_cell_color(i, j, RED);
                }
                else{
                    matriz[i][j] = grado; 
                    visualizer_set_cell_degree(i, j, grado);
                }
                visualizer_redraw();
                //usleep(100000);
            }
        }
    }
}

// Función que aplica la heuristica de comenzar por aquellos nodos en los que su posibilidad de grado es igual a su grado
int heuristica1(int** matriz, int N){
    int cambio = 0;
    for(int i = 0; i < N; i++)
    {
        for(int j = 0; j < N; j++)
        {
            if (matriz[i][j] != 0 && matriz[i][j] != -1 && matriz[i][j] != -2){
                if (matriz[i][j] == calcular_posibles(matriz, N, i, j) && matriz[i][j] != calcular_grado(matriz, N, i, j)){
                    pintar_posibles(matriz, N, i, j);
                    cambio = 1;
                }
            }
        }
    }
    return cambio;
}

// Función que cierra todos los caminos de un nodo que ya llegó a su grado
int heuristica2(int** matriz, int N){
    int cambio = 0;
    for(int i = 0; i < N; i++)
    {
        for(int j = 0; j < N; j++)
        {
            if (matriz[i][j] != 0 && matriz[i][j] != -1 && matriz[i][j] != -2){
                if (matriz[i][j] == calcular_grado(matriz, N, i, j) && matriz[i][j] != calcular_posibles(matriz, N, i, j)){
                    pintar_llenos(matriz, N, i, j);
                    cambio = 1;
                }
            }
        }
    }
    return cambio;
}

// Función que aplica la heuristica de comenzar por aquellos nodos en los que existe un único camino posible
int heuristica3(int** matriz, int N){
    int cambio = 0;
    for(int i = 0; i < N; i++)
    {
        for(int j = 0; j < N; j++)
        {
            if (matriz[i][j] != -1 && matriz[i][j] != -2){
                int posibles = 0;
                int rojos = 0;
                int eje = 0;
                int dir = 0;
                // Revisamos cuantos caminos posibles existen (1 a 4) y cuantos de estos son rojos
                if (j - 1 >= 0){
                    if (matriz[i][j-1] == -1){
                        rojos +=1;
                    }
                    else{
                        eje = 2;
                        dir = -1;
                    }
                    posibles += 1;
                }
                if (j + 1 < N){
                    if (matriz[i][j+1] == -1){
                        rojos +=1;
                    }
                    else{
                        eje = 2;
                        dir = 1;
                    }
                    posibles += 1;
                }
                if (i - 1 >= 0){
                    if (matriz[i-1][j] == -1){
                        rojos +=1;
                    }
                    else{
                        eje = 1;
                        dir = -1;
                    }
                    posibles += 1;
                }
                if (i + 1 < N){
                    if (matriz[i+1][j] == -1){
                        rojos +=1;
                    }
                    else{
                        eje = 1;
                        dir = 1;
                    }
                    posibles += 1;
                }

                // Si solo existe un posible camino se recorre este y se asigna color azul al número de grados y rojo al final
                if (posibles - rojos == 1){
                    
                    if (eje == 1){
                        int idx = i + dir;
                        for (int num = 1; num <= matriz[i][j]; num++){
                            if (idx >= 0 && idx < N && matriz[idx][j] == 0){
                                matriz[idx][j] = -2;
                                cambio = 1;
                                visualizer_set_cell_color(idx, j, BLUE);
                                visualizer_redraw();
                                //usleep(100000);
                            }
                            idx += dir;
                        }     
                    }
                    else{
                        int idx = j + dir;
                        for (int num = 1; num <= matriz[i][j]; num++){
                            if (idx >= 0 && idx < N && matriz[i][idx] == 0){
                                matriz[i][idx] = -2;
                                cambio = 1;
                                visualizer_set_cell_color(i, idx, BLUE);
                                visualizer_redraw();
                                //usleep(100000);
                            }
                            idx += dir;
                        }
                        
                    }
                }
                else if (posibles == rojos){
                    matriz[i][j] = -1;
                    cambio = 1;
                    visualizer_set_cell_color(i, j, RED);
                    visualizer_redraw();
                    //usleep(100000);
                }
            }
        }
    }
    return cambio;
}

// Función que aplica las heurísticas al inicio del proceso
void aplicar_heuristicas(int** matriz, int N){
    int cambio1 = heuristica1(matriz, N);
    int cambio2 = heuristica2(matriz, N);
    int cambio3 = heuristica3(matriz, N);
    if (cambio1 == 1 || cambio2 == 1 || cambio3 == 1){
        aplicar_heuristicas(matriz, N);
    }
}

// Función que imprime la matriz
void print_matriz(int** matriz, int N){
    for(int row = 0; row < N; row++)
    {
        for(int col = 0; col < N; col++)
        {
            printf("%i ", matriz[row][col]);
        }
        printf("\n");
    }
}

// Función que elimina la matriz
void destroy_matriz(int** matriz, int N){
    for(int row = 0; row < N; row++)
    {
        free(matriz[row]);
    }
    free(matriz);
}

// Función para encontrar el proximo lugar sin asignar
int* find_coords(int** matriz, int N, int row, int col){
    int* A = calloc(3, sizeof(int));
    A[0] = 0;
    A[1] = 0;
    A[2] = 0;

    
    for(int i = 0; i < N; i++)
    {
        for(int j = 0; j < N; j++)
        {
            if (matriz[i][j] != 0 && matriz[i][j] != -1 && matriz[i][j] != -2){
                if (matriz[i][j] == calcular_posibles(matriz, N, i, j)){
                    //Equivalente heuristica 1
                    if (matriz[i][j] != calcular_grado(matriz, N, i, j)){
                        for (int i2=j-1; i2 >= 0; i2--){
                            if (matriz[i][i2] != -1){
                                if (matriz[i][i2] == 0){
                                    A[0] = i;
                                    A[1] = i2;
                                    A[2] = -2;
                                    return A;
                                }
                            }
                            else{
                                break;
                            }
                        }
                        for (int i2=j+1; i2 < N; i2++){
                            if (matriz[i][i2] != -1){
                                if (matriz[i][i2] == 0){
                                    A[0] = i;
                                    A[1] = i2;
                                    A[2] = -2;
                                    return A;
                                }
                            }
                            else{
                                break;
                            }
                        }
                        for (int i2=i-1; i2 >= 0; i2--){
                            if (matriz[i2][j] != -1){
                                if (matriz[i2][j] == 0){
                                    A[0] = i2;
                                    A[1] = j;
                                    A[2] = -2;
                                    return A;
                                }
                            }
                            else{
                                break;
                            }
                        }
                        for (int i2=i+1; i2 < N; i2++){
                            if (matriz[i2][j] != -1){
                                if (matriz[i2][j] == 0){
                                    A[0] = i2;
                                    A[1] = j;
                                    A[2] = -2;
                                    return A;
                                }
                            }
                            else{
                                break;
                            }
                        }
                    }
                }
                else{
                    //Equivalente heuristica 2
                    if (matriz[i][j] == calcular_grado(matriz, N, i, j)){
                        for (int i2=j-1; i2 >= 0; i2--){
                            if (matriz[i][i2] != -1){
                                if (matriz[i][i2] == 0){
                                    A[0] = i;
                                    A[1] = i2;
                                    A[2] = -1;
                                    return A;
                                }
                            }
                            else{
                                break;
                            }
                        }
                        for (int i2=j+1; i2 < N; i2++){
                            if (matriz[i][i2] != -1){
                                if (matriz[i][i2] == 0){
                                    A[0] = i;
                                    A[1] = i2;
                                    A[2] = -1;
                                    return A;
                                }
                            }
                            else{
                                break;
                            }
                        }
                        for (int i2=i-1; i2 >= 0; i2--){
                            if (matriz[i2][j] != -1){
                                if (matriz[i2][j] == 0){
                                    A[0] = i2;
                                    A[1] = j;
                                    A[2] = -1;
                                    return A;
                                }
                            }
                            else{
                                break;
                            }
                        }
                        for (int i2=i+1; i2 < N; i2++){
                            if (matriz[i2][j] != -1){
                                if (matriz[i2][j] == 0){
                                    A[0] = i2;
                                    A[1] = j;
                                    A[2] = -1;
                                    return A;
                                }
                            }
                            else{
                                break;
                            }
                        }
                    } 
                    //Equivalente heuristica 3
                    else{
                        int posibles = 0;
                        int rojos = 0;
                        int eje = 0;
                        int dir = 0;
                        // Revisamos cuantos caminos posibles existen (1 a 4) y cuantos de estos son rojos
                        if (j - 1 >= 0){
                            if (matriz[i][j-1] == -1){
                                rojos +=1;
                            }
                            else{
                                eje = 2;
                                dir = -1;
                            }
                            posibles += 1;
                        }
                        if (j + 1 < N){
                            if (matriz[i][j+1] == -1){
                                rojos +=1;
                            }
                            else{
                                eje = 2;
                                dir = 1;
                            }
                            posibles += 1;
                        }
                        if (i - 1 >= 0){
                            if (matriz[i-1][j] == -1){
                                rojos +=1;
                            }
                            else{
                                eje = 1;
                                dir = -1;
                            }
                            posibles += 1;
                        }
                        if (i + 1 < N){
                            if (matriz[i+1][j] == -1){
                                rojos +=1;
                            }
                            else{
                                eje = 1;
                                dir = 1;
                            }
                            posibles += 1;
                        }

                        // Si solo existe un posible camino se recorre este y se asigna color azul al número de grados y rojo al final
                        if (posibles - rojos == 1){
                            
                            if (eje == 1){
                                int idx = i + dir;
                                for (int num = 1; num <= matriz[i][j]; num++){
                                    if (idx >= 0 && idx < N && matriz[idx][j] == 0){
                                        A[0] = idx;
                                        A[1] = j;
                                        A[2] = -2;
                                        return A;
                                    }
                                    idx += dir;
                                }     
                            }
                            else{
                                int idx = j + dir;
                                for (int num = 1; num <= matriz[i][j]; num++){
                                    if (idx >= 0 && idx < N && matriz[i][idx] == 0){
                                        A[0] = i;
                                        A[1] = idx;
                                        A[2] = -2;
                                        return A;
                                    }
                                    idx += dir;
                                }
                                
                            }
                        }
                        else if (posibles == rojos){
                            A[0] = i;
                            A[1] = j;
                            A[2] = -1;
                            return A;
                        }
                    }
                }
            }
        }
    }

   
    //Busqueda normal
    if (row){
        for (int i = row; i < N; i++){
            for (int j = 0; j < N; j++){
                if (i == row && j == 0){
                    j = col;
                }
                if (matriz[i][j] == 0){
                    A[0] = i;
                    A[1] = j;
                    return A;
                }
            }
        }
    }
    else{
        for (int i = 0; i < N; i++){
            for (int j = 0; j < N; j++){
                if (matriz[i][j] == 0){
                    A[0] = i;
                    A[1] = j;
                    return A;
                }
            }
        }
    }
    return A;
}

// Función para copiar una matriz a otra
void copiar_matriz(int** matriz1, int** matriz2, int N){
    for(int i = 0; i < N; i++)
    {
        for(int j = 0; j < N; j++)
        {
            matriz1[i][j] = matriz2[i][j];
        }
    }
}

// Función de backtracking para resolver el puzzle
int oh_yes(int** matriz, int N, int* posibles, int row, int col){
    if (matriz_valida(matriz, N)){
        return 1;
    }

    posibles[0] = -2;
    int largo_posibles = 2;

    int* A = find_coords(matriz, N, 0, 0);
    row = A[0];
    col = A[1];
    if (A[2] == -2){
        posibles[0] = -2;
        largo_posibles = 1;
    }
    else if (A[2] == -1){
        posibles[0] = -1;
        largo_posibles = 1;
    }
    free(A);


    if (matriz[row][col] == 0){
        for (int i=0; i < largo_posibles; i++){

            // Definimos el nodo como la posibilidad actual
            matriz[row][col] = posibles[i];

            //Descomentar para visualizar

            // Indicamos el color de la celda (row,col)
            if (posibles[i]==-2){     
                visualizer_set_cell_color(row, col, BLUE);
            }
            else{
                visualizer_set_cell_color(row, col, RED);
            }
            // destacamos una celda especifica y luego lo borramos
            visualizer_set_cell_highlight(row,col, true);
            visualizer_redraw();

            //usleep(30000);

            visualizer_set_cell_highlight(row,col, false);
            visualizer_redraw();

            //Revisamos si es válida esta asignación
            if(valido2(matriz, N, row, col) == 1){
                //Recursion
                if (oh_yes(matriz, N, posibles, row, col) == 1){
                    return 1;
                }

            }
            matriz[row][col] = 0;
            //Descomentar para visualizar
            visualizer_set_cell_color(row, col, NONE);
            visualizer_redraw();
            //usleep(30000);
        }
    }
    
    return 0;
}

// Función para crear lista ligada de nodos azules asignados
Node* crear_lista(int** matriz, int N){
    int existe_raiz = 0;
    Node* root;
    for(int i = 0; i < N; i++)
    {
        for(int j = 0; j < N; j++)
        {
            if (matriz[i][j] != 0 && matriz[i][j] != -1 && matriz[i][j] != -2){
                if (matriz[i][j] > calcular_grado(matriz, N, i, j)){
                    if (existe_raiz == 0){
                        root = node_init(matriz[i][j], i, j);
                        existe_raiz = 1;
                    }
                    else{
                        Node* node = node_init(matriz[i][j], i, j);
                        if (node->grado < root->grado){
                            node -> next = root;
                            root -> prev = node;
                            root = node;

                        }
                        else{
                            int added = 0;
                            Node* actual = root;
                            while (added == 0){
                                //si hay nodo siguiente se revisa si es menor a ese
                                if (actual -> next){
                                    Node* next_node = actual -> next;
                                    //Si es menor se agrega entremedio
                                    if (next_node -> grado >= node -> grado){
                                        actual -> next = node;
                                        node -> prev = actual;
                                        node -> next = next_node;
                                        next_node -> prev = node;
                                        added = 1;
                                    }
                                    //Si es mayor se avanza al siguiente
                                    else{
                                        actual = next_node;
                                    }
                                }
                                //Si no existe nodo siguiente se agrega al final de la lista ligada
                                else{
                                    actual -> next = node;
                                    node -> prev = actual;
                                    added = 1;
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    return root;
}

// Función que encuentra las coordenadas del proximo nodo a asignar en nuevo modelamiento
int* find_better(int** matriz, int N, Node* node){

    int* A = calloc(3, sizeof(int));
    int col = node -> col;
    int row = node -> row;
    A[2] = 0;


    //Heuristicas
    for(int i = 0; i < N; i++)
    {
        for(int j = 0; j < N; j++)
        {
            if (matriz[i][j] != 0 && matriz[i][j] != -1 && matriz[i][j] != -2){
                if (matriz[i][j] == calcular_posibles(matriz, N, i, j)){
                    //Equivalente heuristica 1
                    if (matriz[i][j] != calcular_grado(matriz, N, i, j)){
                        for (int i2=j-1; i2 >= 0; i2--){
                            if (matriz[i][i2] != -1){
                                if (matriz[i][i2] == 0){
                                    A[0] = i;
                                    A[1] = i2;
                                    A[2] = -2;
                                    return A;
                                }
                            }
                            else{
                                break;
                            }
                        }
                        for (int i2=j+1; i2 < N; i2++){
                            if (matriz[i][i2] != -1){
                                if (matriz[i][i2] == 0){
                                    A[0] = i;
                                    A[1] = i2;
                                    A[2] = -2;
                                    return A;
                                }
                            }
                            else{
                                break;
                            }
                        }
                        for (int i2=i-1; i2 >= 0; i2--){
                            if (matriz[i2][j] != -1){
                                if (matriz[i2][j] == 0){
                                    A[0] = i2;
                                    A[1] = j;
                                    A[2] = -2;
                                    return A;
                                }
                            }
                            else{
                                break;
                            }
                        }
                        for (int i2=i+1; i2 < N; i2++){
                            if (matriz[i2][j] != -1){
                                if (matriz[i2][j] == 0){
                                    A[0] = i2;
                                    A[1] = j;
                                    A[2] = -2;
                                    return A;
                                }
                            }
                            else{
                                break;
                            }
                        }
                    }
                }
                else{
                    //Equivalente heuristica 2
                    if (matriz[i][j] == calcular_grado(matriz, N, i, j)){
                        for (int i2=j-1; i2 >= 0; i2--){
                            if (matriz[i][i2] != -1){
                                if (matriz[i][i2] == 0){
                                    A[0] = i;
                                    A[1] = i2;
                                    A[2] = -1;
                                    return A;
                                }
                            }
                            else{
                                break;
                            }
                        }
                        for (int i2=j+1; i2 < N; i2++){
                            if (matriz[i][i2] != -1){
                                if (matriz[i][i2] == 0){
                                    A[0] = i;
                                    A[1] = i2;
                                    A[2] = -1;
                                    return A;
                                }
                            }
                            else{
                                break;
                            }
                        }
                        for (int i2=i-1; i2 >= 0; i2--){
                            if (matriz[i2][j] != -1){
                                if (matriz[i2][j] == 0){
                                    A[0] = i2;
                                    A[1] = j;
                                    A[2] = -1;
                                    return A;
                                }
                            }
                            else{
                                break;
                            }
                        }
                        for (int i2=i+1; i2 < N; i2++){
                            if (matriz[i2][j] != -1){
                                if (matriz[i2][j] == 0){
                                    A[0] = i2;
                                    A[1] = j;
                                    A[2] = -1;
                                    return A;
                                }
                            }
                            else{
                                break;
                            }
                        }
                    } 
                    //Equivalente heuristica 3
                    else{
                        int posibles = 0;
                        int rojos = 0;
                        int eje = 0;
                        int dir = 0;
                        // Revisamos cuantos caminos posibles existen (1 a 4) y cuantos de estos son rojos
                        if (j - 1 >= 0){
                            if (matriz[i][j-1] == -1){
                                rojos +=1;
                            }
                            else{
                                eje = 2;
                                dir = -1;
                            }
                            posibles += 1;
                        }
                        if (j + 1 < N){
                            if (matriz[i][j+1] == -1){
                                rojos +=1;
                            }
                            else{
                                eje = 2;
                                dir = 1;
                            }
                            posibles += 1;
                        }
                        if (i - 1 >= 0){
                            if (matriz[i-1][j] == -1){
                                rojos +=1;
                            }
                            else{
                                eje = 1;
                                dir = -1;
                            }
                            posibles += 1;
                        }
                        if (i + 1 < N){
                            if (matriz[i+1][j] == -1){
                                rojos +=1;
                            }
                            else{
                                eje = 1;
                                dir = 1;
                            }
                            posibles += 1;
                        }

                        // Si solo existe un posible camino se recorre este y se asigna color azul al número de grados y rojo al final
                        if (posibles - rojos == 1){
                            
                            if (eje == 1){
                                int idx = i + dir;
                                for (int num = 1; num <= matriz[i][j]; num++){
                                    if (idx >= 0 && idx < N && matriz[idx][j] == 0){
                                        A[0] = idx;
                                        A[1] = j;
                                        A[2] = -2;
                                        return A;
                                    }
                                    idx += dir;
                                }     
                            }
                            else{
                                int idx = j + dir;
                                for (int num = 1; num <= matriz[i][j]; num++){
                                    if (idx >= 0 && idx < N && matriz[i][idx] == 0){
                                        A[0] = i;
                                        A[1] = idx;
                                        A[2] = -2;
                                        return A;
                                    }
                                    idx += dir;
                                }
                                
                            }
                        }
                        else if (posibles == rojos){
                            A[0] = i;
                            A[1] = j;
                            A[2] = -1;
                            return A;
                        }
                    }
                }
            }
        }
    }
    

    for (int i=col-1; i >= 0; i--){
        if (matriz[row][i] == 0){
            A[0] = row;
            A[1] = i;
            return A;
        }
        else if (matriz[row][i] == -1 || matriz[row][i] == -3){
            break;
        }

    }
    for (int i=col+1; i < N; i++){
        if (matriz[row][i] == 0){
            A[0] = row;
            A[1] = i;
            return A;
        }
        else if (matriz[row][i] == -1 || matriz[row][i] == -3){
            break;
        }

    }
    for (int i=row-1; i >= 0; i--){
        if (matriz[i][col] == 0){
            A[0] = i;
            A[1] = col;
            return A;
        }
        else if (matriz[i][col] == -1 || matriz[i][col] == -3){
            break;
        }
    }
    for (int i=row+1; i < N; i++){
        if (matriz[i][col] == 0){
            A[0] = i;
            A[1] = col;
            return A;
        }
        else if (matriz[i][col] == -1 || matriz[i][col] == -3){
            break;
        }

    }


}

// Función que verifica si una matriz terminada es válida en nuevo modelamiento
int matriz_yeah(int** matriz, int N, Node* last){
    //Recorremos desde el final para mejorar la eficiencia (Es más probable que hayan ceros al final)
    /*for(int i = N - 1; i >= 0; i--)
    {
        for(int j = N - 1; j >= 0; j--)
        {
            if (matriz[i][j] != -1 && matriz[i][j] != -2 && matriz[i][j] != 0 && matriz[i][j] != -3){
                if (matriz[i][j] != calcular_grado(matriz, N, i, j)){
                    return 0;
                }
            }
        }
    }
    return 1;*/

    while (last){
        if (last -> grado != calcular_grado(matriz, N, last->row, last->col)){
            return 0;
        }
        last = last -> prev;
    }
    return 1;
}

// Función que determina los grador de los nodos azules determinados y le asigna color rojo al resto
void finalizar_yeah(int** matriz, int N){
    for(int i = 0; i < N; i++)
    {
        for(int j = 0; j < N; j++)
        {
            if (matriz[i][j] == -2){
                int grado = calcular_grado(matriz, N, i, j);
                if (grado == 0){
                    matriz[i][j] = -1;
                    visualizer_set_cell_color(i, j, RED);
                }
                else{
                    matriz[i][j] = grado; 
                    visualizer_set_cell_degree(i, j, grado);
                }
                visualizer_redraw();
                //usleep(100000);
            }
            else if (matriz[i][j] == 0 || matriz[i][j] == -3){
                matriz[i][j] = -1;
                visualizer_set_cell_color(i, j, RED);
                visualizer_redraw();
                //usleep(100000);
            }
            
            
        }
    }
}

// Función de backtracking con nueva modelación
int oh_yeah(int** matriz, int N, Node* node, int* posibles, Node* last){
    if (matriz_yeah(matriz, N, last)){
        return 1;
    }

    // avanzamos de nodo de ser necesario
    while (node -> grado == calcular_grado(matriz, N, node->row, node->col)){
        if (node -> next){
            node = node -> next;
        }
    }

    int* A = find_better(matriz, N, node);
    int row = A[0];
    int col = A[1];

    posibles[0] = -2;
    int largo_posibles = 2;

    if (A[2] == -2){
        posibles[0] = -2;
        largo_posibles = 1;
    }
    else if (A[2] == -1){
        posibles[0] = -1;
        largo_posibles = 1;
    }

    free(A);

    for (int i=0; i < largo_posibles; i++){

        // Definimos el nodo como la posibilidad actual
        matriz[row][col] = posibles[i];

        //Descomentar para visualizar

        // Indicamos el color de la celda (row,col)
        if (posibles[i]==-2){     
            visualizer_set_cell_color(row, col, BLUE);
        }
        else{
            visualizer_set_cell_color(row, col, RED);
        }

        // destacamos una celda especifica y luego lo borramos
        visualizer_set_cell_highlight(row,col, true);
        visualizer_redraw();

        //usleep(1000000);

        visualizer_set_cell_highlight(row,col, false);
        visualizer_redraw();

        //Revisamos si es válida esta asignación
        if(valido2(matriz, N, row, col) == 1){
            //Recursion
            if (oh_yeah(matriz, N, node, posibles, last) == 1){
                return 1;
            }

        }
        matriz[row][col] = 0;
        //Descomentar para visualizar
        visualizer_set_cell_color(row, col, NONE);
        visualizer_redraw();
        //usleep(1000000);
        
    }
    
    return 0;
}


