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