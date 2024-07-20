def dfs(grid_rows, grid_cols, pac_row, pac_col, food_row, food_col, grid):    
    stack = []
    visited = []
    path = []
    directions = [(-1,0), (0,-1), (0,1), (1,0)]
    nodes = []   
    stack.append((int(pac_row), int(pac_col), path))
    visited.append((int(pac_row), int(pac_col)))    
    while stack:
        r, c, path = stack.pop()
        if (r, c) not in nodes:
            nodes.append((r, c))
            path.append((r, c))           
            if r == int(food_row) and c == int(food_col):
                return path, nodes           
            for direction in directions:
                next_row = r + direction[0]
                next_col = c + direction[1]                
                if (0 <= next_row < int(grid_rows) and 0 <= next_col < int(grid_cols) and (next_row, next_col) not in visited and grid[next_row][next_col] != "%"):
                    stack.append((next_row, next_col, path.copy()))
                    visited.append((next_row, next_col))    
    return None, None
pacman = input()
pac_row, pac_col = pacman.split()
food = input()
food_row, food_col = food.split()
dim = input()
grid_rows, grid_cols = dim.split()
grid = []
for i in range(int(grid_rows)):
    grid.append(input())
path, nodes = dfs(grid_rows, grid_cols, pac_row, pac_col, food_row, food_col, grid)
if path is not None and nodes is not None:
    print(len(nodes))
    for node in nodes:
        print(node[0], node[1])

    print(len(path) - 1)
    for node in path:
        print(node[0], node[1])
