"""Given an NxM matrix, if a cell is zero, set entire row and column to zeroes.

A matrix without zeroes doesn't change:

    >>> zero_matrix([[1, 2 ,3], [4, 5, 6], [7, 8, 9]])
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

But if there's a zero, zero both that row and column:

    >>> zero_matrix([[1, 0, 3], [4, 5, 6], [7, 8, 9]])
    [[0, 0, 0], [4, 0, 6], [7, 0, 9]]

Make sure it works with non-square matrices:

    >>> zero_matrix([[1, 0, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    [[0, 0, 0, 0], [5, 0, 7, 8], [9, 0, 11, 12]]
"""


def zero_matrix(matrix):
    """Given an NxM matrix, for cells=0, set their row and column to zeroes."""

    zeroes_rows = set()
    zeroes_cols = set()

    for row_idx, row in enumerate(matrix):
        if 0 in set(row):
            for col_idx, cell in enumerate(row):
                if cell == 0:
                    zeroes_rows.add(row_idx)
                    zeroes_cols.add(col_idx)

    for row_pos in zeroes_rows:
        for idx in range(0, len(matrix[row_pos])):
            matrix[row_pos][idx] = 0

    for col_pos in zeroes_cols:
        for row_idx, row in enumerate(matrix):
            matrix[row_idx][col_pos] = 0

    return matrix



if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** TESTS PASSED! YOU'RE DOING GREAT!\n")
