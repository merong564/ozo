# 실수 1개를 입력받아 정수 부분과 실수 부분으로 나누어 출력한다.

# ** 여러 가지 방법들로 해결할 수 있다.

# 만약 실수 부분이 0으로 시작하지 않는다면(예를 들어 1.000009)
# scanf("%d.%d", &a, &b)도 하나의 방법이 될 수 있다.


## 답안 1. split('.') 사용 
# - 이 경우 정수값 입력은 다루지 못함

# integer_part, fractional_part = map(int, input('실수 1개를 입력하시오: ').split('.'))
# print(integer_part)
# print(fractional_part)



## 답안 2. 정규표현식 사용
# import re
# num_str = input('실수 1개를 입력하시오: ')

# pattern = re.compile(r'(\d+)[.]?(\d*)')          # () : 하나의 그룹으로 캡처 -> 괄호 안에 +, * 넣어야 함
# result = pattern.match(num_str)
# integer_part = result.group(1)
# fractional_part = result.group(2)

# print(integer_part)
# print(fractional_part)



# 답안 3. for문 사용
num_str = input('실수 1개를 입력하시오: ')

is_there_comma = False
integer_part = ''
fractional_part = ''


# s의 경우의 수
# 1. '.' 이전의 문자
# 2. '.' 그자체
# 3. '.' 이후의 문자

for s in num_str:
    if s == '.':
        is_there_comma = True

    elif is_there_comma:
        fractional_part += s

    else:
        integer_part += s

print(integer_part)
print(fractional_part)

