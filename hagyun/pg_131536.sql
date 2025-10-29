select O.USER_ID, O.PRODUCT_ID
from ONLINE_SALE as O
group by O.USER_ID, O.PRODUCT_ID
having count(*)>1
-- count(*) : 같은 그룹 내에 있는 총 행 수, 안에 컬럼을 지정하여 null값을 빼고 셀 수 있음
order by O.USER_ID, O.PRODUCT_ID desc;

--self join을 쓴다면?
-- ON A.USER_ID = B.USER_ID AND A.PRODUCT_ID = B.PRODUCT_ID AND A.ONLINE_SALE_ID <> B.ONLINE_SALE_ID
-- <> : not equal, 즉 같은 기록은 제외하겠다는 뜻
