from typing import TextIO

class Cell:
    def __init__(self, cell_id: int) -> None:
        
        # Definimos su identificador
        self.id = cell_id

        # Definimos sus 10 hijas
        self.children = [None, None, None, None, None, None, None, None, None, None]
    
    def observe(self, spacing: int, idx: int, file: TextIO) -> None:
        """
        Función para guardar en un archivo
        el estado de una célula y sus hijas,
        recursivamente.
        """

        # Escribimos el espaciado
        for _ in range(spacing):
            print("   ", end='', file=file)

        # Escribimos el índice de la célula y su identificador
        if idx == -1:
            print("r:0", file=file)
        else:
            print(f"{idx}:{self.id}", file=file)

        # Por cada hija
        for i in range(10):

            # Obtenemos a la hija
            child = self.children[i]

            # Si existe
            if child is not None:

                # La observamos
                child.observe(spacing + 1, i, file)

    def delete(self, idx: int) -> None:
        """
        Función para eliminar una célula hija en índice 'idx'.
        """
        self.children[idx] = None
