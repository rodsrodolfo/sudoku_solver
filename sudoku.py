import sudoku_functions as sf

txt_version = 1
filename = f'sudoku_{txt_version}.txt'

with open(filename) as sudoku_file:  # with fecha o arquivo quando acaba o loop, mais seguro
    sudoku = []
    for line in sudoku_file:
        sudoku.append(line.split())

for y in range(9):
    for x in range(9):
        sudoku[y][x] = int(sudoku[y][x])

sf.solve(sudoku)
