class CircularQueue:
    def __init__(self, capacity: int):
        assert capacity > 0 # 용량은 양수
        self.cap = capacity # 고정 용량
        self.arr = [None] * capacity # 실제 저장 배열
        self.front = 0 # 맨 앞 원소의 인덱스(꺼낼 위치)
        self.rear = 0 # 다음 삽입이 들어갈 인덱스(넣는 위치)
        self.count = 0 # 현재 원소 개수

    def is_empty(self) -> bool:
        return self.count == 0 # 원소 수가 0이면 비어 있음
    
    def is_full(self) -> bool:
        return self.count == self.cap # 원소 수가 용량과 같으면 가득
    
    def front_value(self) -> int:
        if self.is_empty(): # 비었으면 -1 반환
            return -1
        return self.arr[self.front] # 맨 앞 원소를 조회만
    
    def rear_value(self) -> int:
        if self.is_empty():
            return -1
        # rear는 다음 삽입 위치이므로 실제 마지막 원소는 rear-1 위치
        return self.arr[(self.rear -1) % self.cap]
    
    def enqueue(self, x: int) -> bool:
        if self.is_full():
            return False
        self.arr[self.rear] = x
        self.rear = (self.rear + 1) % self.cap
        self.count += 1
        return True
    
    def dequeue(self) -> int:
        if self.is_empty():
            return -1
        val = self.arr[self.front]              # front 위치의 값을 꺼내 반환용 보관
        self.arr[self.front] = None             # (선택) 지운 자리 표시(디버깅용)
        self.front = (self.front + 1) % self.cap# front 한 칸 전진(원형 회전)
        self.count -= 1                         # 원소 수 감소
        return val

    def rotate(self, k: int) -> None:
        """
        k>0: 왼쪽(앞으로) k칸 회전, k<0: 오른쪽(뒤로) |k|칸 회전
        실제 데이터를 옮기지 않고 front/rear 포인터만 조정
        """
        if self.count == 0:                     # 빈 큐는 회전 의미 없음
            return
        k %= self.count                         # 현재 들어있는 원소 수 기준으로 회전량 축소
        self.front = (self.front + k) % self.cap# 왼쪽 회전: front를 앞으로 k칸
        self.rear = (self.front + self.count) % self.cap  # rear는 front+count로 정합 유지

    def to_list(self):
        """현재 큐의 논리적 순서를 리스트로 반환(디버깅 편의)"""
        out = []
        i = self.front
        for _ in range(self.count):
            out.append(self.arr[i])
            i = (i + 1) % self.cap
        return out

    def __repr__(self):
        return (f"CQ(cap={self.cap}, front={self.front}, rear={self.rear}, "
                f"count={self.count}, data={self.to_list()})")