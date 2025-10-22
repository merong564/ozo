-- 프로그래머스 답안

SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE NOT INTAKE_CONDITION = 'Aged'
ORDER BY ANIMAL_ID


-- 조건에서 Not 구문 예시

SELECT *
FROM employees
WHERE department = 'Sales'
  AND NOT (salary > 5000)
  AND active = 1;


-- 괄호 필수는 아니나, 사용하여 우선순위를 명확히 하는게 좋음

SELECT *
FROM products
WHERE (NOT category = 'Electronics')
  OR price < 100;
