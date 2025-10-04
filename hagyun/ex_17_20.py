graph2={1:[2,3,4],2:[1,5],3:[1,6],4:[1,6],5:[2,6],6:[3,4,5]}

def dfs(graph,start_node):
    stack=[]
    visited=[]
    stack.append(start_node)
    while stack:
        node=stack.pop()
        print(f's-{stack}')
        if node not in visited:
            visited.append(node)
            stack.extend(reversed(graph[node]))
            print(f'v-{visited}')
    print(f'v:{visited}')
    return visited

def bfs(graph,start_node):
    queue=[]
    visited=[]
    queue.append(start_node)
    while queue:
        node=queue.pop()
        print(f's-{queue}')
        if node not in visited:
            visited.append(node)
            queue.extend(reversed(graph[node]))
            print(f'v-{visited}')
    print(f'v:{visited}')
    return visited
    
# dfs(graph2,1)
# bfs(graph2,1)