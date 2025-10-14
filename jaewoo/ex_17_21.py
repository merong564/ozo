def build_grid(n_rows, n_cols, walls):
    g = [[0]*n_cols for _ in range(n_rows)]
    for r, c in walls:
        g[r-1][c-1] = 1
    return g

walls = {(1,3),(1,5),(2,1),(2,3),(3,4),(4,2),(5,4),(5,5)}  
grid2 = build_grid(5, 5, walls)

for row in grid2:
    print(row)





print('---------------------')

graph = []
for _ in range(5):
    row = [int(s) for s in input()]
    graph.append(row)

print(graph)