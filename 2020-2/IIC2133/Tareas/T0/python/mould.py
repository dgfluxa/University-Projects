from cell import Cell

class Mould:
    def __init__(self) -> None:
        self.root = Cell(0)
        self.id = 1

    def copy_cell(self, cell: Cell) -> Cell:
        """
        Función para clonar una célula.
        """

        # Si la célula existe
        if cell is not None:

            # Creamos una nueva célula
            new = Cell(self.id)

            # Aumentamos el identificador global
            self.id += 1

            # Por cada una de las células
            for i in range(10):

                # Clonamos la hija
                new.children[i] = self.copy_cell(cell.children[i])
            
            # Retornamos el clon
            return new

        # Si la célula no existe, no hay clon
        return None

    def add_cell(self, cell: Cell, idx: int) -> None:
        """
        Función para agregar una célula en un determinado índice.
        """
        
        # Agregamos la célula
        cell.children[idx] = Cell(self.id)

        # Aumentamos el ídentificador global
        self.id += 1

