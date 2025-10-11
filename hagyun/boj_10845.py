queue=[]

N=int(input())

for _ in range(N):
    command=input().strip()
    if command.startswith('push'):
        push_str,X=command.split()
        x=int(X)
        queue.append(x)
    elif command=='pop':
        if not queue:
            print(-1)
        else:
            print(queue.pop(0))
    elif command=='size':
        print(len(queue))
    elif command=='empty':
        if not queue:
            print(1)
        else:
            print(0)
        # == print(1 if not queue else 0)
    elif command=='front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif command=='back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])