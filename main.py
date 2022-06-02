# User Input
M = int( input("Donner la puissance P de taille " ));
X = int (input("Donner la colonne C de trou "));
Y = int (input("Donner la ligne L de trou "));
N = 2**M
grid = [[0 for i in range(N)] for j in range(N)]
grid[Y][X] = -1
symbols = list(range(N*N))


def tiling(n, x, y, a, b, i):

    # n : size of grid
    #a,b,c,d : corners of sub-grid
    # x, y : position of filled tile in current grid


    show()

    # Base Case -> place 3 OTHER Tiles
    if n == 2:
        # Top Left Quarter
        if x-a < n//2 and y-b < n//2:
            grid[b+n//2-1][a+n//2] = symbols[i+1]
            grid[b+n//2][a+n//2] = symbols[i+1]
            grid[b+n//2][a+n//2-1] = symbols[i+1]
        # Top Right Quarter
        if x-a >= n//2 and y-b < n//2:
            grid[b+n//2-1][a+n//2-1] = symbols[i+1]
            grid[b+n//2][a+n//2] = symbols[i+1]
            grid[b+n//2][a+n//2-1] = symbols[i+1]
        # Bottom Left Quarter
        if x-a < n//2 and y-b >= n//2:
            grid[b+n//2-1][a+n//2-1] = symbols[i+1]
            grid[b+n//2-1][a+n//2] = symbols[i+1]
            grid[b+n//2][a+n//2] = symbols[i+1]
        # Bottom Right Quarter
        if x-a >= n//2 and y-b >= n//2:
            grid[b+n//2-1][a+n//2-1] = symbols[i+1]
            grid[b+n//2-1][a+n//2] = symbols[i+1]
            grid[b+n//2][a+n//2-1] = symbols[i+1]
        i += 1
        return i

    # if n>2
    # Place Middle Tile
    # Top Left Quarter
    if x-a < n//2 and y-b < n//2:
        grid[b+n//2-1][a+n//2] = symbols[i+1]
        grid[b+n//2][a+n//2] = symbols[i+1]
        grid[b+n//2][a+n//2-1] = symbols[i+1]
    # Top Right Quarter
    if x-a >= n//2 and y-b < n//2:
        grid[b+n//2-1][a+n//2-1] = symbols[i+1]
        grid[b+n//2][a+n//2] = symbols[i+1]
        grid[b+n//2][a+n//2-1] = symbols[i+1]
    # Bottom Right Quarter
    if x-a < n//2 and y-b >= n//2:
        grid[b+n//2-1][a+n//2-1] = symbols[i+1]
        grid[b+n//2-1][a+n//2] = symbols[i+1]
        grid[b+n//2][a+n//2] = symbols[i+1]
    # Bottom Left Quarter
    if x-a >= n//2 and y-b >= n//2:
        grid[b+n//2-1][a+n//2-1] = symbols[i+1]
        grid[b+n//2-1][a+n//2] = symbols[i+1]
        grid[b+n//2][a+n//2-1] = symbols[i+1]
    i += 1
    # Recursion
    # Top Left Quarter
    if x-a < n//2 and y-b < n//2:
        i = tiling(n//2, x, y, a, b, i)
        i = tiling(n//2, a+n//2, b+n//2-1, a+n//2, b, i)
        i = tiling(n//2, a+n//2, b+n//2, a+n//2, b+n//2, i)
        i = tiling(n//2, a+n//2-1, b+n//2, a, b+n//2, i)
    # Top Right Quarter
    if x-a >= n//2 and y-b < n//2:
        i = tiling(n//2, a+n//2-1, b+n//2-1, a, b, i)
        i = tiling(n//2, x, y, a+n//2, b, i)
        i = tiling(n//2, a+n//2, b+n//2, a+n//2, b+n//2, i)
        i = tiling(n//2, a+n//2-1, b+n//2, a, b+n//2, i)
    # Bottom Right Quarter
    if x-a >= n//2 and y-b >= n//2:
        i = tiling(n//2, a+n//2-1, b+n//2-1, a, b, i)
        i = tiling(n//2, a+n//2, b+n//2-1, a+n//2, b, i)
        i = tiling(n//2, x, y, a+n//2, b+n//2, i)
        i = tiling(n//2, a+n//2-1, b+n//2, a, b+n//2, i)
    # Bottom Left Quarter
    if x-a < n//2 and y-b >= n//2:
        i = tiling(n//2, a+n//2-1, b+n//2-1, a, b, i)
        i = tiling(n//2, a+n//2, b+n//2-1, a+n//2, b, i)
        i = tiling(n//2, a+n//2, b+n//2, a+n//2, b+n//2, i)
        i = tiling(n//2, x, y, a, b+n//2, i)
    return i

def show():
    for i in grid:
        for j in i:
            print(str(j).rjust(3), end=' ')
        print()
    print()


tiling(N, X, Y, 0, 0, 0)
print("Final : ")
show()