from collections import deque

def rotate_queue(data, k):
    dq = deque(data)

    # 방법 1. 왼쪽으로 k만큼 회전 (rotate 메서드)
    dq.rotate(-k)               # !! 유의 !! 음수 처리해야 덱의 앞부분이 뒤로 감
    # dq.rotate(k)              # 인수가 양수일 경우, 덱의 끝에서부터 회전됨

    # 방법 2. 가장 왼쪽 값을 오른쪽에 붙이기, k번 반복 (popleft, append 메서드)
    # for _ in range(k):
    #     dq.append(dq.popleft())

    return dq

print(rotate_queue([1, 2, 3, 4, 5], 2))
