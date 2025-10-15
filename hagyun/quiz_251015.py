import pandas as pd
import numpy as np

#1
a=[
    [7,0,0,0,7],
    [0,0,0,0,0],
    [0,0,7,0,7],
    [0,0,0,0,0],
    [7,0,0,0,7]
]
dfa=pd.DataFrame(a,columns=['A','B','C','D','E'])

b=[
    [0,0,7,0,0],
    [0,0,0,0,0],
    [7,0,7,0,7],
    [0,0,0,0,0],
    [0,0,7,0,0]
]
dfb=pd.DataFrame(b,columns=['A','C','E','G','I'])

dfc=pd.merge(dfa,dfb,how='inner')
print(dfc)

print('-----')

a=[
    [7,0,0,0,7],
    [0,7,0,7,0],
    [0,0,7,0,7],
    [0,7,0,7,0],
    [7,0,0,0,7]
]
dfa=pd.DataFrame(a,columns=['A','B','C','D','E'])

b=[
    [0,0,7,0,0],
    [0,0,7,0,0],
    [7,7,7,7,7],
    [0,0,7,0,0],
    [0,0,7,0,0]
]
dfb=pd.DataFrame(b,columns=['A','C','E','G','I'])

dfc=pd.merge(dfa,dfb,how='inner')
print(dfc)


#2
start = np.identity(5)*7
goal= [
    [0,0,0,0,0,0],
    [7,0,0,0,0,0],
    [0,7,0,0,0,0],
    [0,0,7,0,0,0],
    [0,0,0,7,0,0],
    [0,0,0,0,7,0]
]

#2_1
import numpy as np

A = np.array([[7,0,0,0,0],
              [0,7,0,0,0],
              [0,0,7,0,0],
              [0,0,0,7,0],
              [0,0,0,0,7]])

# 새 배열을 하나 크게 만든 뒤, 원래 A를 아래로 복사
rows, cols = A.shape  # (5,5)
B = np.zeros((rows + 1, cols + 1), dtype=A.dtype)  
# B는 6x6 배열, 모두 0으로 초기화

# A를 B의 (1:, 0:cols) 영역에 넣기 → 한 칸 아래로 밀리는 효과
B[1:rows+1, :cols] = A

print(B)

#2_2
import numpy as np

A = np.array([[7,0,0,0,0],
              [0,7,0,0,0],
              [0,0,7,0,0],
              [0,0,0,7,0],
              [0,0,0,0,7]])

# 먼저 A에 한 열 추가 (우측에 0 열)
A2 = np.insert(A, A.shape[1], values=0, axis=1)  # 5×6 배열

# 그 다음 위쪽에 0 행 삽입
B = np.insert(A2, 0, values=np.zeros(A2.shape[1], dtype=A.dtype), axis=0)

print(B)

#2_3
import numpy as np

A = np.array([[7,0,0,0,0],
              [0,7,0,0,0],
              [0,0,7,0,0],
              [0,0,0,7,0],
              [0,0,0,0,7]])

# 우선 오른쪽에 0 열을 붙이기
zero_col = np.zeros((A.shape[0], 1), dtype=A.dtype)
A_extended = np.hstack((A, zero_col))  # 5×6

# 그 다음 위에 0 행 붙이기
zero_row = np.zeros((1, A_extended.shape[1]), dtype=A.dtype)
B = np.vstack((zero_row, A_extended))

print(B)
