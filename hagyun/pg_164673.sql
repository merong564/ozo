-- create table sub as
-- select title, board_id
-- from used_goods_board
-- where year(created_date)=2022 and month(created_date)=10;

select S.TITLE,S.BOARD_ID, R.REPLY_ID,R.WRITER_ID,R.CONTENTS,DATE(R.CREATED_DATE) AS CREATED_DATE
from used_goods_board as S
inner join used_goods_reply as R
on S.BOARD_ID=R.BOARD_ID
where year(S.CREATED_DATE)=2022 and month(S.CREATED_DATE)=10
order by R.CREATED_DATE asc, S.CREATED_DATE asc;


-- gpt ver 1, date를 to_char로 문자열 형태로 만드는 구조
-- 프로그래머스가 to_char를 허용 안함
-- SELECT 
--     B.TITLE,
--     B.BOARD_ID,
--     R.REPLY_ID,
--     R.WRITER_ID,
--     R.CONTENTS,
--     TO_CHAR(R.CREATED_DATE, 'YYYY-MM-DD') AS CREATED_DATE
-- FROM USED_GOODS_BOARD B
-- JOIN USED_GOODS_REPLY R ON B.BOARD_ID = R.BOARD_ID
-- WHERE TO_CHAR(B.CREATED_DATE, 'YYYY-MM') = '2022-10'
-- ORDER BY R.CREATED_DATE ASC, B.TITLE ASC;

-- gpt ver 2, date_format으로 문자열로 바꾸는 형태
-- SELECT 
--     B.TITLE,
--     B.BOARD_ID,
--     R.REPLY_ID,
--     R.WRITER_ID,
--     R.CONTENTS,
--     DATE_FORMAT(R.CREATED_DATE, '%Y-%m-%d') AS CREATED_DATE
-- FROM USED_GOODS_BOARD B
-- JOIN USED_GOODS_REPLY R ON B.BOARD_ID = R.BOARD_ID
-- WHERE DATE_FORMAT(B.CREATED_DATE, '%Y-%m') = '2022-10'
-- ORDER BY R.CREATED_DATE ASC, B.TITLE ASC;

-- join의 디폴트는 inner join