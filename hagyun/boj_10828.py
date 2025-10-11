stack=[]

N=int(input())

for _ in range(N):
    command=(input())
    if command.startswith('push'):
        push_str,X=command.split()
        x=int(X)
        stack.append(x)
    elif command=='pop':
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif command=='size':
        if not stack:
            print(-1)
        else:
            print(len(stack))
    elif command=='empty':
        if not stack:
            print(1)
        else:
            print(0)
    elif command=='top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
