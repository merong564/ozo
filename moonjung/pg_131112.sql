-- 프로그래머스 
-- 답안 1
SELECT FACTORY_ID, FACTORY_NAME, ADDRESS
FROM FOOD_FACTORY
WHERE LEFT(ADDRESS, 3) = '강원도'
ORDER BY FACTORY_ID;

-- 답안 2
select FACTORY_ID, FACTORY_NAME, ADDRESS
from FOOD_FACTORY
where ADDRESS like '강원도%';


-- 문자열 원하는 대로 자르기: LEFT, RIGHT, MID
-- https://jaehwaseo.tistory.com/12

-- LEFT(ADDRESS, 3)
-- MID(ADDRESS, 2, 4)      # 컬럼, 시작 인덱스, 가져올 개수

-- SUBSTR, SUBSTRING
-- SUBSTR(컬럼, 시작 인덱스, 가져올 개수)


-- LIKE 구문
-- WHERE F.ADDRESS LIKE '강원도%'

