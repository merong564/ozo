## 원형 큐: 배열의 시작과 끝을 연결
# 마지막 인덱스 다음은 다시 0번 인덱스로 돌아감
# 배열의 한 칸(rear)을 항상 비워 두어, 빈 상태와 꽉 찬 상태를 구분
# queue = list() -> 실제 데이터를 저장하는 배열
# front -> 첫 번째 요소 인덱스 (삭제 위치)
# rear -> 마지막 요소 인덱스(삽입 위치) 바로 다음 위치
# size -> 큐 전체 크기

# front, rear는 위치가 바뀌면서 이동함. front, rear 위치에 맞게 enqueue, dequeue됨

class CirQueue:
    def __init__(self, size):
        self.cirqueue = [None] * size
        self.size = size
        self.front = 0
        self.rear = 0

    def enqueue(self, x):
        if self.is_full():
            return
        self.cirqueue[self.rear] = x     
        self.rear = (self.rear+1)%self.size

    def dequeue(self):
        if self.is_empty():
            return -1
        first = self.cirqueue[self.front]
        self.front = (self.front+1)%self.size
        return first
    
    def peek(self):
        if self.is_empty():
            return -1
        return self.cirqueue[self.front]
    
    def is_empty(self):
        if self.front == self.rear:
            return True
        return False
    
    def is_full(self):
        if (self.rear + 1) % self.size == self.front:
            return True
        return False


## (참고) 회전 큐 -> deque 이용
from collections import deque

def rotate_queue(data, k):
    dq = deque(data)

    # 방법 1. 왼쪽으로 k만큼 회전
    # dq.rotate(-k)

    # 방법 2. 가장 왼쪽 값을 오른쪽에 붙이기, k번 반복
    for _ in range(k):
        dq.append(dq.popleft())

    return dq


queue = [1, 2, 3, 4, 5]
k = 2
print(rotate_queue(queue, k))