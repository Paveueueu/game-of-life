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


# normal rules
# ----------------

def count_neighbors(cell: tuple[int, int], toggled_cells: set[tuple[int, int]]) -> int:
    """
        Counts all living neighbors of the cell.

        Args:
            cell (tuple[int, int]): (row, column) tuple
            toggled_cells (set[tuple[int, int]]): list of all living cells

        Returns:
            int: number of living neighbors
    """
    count = 0
    for offset in OFFSETS:
        if (cell[0] + offset[0], cell[1] + offset[1]) in toggled_cells:
            count += 1
    return count


def step(toggled_cells: set[tuple[int, int]], rules: tuple[list, list]) -> list[tuple[int, int]]:
    """
        Run one step of the simulation.

        Args:
            toggled_cells (set[tuple[int, int]]): list of all living cells
            rules (tuple[list, list]): list of user-set rules (live-rules, die-rules)

        Returns:
            set[tuple[int, int]]: updated set of living cells
    """
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
                    count = count_neighbors(neighbor, toggled_cells)  # neighbors of the neighbor
                    if count in rules_live:
                        result_cells.add(neighbor)

            # if cell is not supposed to die, keep him alive
            if neighbors[cell] not in rules_die:
                result_cells.add(cell)

    return result_cells


# wrapping variant
# ----------------

def count_neighbors_wrap_around(cell: tuple[int, int], toggled_cells: set[tuple[int, int]], board_size: int):
    """
        Counts all living neighbors of the cell. Board wrapping enabled.

        Args:
            cell (tuple[int, int]): (row, column) tuple
            toggled_cells (set[tuple[int, int]]): list of all living cells
            board_size (int): size of the board

        Returns:
            int: number of living neighbors
    """
    count = 0
    for offset in OFFSETS:
        neighbor = ((cell[0] + offset[0]) % board_size, (cell[1] + offset[1]) % board_size)
        if neighbor in toggled_cells:
            count += 1
    return count


def step_wrap_around(toggled_cells: set[tuple[int, int]], rules: tuple[list, list], board_size: int):
    """
        Run one step of the simulation. Board wrapping enabled.

        Args:
            toggled_cells (set[tuple[int, int]]): list of all living cells
            rules (tuple[list, list]): list of user-set rules (live-rules, die-rules)
            board_size (int): size of the board

        Returns:
            list[tuple[int, int]]: updated list of living cells
    """
    result_cells = set()
    neighbors = {
        cell: count_neighbors_wrap_around(cell, toggled_cells, board_size)
        for cell in toggled_cells
    }

    rules_live = rules[0]
    rules_die = rules[1]

    for cell in toggled_cells:
        for offset in OFFSETS:
            neighbor = ((cell[0] + offset[0]) % board_size, (cell[1] + offset[1]) % board_size)
            # if a neighbor is dead & not to be alive next turn, toggle him alive (according to the rules)
            if neighbor not in toggled_cells:
                if neighbor not in result_cells:
                    count = count_neighbors_wrap_around(neighbor, toggled_cells, board_size)
                    if count in rules_live:
                        result_cells.add(neighbor)

            # if cell is not supposed to die, keep him alive
            if neighbors[cell] not in rules_die:
                result_cells.add(cell)

    return result_cells
