# 유의사항
# 1. 첫번째 요소 -로 시작 가능
# 2. 재귀 반복 시, 매 분기마다 변하는 변수는 인수로 넣어줘야 함
# -> 안 하면 값이 누적됨

cnt = 0
def solution(numbers, target):
    global cnt
    
    DFS(numbers, target, 0, 0)
    
    return cnt

def DFS(numbers, target, sum, idx):
    global cnt
    operators = ['+', '-']
    
    if idx == len(numbers):
        if sum == target:
            cnt += 1
        return
    
    for oper in operators:
        if oper == '+':
            DFS(numbers, target, sum+numbers[idx], idx+1)
        else:
            DFS(numbers, target, sum-numbers[idx], idx+1)

# 틀린 답안
# def DFS(numbers, target, sum, idx):
#     global cnt
#     operators = ['+', '-']
    
#     if idx == len(numbers):
#         if sum == target:
#             cnt += 1
#         return
    
#     for oper in operators:
#         if oper == '+':
#             sum += numbers[idx]     # 여기서 더해버리면 다음 -할 때 이전에 더해진 sum에다가 뺌
#         else:
#             sum -= numbers[idx]
        
#         DFS(numbers, target, sum+numbers[idx], idx+1)
            
        