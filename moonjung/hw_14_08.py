# 8. 주어진 문자열에서 "Python"이 포함된 문장만 리스트로 반환하세요.
# text = "I love Python. Java is also popular. Python is great for AI."

## 문제 풀이 포인트
# Python 앞뒤로 문자가 없을 수도, 여러 개 있을 수도 있다. 
# 단, .을 제외해야 함

import re
text = "I love Python. Java is also popular. Python is great for AI."


# 답안 1
# pattern = re.compile('[^.]*Python[^.]*[.]')

# 답안 2
# pattern = re.compile(r'[^.]*Python[^.]*\.')           # 특수문자 .을 의미 없는 문자로 쓰고 싶을 경우 \.로 escape 해야함
                                                        # r'' -> raw string. \s, \w 쓸 때 \\s, \\w 안 써도 같은 효과 내도록 함 

# 답안 3
pattern = re.compile(r'[\w\s]*Python[\s\w]*\.')

result = [s.strip() for s in pattern.findall(text)]
print(result)



## 시도한 패턴 (다 틀림) 
# -> + 를 사용했기 때문. Python 앞뒤로 r'[\s\w]'이 있을 수도, 없을 수도 있음
# -> * 사용 필요

# pattern = re.compile('[A-Z][^.]+Python[^.]+[.]')            # 이러면 Java도 추출됨
# pattern = re.compile('[^.]+Python[^.]?[.]')                 # I love Python.
# pattern = re.compile('Python[^.]+[.]')                      # Python is great for AI.


## 참고
# '^문자' == 문자로 시작
# '[^문자]' == not 문자
# '\w' == '[0-9a-zA-Z_]'

# '.' == \n을 제외한 모든 문자
# '[.]' == 문자 .
# '[^.]' == 문자 .을 제외한 모든 문자 (\s까지 포함됨)