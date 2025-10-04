def solution(maps):
    queue = list()
    queue.append((0,0))         # 시작위치 (0,0)를 큐에 추가
    
    n = len(maps)               # maps의 행 길이 n
    m = len(maps[0])            # maps의 열 길이 m

    # 이동 가능한 방식: 상하좌우
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    # 큐가 빌 때까지 반복
    while queue:
        x, y  = queue.pop(0)                # 큐에서 좌표 꺼내기 -> 현재 위치가 됨
        for i in range(4):                  # 현재 위치에서 상하좌우로 탐색
            nx, ny = x+dx[i], y+dy[i]            

            if 0<=nx<n and 0<=ny<m:         # 탐색한 좌표가 maps 범위 안에 있을 경우
                if maps[nx][ny] == 1:       # 탐색한 좌표가 갈 수 있는 길일 경우 큐에 추가
                    queue.append((nx, ny))
                    maps[nx][ny] = maps[x][y] + 1       # 해당 좌표에 지금까지 이동한 거리를 표시
                    
    if maps[n-1][m-1] != 0 and maps[n-1][m-1] != 1:         # 상대팀 진영의 값이 0, 1이 아닐 경우 반환 (도달 가능함)
        return maps[n-1][m-1]    
    
    else:                                   # 도달 불가능할 경우 -1 반환
        return -1

    