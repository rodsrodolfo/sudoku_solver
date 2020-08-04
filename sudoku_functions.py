from numpy import matrix as npmatrix


def possible(n, x, y, grid):
    """determina se é possível um numero n ser
    colocado na posição x y de um grid de sudoku"""
    grid = npmatrix(grid)
    if n in grid[y, :]:
        return False
    if n in grid[:, x]:
        return False
    if n in grid[y // 3 * 3: y // 3 * 3 + 3, x // 3 * 3: x // 3 * 3 + 3]:
        return False
    else:
        return True


def solve(_sudoku):
    """resolve um sudoku em forma de np.matrix,
    depende da funçao possible"""
    for y in range(9):
        for x in range(9):
            if _sudoku[y][x] == 0:
                for n in range(1, 10):
                    if possible(n, x, y, _sudoku):
                        _sudoku[y][x] = n
                        solve(_sudoku)
                        _sudoku[y][x] = 0
                        #print(npmatrix(_sudoku))
                return
                #print('impossible sudoku')
    print('\n')
    print('\n')
    print('\n')
    print(npmatrix(_sudoku))
    input('\nmore? ')
