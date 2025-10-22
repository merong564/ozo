-- 프로그래머스 답안

SELECT ID, EMAIL, FIRST_NAME, LAST_NAME
FROM DEVELOPER_INFOS
WHERE SKILL_1 = 'Python' OR SKILL_2 = 'Python' OR SKILL_3 = 'Python'
ORDER BY ID;


-- MySQL에 직접 구현해본 코드

CREATE ozo;

USE ozo;

CREATE TABLE DEVELOP_INFOS(
ID VARCHAR(50) PRIMARY KEY,
FIRST_NAME VARCHAR(50),
LAST_NAME VARCHAR(50),
EMAIL VARCHAR(50) UNIQUE NOT NULL,
SKILL_1 VARCHAR(50),
SKILL_2 VARCHAR(50),
SKILL_3 VARCHAR(50)
);

INSERT INTO DEVELOPER_INFOS
VALUES ('D165', 'Jerami', 'Edwards', 'jerami_edwards@grepp.co', 'Java', 'JavaScript', 'Python');

INSERT INTO DEVELOPER_INFOS (ID, FIRST_NAME, LAST_NAME, EMAIL, SKILL_1)
VALUES('D161', 'Carsen', 'Garza', 'carsen_garza@grepp.co','React');

INSERT INTO DEVELOPER_INFOS (ID, FIRST_NAME, LAST_NAME, EMAIL, SKILL_1)
VALUES('D164', 'Kelly', 'Grant', 'kellly_grant@grepp.co','C#');

INSERT INTO DEVELOPER_INFOS (ID, FIRST_NAME, LAST_NAME, EMAIL, SKILL_1)
VALUES ('D163', 'Luka', 'Cory', 'luka_cory@grepp.co', 'Node.js');

INSERT INTO DEVELOPER_INFOS
VALUES('D162', 'Cade', 'Cunningham', 'cade_cunningham@grepp.co', 'Vue', 'C++', 'Python');


SELECT ID, EMAIL, FIRST_NAME, LAST_NAME
FROM DEVELOPER_INFOS
WHERE SKILL_1 = 'Python' OR SKILL_2 = 'Python' OR SKILL_3 = 'Python'
ORDER BY ID;


-- PRIMARY KEY 여러개 설정 시 에러남. PRIMARY KEY는 TABLE 당 하나만 존재함

-- 여러 개의 조건 사용할 경우 AND OR NOT 사용
-- IN 문법 쓰면 OR 여러개 필요 없다고 함
-- https://codingapple.com/unit/sql-where-and-or-in/