# some=(input())
# a,b=some.split('.')
# print(a)
# print(b)

# 위 코드는 단순 정수가 왔을 때 ValueError

print('-----')
import re
# \d+[.]\d+
p=re.compile(r'\d+')
somef=(input())
result=p.findall(somef)
if len(result)==1:
    print(result[0])
if len(result)==2:
    print(result[0])
    print(result[1])