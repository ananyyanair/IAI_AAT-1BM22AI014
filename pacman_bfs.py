from collections import deque
def bfs(grid_rows, grid_cols, pac_row, pac_col, food_row, food_col, grid):
    directions = [(-1,0), (0,-1), (0,1), (1,0)]
    queue = deque([(int(pac_row), int(pac_col), [])])
    visited = set()
    visited.add((int(pac_row), int(pac_col)))
    nodes = []    
    while queue:
        r, c, path = queue.popleft()
        if (r, c) not in nodes:
            nodes.append((r, c))
            current_path = path + [(r, c)]
            if r == int(food_row) and c == int(food_col):
                return current_path, nodes            
            for direction in directions:
                next_row = r + direction[0]
                next_col = c + direction[1]                
                if (0 <= next_row < int(grid_rows) and 0 <= next_col < int(grid_cols) and 
                    (next_row, next_col) not in visited and grid[next_row][next_col] != "%"):
                    queue.append((next_row, next_col, current_path))
                    visited.add((next_row, next_col))                    
    return None, None
pacman = input()
pac_row, pac_col = pacman.split()
food = input()
food_row, food_col = food.split()
dim = input()
grid_rows, grid_cols = dim.split()
grid = [input().strip() for _ in range(int(grid_rows))]
path, nodes = bfs(grid_rows, grid_cols, pac_row, pac_col, food_row, food_col, grid)
if path is not None and nodes is not None:
    print(len(nodes))
    for node in nodes:
        print(node[0], node[1])    
    print(len(path) - 1)
    for node in path:
        print(node[0], node[1])
