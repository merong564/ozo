from collections import deque

graph = {
    1: [2,3,4],
    2: [1,5],
    3: [1,6],
    4: [1,6],
    5: [2,6],
    6: [3,4,5]
}

def dfs_recursive(start):
    visited, order = set(), []
    def dfs(u):
        visited.add(u)
        order.append(u)
        for v in graph[u]:
            if v not in visited:
                dfs(v)
    dfs(start)
    return order

def bfs_queue(start):
    visited, order = {start}, []
    q = deque([start])
    while q:
        u = q.popleft()
        order.append(u)
        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                q.append(v)
    return order

print("DFS(rec):", dfs_recursive(1))  
print("BFS:",      bfs_queue(1))      
