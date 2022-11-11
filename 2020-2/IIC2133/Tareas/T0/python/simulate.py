import sys
from typing import Tuple, List
from mould import Mould
from cell import Cell

def fscanf(string: str) -> Tuple[str, str]:
    """
    Función para leer parcialmente una línea.
    Esta función permite hacer una equivalencia
    más directa con la función 'fscanf' de C
    y no es necesario que la reescriban.
    Ejemplo de uso:
    a, b = fscanf("hola como estas")
    a -> "hola"
    b -> "como estas"
    """
    space = string.find(' ')
    if space == -1:
        return string, ''
    else:
        return string[:space], string[space+1:]

def check_arguments(argc: int, argv: List[str]):
    if argc != 3:
        print(f"Modo de uso: python3 {argv[0]} INPUT OUTPUT")
        print("Donde:")
        print("\tINPUT es la ruta del archivo de input")
        print("\tOUTPUT es la ruta del archivo de output")
        return False
    return True

# Programa principal
if __name__ == "__main__":

    # Si los parámetros del programa son inválidos
    if not check_arguments(len(sys.argv), sys.argv):
        # Salimos del programa indicando que no terminó correctamente
        sys.exit(1)

        
    # Inicializamos el MOULD
    mould = Mould()

    # Abrimos el archivo de input
    input_file = open(sys.argv[1], 'r')

    # Abrimos archivo de output
    output_file = open(sys.argv[2], 'w')

    # Número de líneas a leer
    n_lines = int(input_file.readline().strip())

    # Mientras existan líneas
    while n_lines > 0:

        # Disminuímos el número de líneas por leer en 1
        n_lines -= 1

        # Leemos la línea
        line = input_file.readline().strip()

        # Obtenemos el comando
        command, line = fscanf(line)

        # Caso 1: Comando GROW
        if command == "GROW":

            # Partimos desde la raíz
            cur = mould.root

            # Obtenemos la profundidad de la célula que crecerá
            depth, line = fscanf(line)

            # Iteramos hasta llegar a dicha célula
            for level in range(int(depth)):

                # Obtenemos el índice
                idx, line = fscanf(line)

                # Cambiamos la célula actual
                cur = cur.children[int(idx)]
            
            # Obtenemos en qué posición crear una nueva célula
            idx, line = fscanf(line)

            # La creamos
            mould.add_cell(cur, int(idx))

        # Caso 2: Comando CLONE
        elif command == "CLONE":

            # Partimos desde la raíz
            cell_to_clone = mould.root

            # Obtenemos la profundidad de la célula a clonar
            depth, line = fscanf(line)

            # Iteramos hasta encontrar la célula
            for level in range(int(depth)):

                # Obtenemos el índice
                idx, line = fscanf(line)

                # Cambiamos la célula actual
                cell_to_clone = cell_to_clone.children[int(idx)]

            # Partimos desde la raíz
            parent = mould.root

            # Obtenemos la profundidad de la célula donde será clonada
            depth, line = fscanf(line)

            # Iteramos hasta dicha profundidad
            for level in range(int(depth)):

                # Obtenemos el índice
                idx, line = fscanf(line)

                # Cambiamos la célula actual
                parent = parent.children[int(idx)]

            # Obtenemos la posición donde será clonada
            cloned_node_idx, line = fscanf(line)

            # La clonamos
            parent.children[int(cloned_node_idx)] = mould.copy_cell(cell_to_clone)
        
        # Caso 3: Comando CROSSOVER
        elif command == "CROSSOVER":

            # Partimos desde la raíz
            parent_1 = mould.root

            # Obtenemos la profundidad de la célula madre 1
            depth, line = fscanf(line)

            # Iteramos hasta dicha profundidad
            for level in range(int(depth)):

                # Obtenemos el índice
                idx, line = fscanf(line)

                # Cambiamos la célula actual
                parent_1 = parent_1.children[int(idx)]

            # Obtenemos el índice de la primera hija
            child_1_idx, line = fscanf(line)

            # Obtenemos dicha hija
            child_1 = parent_1.children[int(child_1_idx)]

            # Partimos desde la raíz
            parent_2 = mould.root

            # Obtenemos la profundidad de la célula madre 2
            depth, line = fscanf(line)

            # Iteramos hasta dicha profundidad
            for level in range(int(depth)):

                # Obtenemos el índice
                idx, line = fscanf(line)

                # Cambiamos la célula actual
                parent_2 = parent_2.children[int(idx)]
            
            # Obtenemos el índice de la segunda hija
            child_2_idx, line = fscanf(line)

            # Obtenemos dicha hija
            child_2 = parent_2.children[int(child_2_idx)]

            # Hacemos el intercambio
            parent_1.children[int(child_1_idx)] = child_2
            parent_2.children[int(child_2_idx)] = child_1
        
        # Caso 4: Comando BUD
        elif command == "BUD":

            # Partimos desde la raíz
            cur = mould.root

            # Obtenemos la profundidad de la célula
            depth, line = fscanf(line)

            # Iteramos hasta dicha célula
            for level in range(int(depth)):

                # Obtenemos el índice
                idx, line = fscanf(line)

                # Cambiamos la célula actual
                cur = cur.children[int(idx)]
        
            # Obtenemos el índice de la hija a eliminar
            idx, line = fscanf(line)

            # La eliminamos
            cur.delete(int(idx))
        
        # Caso 5: Comando ABSORB
        elif command == "ABSORB":

            # Partimos desde la raíz
            parent_1 = mould.root

            # Obtenemos la profundidad
            depth, line = fscanf(line)

            # Iteramos hasta dicha profundidad
            for level in range(int(depth)):

                # Obtenemos el índice
                idx, line = fscanf(line)

                # Cambiamos la célula actual
                parent_1 = parent_1.children[int(idx)]

            # Obtenemos el índice de la hija que reemplazaremos
            new_idx, line = fscanf(line)

            # Obtenemos dicha hija
            parent_2 = parent_1.children[int(new_idx)]

            # Obtenemos la profundidad del camino por continuar
            depth, line = fscanf(line)

            # Iteramos por ese camino hasta la penúltima célula
            for level in range(int(depth) - 1):

                # Obtenemos el índice
                idx, line = fscanf(line)

                # Cambiamos la célula actual
                parent_2 = parent_2.children[int(idx)]

            # Obtenemos el índice de la célula que quedará
            idx, line = fscanf(line)

            # Obtenemos dicha célula
            child = parent_2.children[int(idx)]

            # Desvinculamos a la madre
            parent_2.children[int(idx)] = None

            # Reemplazamos
            parent_1.children[int(new_idx)] = child
        
        # Caso 7: Comando OBSERVE
        elif command == "OBSERVE":

            # Definimos el índice inicial
            idx = -1

            # Partimos de la raíz
            current = mould.root

            # Obtenemos la profundidad de la célula a observar
            depth, line = fscanf(line)

            # Iteramos hasta dicha profundidad
            for level in range(int(depth)):

                # Obtenemos el índice
                idx, line = fscanf(line)

                # Cambiamos la célula actual
                current = current.children[int(idx)]

            # Distinguimos el estado
            print("STATE", file=output_file)

            # Obtenemos los datos de nuestra célula
            current.observe(0, int(idx), output_file)

    # Cerramos archivo de lectura
    input_file.close()

    # Cerramos archivo de escritura
    output_file.close()


