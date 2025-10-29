select JI.ITEM_ID, JI.ITEM_NAME, JI.RARITY
from ITEM_TREE as IT
inner join ITEM_INFO as II
on IT.PARENT_ITEM_ID = II.ITEM_ID
inner join ITEM_INFO as JI
on IT.ITEM_ID = JI.ITEM_ID
where II.RARITY = 'RARE'
order by JI.ITEM_ID desc;