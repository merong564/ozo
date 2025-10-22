-- 프로그래머스 답안

SELECT CONCAT(FORMAT(MAX(LENGTH), 2), 'cm') AS MAX_LENGTH
FROM FISH_INFO



-- 1. MAX으로 컬럼 중에서 최댓값 찾기

-- 2. FORMAT으로 소수점 자리수 나타내기

-- 3. CONCAT 으로 문자열 붙이기

-- 4. AS MAX_LENGTH 로 컬럼명 설정