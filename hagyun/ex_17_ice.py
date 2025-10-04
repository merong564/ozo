# N x M 크기의 얼음 틀에서 물을 넣는 홈은 0, 칸막이는 1
# 상하좌우로 0이 붙어있으면 연결된 것으로 간주, 총 갯수는 1개
# 2차원 그래프 데이터로 총 얼음 개수를 측정하는 프로그램

graph_ex=[
    [0,0,1,1,0],
    [0,0,0,1,1],
    [1,1,1,1,1],
    [0,0,0,0,0]
]

# checked는 뭘 지웠는지 확인하는 용도, 결과엔 필요 없음
def count_ice(graph):
    N=len(graph)
    M=len(graph[0])
    count=[]
    checked=[]
    for n in range(N):
        for m in range(M):
            if graph[n][m]==0:
                count.append([n,m])
# 0인 부분을 다 count에 넣어서
    count_copy=tuple(count)
    for axis in count_copy:
        if [axis[0]+1, axis[1]] in count or [axis[0],axis[1]+1] in count:
            checked.append(axis)
            count.remove(axis)
# 인접한 좌표를 가진 count 요소를 하나씩 check하며 빼냄
    result=len(count)
    checked.extend(count)        
    print(checked)
# count 에 남은 숫자 반환
    return result

print(count_ice(graph_ex))