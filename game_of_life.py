
OFFSETS = [
    (-1, -1),
    (-1, +0),
    (-1, +1),

    (+0, -1),
    (+0, +1),

    (+1, -1),
    (+1, +0),
    (+1, +1),
]


def count_neighbors(cell, toggled_cells):
    count = 0

    for offset in OFFSETS:
        if (cell[0] + offset[0], cell[1] + offset[1]) in toggled_cells:
            count += 1

    return count




def step(toggled_cells: set[tuple[int, int]]):
    result_cells = set()
    neighbors = {
        cell: count_neighbors(cell, toggled_cells)
        for cell in toggled_cells
    }

    for cell in toggled_cells:
        for offset in OFFSETS:
            nb = (cell[0] + offset[0], cell[1] + offset[1])
            if nb not in toggled_cells:
                if nb not in result_cells:
                    if count_neighbors(nb, toggled_cells) == 3:
                        result_cells.add(nb)

            if neighbors[cell] == 3 or neighbors[cell] == 2:
                result_cells.add(cell)

    return result_cells
