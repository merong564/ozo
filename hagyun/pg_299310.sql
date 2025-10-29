select
    extract(year from E.DIFFERENTIATION_DATE) as YEAR,
    (MAX_T.MAX_SIZE - E.SIZE_OF_COLONY) as YEAR_DEV,
    E.ID
from ECOLI_DATA as E
inner join (
    select
        extract(year from DIFFERENTIATION_DATE) as YEAR,
        max(SIZE_OF_COLONY) as MAX_SIZE
    from ECOLI_DATA
    group by extract(year from DIFFERENTIATION_DATE)
) as MAX_T
--서브쿼리 생성, year, max값을 가지면서 year별로 묶여 있음
on extract(year from E.DIFFERENTIATION_DATE) = MAX_T.YEAR
--서브 쿼리와 본 쿼리의 year를 기준으로 join, select는 본 쿼리의 year
order by YEAR asc, YEAR_DEV asc;