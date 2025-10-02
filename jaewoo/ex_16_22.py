from collections import deque

def rotate_Deque(data):
    dq = deque(data)
    dq.rotate(-2)
    return list(dq)

print(rotate_Deque([1,2,3,4,5]))


print('-------------------------')

def rotate_Deque(data):
    n= len(data)
    k = 2 % n if n else 0
    return data [k:] + data[:k]


print(rotate_Deque([1,2,3,5,6,7,8,9]))