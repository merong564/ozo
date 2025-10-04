def solution(maps):    
    stack=[]
    visited=[]
    Y=len(maps)
    X=len(maps[0])
    goal=((X-1,Y-1))
    stack.append((0,0))
    answer=0
# answer는 탐색 길이, level 대용으로도 사용함
    b=1
# b는 breadth, 다음 level에 탐색할 노드 수
    check=1
# check는 level이 바뀔 시 b값을 받아 노드를 탐색할 때마다 하나씩 차감, 다 떨어지면 다음 level로 진입함을 인지시킴
    while stack:
        node=stack.pop(0)
        x,y=node
        count=0
        if node not in visited:
            visited.append(node)
        if x+1<X and maps[y][x+1]==1 and (x+1,y) not in visited:
            stack.append((x+1,y))
            count+=1
        if y+1<Y and maps[y+1][x]==1 and (x,y+1) not in visited:
            stack.append((x,y+1))
            count+=1
        if x-1>=0 and maps[y][x-1]==1 and (x-1,y) not in visited:
            stack.append((x-1,y))
            count+=1
        if y-1>=0 and maps[y-1][x]==1 and (x,y-1) not in visited:
            stack.append((x,y-1))
            count+=1
        check-=1
        if check==0:
            answer+=1
            check=b
            b=0
        b+=count
        if goal in visited:
            break
    if goal not in visited:
        answer=-1
    return answer

a=[[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]
print(solution(a))

b=[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
print(solution(b))