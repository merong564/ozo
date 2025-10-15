## 후위 표기법 -> 후입선출, stack 사용
# 1. 숫자를 만날 경우 stack에 넣음
# 2. 연산자를 만날 때마다 stack에 넣어놨던 값을 pop하여 연산 
# 3. 연산 결과를 stack에 append

## 유의사항
# 1. 복수 연산자까지 구현해야 함
# 2. stack의 pop 순서 유의할 것
# stack = [1, 2]
# 위 스택에서 pop한 순서에 따라 1-2, 2-1 두가지로 연산 결과가 달라짐
# 3. 잘못된 가정은 금지
# ex) 연산자 앞에 무조건 2개의 피연산자가 있다는 가정


# input 예시
# 345+* -> 27
# 34-   -> -1
# 34+56+*   -> 77

expression = input()
stack = list()

for char in expression:

    # 연산자일 경우 stack에서 값을 빼와 연산
    if char in '+-*/':
        b = stack.pop()         # 유의! 먼저 꺼낸 게 b가 되어야 함. 안그러면 연산 순서 바뀜
        a = stack.pop()
        
        if char == '+':
            result = a+b

        elif char == '-':
            result = a-b

        elif char == '*':
            result = a*b

        elif char == '/':
            result = a/b

        stack.append(result)
           
    # 숫자일 경우 stack에 넣기
    else:
        stack.append(int(char))

print(stack[0])


# 틀린 답안: 연산자를 처음 볼 때만 stack에서 두 값을 꺼내고, 이후부터는 하나만 꺼냄
# -> 아래와 같은 경우는 처리하지 못함
# 34+56+*   -> 77

# expression = input()
# stack = list()
# First = True            # 처음으로 연산자를 만났을 때 플래그

# for char in expression:

#     # 연산자일 경우 stack에서 값을 빼와 연산
#     if char in '+-*/':
#         # 처음 연산자를 만났을 경우, stack에서 값을 두개 빼와서 연산
#         if First:         
#             a = stack.pop()
#             b = stack.pop()
            
#             if char == '+':
#                 result = a+b

#             elif char == '-':
#                 result = a-b

#             elif char == '*':
#                 result = a*b

#             elif char == '/':
#                 result = a/b
            
#             First = False           # 플래그 False 처리

#         # 연산자를 두번째 이상으로 만났을 경우 stack에서 값 하나만 빼옴
#         else:
#             a = stack.pop()

#             if char == '+':
#                 result += a

#             elif char == '-':
#                 result -= a

#             elif char == '*':
#                 result *= a

#             elif char == '/':
#                 result /= a

#     # 숫자일 경우 stack에 넣기
#     else:
#         stack.append(int(char))

# print(result)