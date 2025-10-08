# push할 때 x 처리 유의하기
# 명령 처리 시 if~elif 사용할 경우 시간 초과
# strip()으로 \n 제거하기

# 시간 초과 방지
# 1. sys.stdin.readline으로 입력받기
# 2. deque 사용 (pop(0) 사용하지 않기)
# 3. if~elif 사용 (if문만 사용하지 않기)


# 답안 1
from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

queue = deque()

for _ in range(n):
    command = input().strip()
    
    if 'push' in command:
        push, x = command.split()
        queue.append(int(x))
    
    elif command == 'pop':
        if len(queue) == 0:
            print(-1)
            continue
        print(queue.popleft())

    elif command == 'size':
        print(len(queue))

    elif command == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    
    elif command == 'front':
        if len(queue) == 0:
            print(-1)
            continue
        print(queue[0])
    
    elif command == 'back':
        if len(queue) == 0:
            print(-1)
            continue
        print(queue[-1])

# # 답안 2. class 사용
# from collections import deque
# import sys

# class MyQueue:
#     def __init__(self):
#         self.queue = deque()

#     def push(self, x):
#         self.queue.append(x)

#     def pop(self):
#         if len(self.queue) == 0:
#             print(-1)
#             return
#         print(self.queue.popleft())

#     def size(self):
#         print(len(self.queue))
#         return
    
#     def empty(self):
#         if len(self.queue) == 0:
#             print(1)
#             return
#         print(0)
    
#     def front(self):
#         if len(self.queue) == 0:
#             print(-1)
#             return
#         print(self.queue[0])
    
#     def back(self):
#         if len(self.queue) == 0:
#             print(-1)
#             return
#         print(self.queue[-1])

# input = sys.stdin.readline
# n = int(input())
# myqueue = MyQueue()

# for _ in range(n):
#     command = input().strip()
  
#     if 'push' in command:
#         push, x = command.split()
#         myqueue.push(int(x))

#     elif command == 'pop':
#         myqueue.pop()

#     elif command == 'size':
#         myqueue.size()

#     elif command == 'empty':
#         myqueue.empty()

#     elif command == 'front':
#         myqueue.front()

#     elif command == 'back':
#         myqueue.back()


# # 답안 3. 디폴트로 split하여 arr 만들기
# import sys
# input = sys.stdin.readline

# n = int(input())

# stack = []

# for i in range(n):
#     arr = list(input().strip().split())

#     if len(arr) == 2 and arr[0] == 'push':
#         stack.append(arr[1])

#     elif arr[0] == 'pop':
#         if len(stack) == 0:
#             print(-1)
#         else:
#             print(stack.pop(0))
    
#     elif arr[0] == 'size':
#         print(len(stack))

#     elif arr[0] == 'empty':
#         if len(stack) == 0:
#             print(1)
#         else:
#             print(0)
    
#     elif arr[0] == 'front':
#         if len(stack) == 0:
#             print(-1)
#         else:
#             print(stack[0])
        
#     elif arr[0] == 'back':
#         if len(stack) == 0:
#             print(-1)
#         else:
#             print(stack[-1])




# 시간 초과 뜨는 답안 -> sys.stdin.readline 안 쓸 경우
# n = int(input())

# queue = list()

# for _ in range(n):
#     command = input().strip()
    
#     if 'push' in command:
#         push, x = command.split()
#         queue.append(int(x))
    
#     if command == 'pop':
#         if len(queue) == 0:
#             print(-1)
#             continue
#         print(queue.pop(0))

#     if command == 'size':
#         print(len(queue))

#     if command == 'empty':
#         if len(queue) == 0:
#             print(1)
#         else:
#             print(0)
    
#     if command == 'front':
#         if len(queue) == 0:
#             print(-1)
#             continue
#         print(queue[0])
    
#     if command == 'back':
#         if len(queue) == 0:
#             print(-1)
#             continue
#         print(queue[-1])