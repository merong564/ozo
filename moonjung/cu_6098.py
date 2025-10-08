graph = []
for _ in range(10):
    graph.append(list(map(int, input().split())))
visited = [row[:] for row in graph]
# visited = graph         # 이렇게 복사해도 괜찮은지? 안됨. visited 바뀌면 graph까지 바뀜


start = 1, 1     # 행렬은 0부터 시작 -> 개미 출발 위치 (1, 1)
queue = [(1, 1)]    # 개미의 위치를 넣는 스택
# 유의! 이렇게 큐 만들면 안됨 queue = [list(start)]  


while queue:
    x, y = queue.pop(0)       # 개미의 현재 위치
    # print(f'현재위치: {x,y}')

    # 방문한 곳이면 넘기기
    if visited[x][y] == 9:
        continue

    # 맨 아래의 가장 오른쪽에 도착했거나, 먹이를 찾은 경우 방문처리 후 반복 종료
    if ((x, y) == (9, 9)) or (graph[x][y] == 2):        # 유의! x,y = 9,9 이렇게 쓰면 안됨
        visited[x][y] = 9
        break

    # 더이상 움직일 수 없는 경우 반복 종료
    if x > 10 or y > 10:
        break

    # 현재 위치가 갈 수 있는 곳이면 방문처리 후 이동
    if graph[x][y] == 0:
        visited[x][y] = 9

        # 오른쪽으로 갈 수 있으면 큐에 오른쪽 좌표 추가
        if graph[x][y+1] == 0 or graph[x][y+1] == 2:        # 유의! 2일 때도 갈 수 있음
            queue.append((x, y+1))

        # 아니면 아래쪽 좌표 추가
        else:
            queue.append((x+1, y))

    # 현재 위치에 벽이 있는 경우 넘기기
    elif graph[x][y] == 1:
        continue



for row in visited:
    print(*row)

        




