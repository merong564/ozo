select USER_ID, PRODUCT_ID
from ONLINE_SALE
group by USER_ID, PRODUCT_ID    -- 테이블의 행들을 특정 컬럼 기준으로 묶어서 가져옴
having count(PRODUCT_ID) > 1    -- group by로 묶인 행들에 조건 적용
order by USER_ID, PRODUCT_ID desc;