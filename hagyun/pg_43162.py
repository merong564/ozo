def solution(n, computers):
    network={}
    answer=n
    for y in range(0,n):
        lines=[]
        for x in range(0,n):
            if computers[y][x]==1:
                lines.append(x)
        network[y]=lines
    visited=set()
    # set : 집합, iterable하고 순서 없는 리스트 느낌
    # 중복해서 add해도 한 번만 들어감 
    for net in network:
        if net not in visited:
            stack = [net]
            visited.add(net)
            group_size=1
            while stack:
                current=stack.pop()
                for c in network.get(current,[]):
                    # 딕셔너리를 건드리지 않고 current key의 value만 가져옴
                    # 없으면 [] 반환
                    if c not in visited:
                        visited.add(c)
                        stack.append(c)
                        group_size+=1
            answer-=(group_size-1)
    return answer









# 딕셔너리 메서드 setdefault(key,value)
# key가 있으면 값 유지 및 그 값 반환, 없으면 value 추가 후 그 값 반환
# setdefault(key,[]).append(value) 형식으로 반복문에도 사용 가능


## gpt-1
def solution(n, computers):
    visited = [False] * n  # 방문 여부 기록

    def dfs(node):
        visited[node] = True
        for neighbor in range(n):
            if computers[node][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor)

    answer = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1  # 하나의 네트워크를 모두 방문하고 나서 +1

    return answer


## gpt-2
# Union-Find(Disjoint Set) : 서로소 찾기
def solution(n, computers):
    parent = [i for i in range(n)]  # 처음엔 자기 자신이 부모

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]  # 경로 압축
            x = parent[x]
        return x

    def union(a, b):
        rootA = find(a)
        rootB = find(b)
        if rootA != rootB:
            parent[rootB] = rootA  # 한 그룹으로 합침
            return True
        return False

    answer = n
    for i in range(n):
        for j in range(i + 1, n):
            if computers[i][j] == 1:
                if union(i, j):
                    answer -= 1  # 그룹 합칠 때만 네트워크 수 감소

    return answer
