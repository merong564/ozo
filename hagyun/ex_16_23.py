from collections import deque

class Rotating_Queue(deque):
    def __init__(self,iterable=None,number=100):
        if iterable==None:
            iterable=[]
        super().__init__(iterable)
        self.motive=deque(list(range(number)))
    def rotating(self,moving:int):
        if moving>0:
            for _ in range(moving):
                temp=self.pop()
                self.motive.appendleft(temp)
                temp2=self.motive.pop()
                self.appendleft(temp2)
        elif moving<0:
            for _ in range(-moving):
                temp=self.popleft()
                self.motive.append(temp)
                temp2=self.motive.popleft()
                self.append(temp2)

ex=Rotating_Queue([1,2,3,4,5])
ex.rotating(13)
print(ex)
print(ex.motive)
ex.rotating(-16)
print(ex)
print(ex.motive)

# 밑은 수업시간 내용
def rotate_queue(queue,k):
    dq= deque(queue)
    for _ in range(k):
        dq.append(dq.popleft())
    return list(dq)

queue=[1,2,3,4,5]
k=2
print(rotate_queue(queue,k))