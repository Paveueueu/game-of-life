
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




def step(toggled_cells: set[tuple[int, int]], rules: tuple[list[int], list[int]]):
    result_cells = set()
    neighbors = {
        cell: count_neighbors(cell, toggled_cells)
        for cell in toggled_cells
    }

    rules_live = rules[0]
    rules_die = rules[1]

    for cell in toggled_cells:
        for neighbor in [(cell[0] + offset[0], cell[1] + offset[1]) for offset in OFFSETS]:
            # if a neighbor is dead & not to be alive next turn, toggle him alive (according to the rules)
            if neighbor not in toggled_cells:
                if neighbor not in result_cells:
                    count = count_neighbors(neighbor, toggled_cells) # neighbors of the neighbor
                    if count in rules_live:
                        result_cells.add(neighbor)

            # if cell is not supposed to die, toggle him alive next turn
            if neighbors[cell] not in rules_die:
                result_cells.add(cell)

    return result_cells
