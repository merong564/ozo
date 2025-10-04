# 17차시 강의 중 따로 알려주신 얼음틀 문제 풀이
# 입력이 아래와 같은 형식이라고 가정
# 4 5
# 00110
# 00011
# 11111
# 00000

def dfs(graph, sx, sy):       # 파라미터: 그래프, 탐색 시작 위치 (sx,sy)
    if graph[sx][sy] != 0:    # 시작 위치의 값이 0일 때만 탐색 진행
        return
    
    stack = list()
    stack.append((sx,sy))       # 시작 위치를 스택에 추가
    graph[sx][sy] = 1           # 방문 처리 (중복 탐색 방지)
   

    while stack:
        x, y = stack.pop()      # 현재 위치 x,y

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]       # 상하좌우로 새로운 위치 탐색
            
            # 그래프의 범위 내 위치이고 값이 0일 경우
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 0:        
                graph[nx][ny] = 1               # 방문처리
                stack.append((nx,ny))           # 스택에 추가

    return True                  # 탐색 완료 후 True 반환
    


n, m = map(int, input().split())
graph = []
for _ in range(n):
    row = input()       # 그래프의 한 줄마다 문자열로 입력 받기
    graph.append([int(char) for char in row])       # 문자열의 문자마다 정수 처리
# print(graph)          # 그래프 제대로 만들어졌는지 확인

# 아래와 같은 한 줄로 그래프 생성 가능
# graph = [list(map(int, input())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

cnt = 0             # 얼음틀 개수 (= 탐색 횟수)

for i in range(n):
    for j in range(m):
        if dfs(graph, i, j):        # dfs 결과가 True일 경우 카운트
            cnt += 1

print(cnt)