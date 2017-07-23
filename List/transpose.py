from __future__ import print_function
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
def transpose(grid):
    transposed = [['' for i in range(len(grid))] for i in range(len(grid[0]))]
    for i in range(0, len(grid[0])):
        for j in range(0, len(grid)):
            #transposed[i][j] = grid[j][i]
            print(grid[j][i], end='')
        print()
    return transposed
transpose(grid)
#print(transpose(grid))
exit()