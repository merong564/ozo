def DFS(graph, start):
    stack = list()              # DFS -> stack 사용
    visited = list()            # 방문한 노드를 리스트에 저장

    stack.append(start)         # 시작 노드를 stack에 저장

    # stack에 남은 노드가 없을 때까지 반복
    while stack:
        node = stack.pop()      # stack 끝에서 노드 꺼내기

        if node not in visited:     # 아직 방문하지 않았을 경우
            visited.append(node)    # 방문처리
            stack.extend(reversed(graph[node]))       # 해당 노드와 연결된 모든 노드를 stack에 저장
                                                      # reversed 사용 이유: 작은 수부터 순서대로 꺼내기 위함
    return visited

def BFS(graph, start):
    queue = list()              # BFS -> queue 사용
    visited = list()            # 방문한 노드를 리스트에 저장

    queue.append(start)         # 시작 노드를 queue에 저장

    # queue에 남은 노드가 없을 때까지 반복
    while queue:                
        node = queue.pop(0)     # queue 처음에서 노드 꺼내기
        if node not in visited:     # 아직 방문하지 않았을 경우
            visited.append(node)    # 방문처리
            queue.extend(graph[node])     # 해당 노드와 연결된 모든 노드를 queue에 저장

    return visited               
        


graph = {1:[2, 3, 4], 
         2:[1, 5], 
         3:[1, 6], 
         4:[1, 6], 
         5:[2, 6], 
         6:[3, 4, 5]}

result_DFS = DFS(graph, 1)
result_BFS = BFS(graph, 1)
print(f'DFS 결과: {result_DFS}, BFS 결과: {result_BFS}')

