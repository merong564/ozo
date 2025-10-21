select D.ID, D.EMAIL, D.FIRST_NAME, D.LAST_NAME
from DEVELOPER_INFOS as D
where D.SKILL_1='Python' or D.SKILL_2='Python' or D.SKILL_3='Python'
order by D.ID asc;