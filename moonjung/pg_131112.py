# 프로그래머스 답안
'''
SELECT FACTORY_ID, FACTORY_NAME, ADDRESS
FROM FOOD_FACTORY
WHERE LEFT(ADDRESS, 3) = '강원도'
ORDER BY FACTORY_ID
'''

# 문자열 원하는 대로 자르기: LEFT, RIGHT, MID
# https://jaehwaseo.tistory.com/12

# LEFT(ADDRESS, 3)
# MID(ADDRESS, 2, 4)      # 컬럼, 시작 인덱스, 가져올 개수

# SUBSTR, SUBSTRING
# SUBSTR(컬럼, 시작 인덱스, 가져올 개수)

