# 답안 1. 일일이 입력
# graph = [[0, 0, 1, 0, 1],
#          [1, 0, 1, 0, 0],
#          [0, 0, 1, 1, 0],
#          [0, 1, 0, 0, 0],
#          [0, 0, 0, 1, 1]]

## 아래와 같이 입력이 주어질 경우
# 00101
# 10100
# 00110
# 01000
# 00011

# 답안 2. for문으로 각 행을 리스트로 만들기
graph = []
for _ in range(5):                          # 한 줄씩 입력받기
    row = [int(s) for s in input()]         # for문: 문자열의 글자마다 int 처리
    graph.append(row)                       # 만들어진 row 리스트를 graph에 추가

print(graph)


# 답안 2. map함수로 각 행을 리스트로 만들기
graph = []
for _ in range(5):                          # 한 줄씩 입력받기
    row = list(map(int, input()))           # map 함수: 입력 받은 문자열의 문자마다 int 처리
    graph.append(row)                       # 만들어진 row 리스트를 graph에 추가

print(graph)


## 아래와 같이 입력이 주어질 경우 (숫자 사이에 공백 존재)
# 0 0 1 0 1
# 1 0 1 0 0
# 0 0 1 1 0
# 0 1 0 0 0
# 0 0 0 1 1

# 답안 3. input().split() 이용
graph = []
for _ in range(5):
    row = list(map(int, input().split()))
    graph.append(row)

print(graph)

