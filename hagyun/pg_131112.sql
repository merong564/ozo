select F.FACTORY_ID, F.FACTORY_NAME, F.ADDRESS
from FOOD_FACTORY as F
where F.ADDRESS like '강원도%'
order by F.FACTORY_ID asc;