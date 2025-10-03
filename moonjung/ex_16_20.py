# 괄호 열린 순서대로 닫혀야 함
# -> stack 이용하면 유리함

# ## 문제 풀이 포인트
# # 경우의 수를 먼저 생각하고 코드 짜기

# # True 반환 조건
# # 1. 시작하는 괄호가 있을 경우
# # 2. 끝나는 괄호가 있을 경우
# # 3. 시작, 끝 괄호가 서로 같은 경우
# # 4. stack에 남은 괄호가 없을 경우

# # 그 외는 모두 False


## 답안 1. 강사님 코드
# def check_brakets(expression):
#     stack = []
#     for char in expression:
#         if char in "({[":
#             stack.append(char)
        
#         elif char in ")}]":
#             if not stack:
#                 return False            
#             top = stack.pop()

#             if (char == ')' and top != '(') or \
#                 (char == '}' and top != '{') or \
#                 (char == ']' and top != '['):
#                 return False 
    
#     return len(stack) == 0      # True
    
# print(check_brakets('pjd[ddfs2re]'))
# print(check_brakets('pjdddfs2re]'))
# print(check_brakets('pjd(ddfs2re]'))




# 답안 2. continue 이용
def check_brakets(text):
    stack = []

    for char in text:
        # 시작 괄호일 경우 stack에 넣기
        if char in '([{':
            stack.append(char)
        
        # 끝 괄호일 경우 
        elif char in ')]}':
            # stack이 비어 있을 경우 False 반환
            if not stack:
                return False
            
            top  = stack.pop()         # stack 끝에 있는 괄호(top) 확인

            # 괄호 짝이 맞을 경우, continue
            if (char == ')' and top == '(') or \
            (char == ']' and top == '[') or \
            (char == '}' and top == '{'):
                continue
            
            # 괄호 짝이 맞지 않는 경우, False 반환
            return False

    # stack이 비어 있다면 True 반환
    if not stack:
        return True


text = input()
result = check_brakets(text)
print(result)