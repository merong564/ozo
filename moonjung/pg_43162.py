cnt = 0

def solution(n, computers):
    global cnt
    visited = [False]*n

    for i in range(n):
        if not visited[i]:
            DFS(i, computers, visited)
            cnt += 1
        
    return cnt

def DFS(start_row, computers, visited):
    visited[start_row] = True
    
    for col in range(len(computers[start_row])): 
        if computers[start_row][col] == 1 and not visited[col]:
            DFS(col, computers, visited)         # 연결된 컴퓨터가 있으면 DFS로 방문

        
## 틀린 답안: cnt 증가시키는 위치가 잘못됨. 
# 네트워크가 연결될 때마다 증가되어야 하나, 아래 코드는 DFS가 실행될 때마다 증가함
# cnt = 0
# def solution(n, computers):
#     global cnt
    
#     for i in range(n):
#         DFS(i, computers)
        
#     return cnt

# def DFS(start_row, computers):
#     global cnt
#     row = start_row   
    
#     for col in range(len(computers[row])): 
#         print(f'[{row}][{col}]')
#         # 이미 방문했으면 패스
#         if computers[row][col] == 2:
#             continue

#         # 대각 성분일 경우 방문처리
#         elif row == col:
#             computers[row][col] = 2

#         # 현재 row에서 연결되어있으면 col을 stack에 추가, 방문처리
#         elif computers[row][col] == 1:
#             computers[row][col] = 2 
#             print(f'DFS 실행')
#             DFS(col, computers)
#             cnt+=1
#             print(f'카운트, {cnt}')
            
        