def make_map(y:int,x:int,data:str)->list:
# data가 문자열로 주어져야 함
    data_list=data.split()
    result=[]
    temp=[]
    for dt in data_list:
        if len(temp)==x:
            result.append(temp)
            temp=[]
        if len(result)==y:
            break
        temp.append(dt)
    return result