def reverse_calculate(express:str)->float:
    ex_list=express.split(' ')
    stack=[]
    for ex in ex_list:
        if ex in '+-*/':
            b=stack.pop()
            a=stack.pop()
            if ex=='+':
                stack.append(a+b)
            if ex=='-':
                stack.append(a-b)
            if ex=='*':
                stack.append(a*b)
            if ex=='/':
                stack.append(a/b)
        else:
            stack.append(float(ex))
    return stack[0]

print(reverse_calculate("3 4 + 2 * 7 /"))  # ((3+4)*2)/7 = 2.0
print(reverse_calculate("5 1 2 + 4 * + 3 -"))  # 5 + ((1+2)*4) - 3 = 14.0
