# 문제 1: 괄호 짝 검사 
# 문자열을 인수로 받아 포함된 괄호의 짝이 올바르게 사용되었는지  
# 확인하는 프로그램을 작성하시오 
# • 스택 활용 
# • 괄호의 짝이 맞으면 True 반환 
# • 괄호의 짝이 맞지 않으면 False 반환 


## 문제 풀이 포인트
# 경우의 수를 먼저 생각하고 코드 짜기

# True 반환 조건
# 1. 시작하는 괄호가 있을 경우
# 2. 끝나는 괄호가 있을 경우
# 3. 시작, 끝 괄호가 서로 같은 경우
# 4. stack에 남은 괄호가 없을 경우

# 그 외는 모두 False

def check_brakets(expression):
    stack = []
    for char in expression:
        if char in "({[":
            stack.append(char)
        
        elif char in ")}]":
            if not stack:
                return False            
            top = stack.pop()

            if (char == ')' and top != '(') or \
                (char == '}' and top != '{') or \
                (char == ']' and top != '['):
                return False 
    
    return len(stack) == 0      # True
    
print(check_brakets('pjd[ddfs2re]'))
print(check_brakets('pjdddfs2re]'))
print(check_brakets('pjd(ddfs2re]'))