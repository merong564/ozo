ex='''
1 1 1 1 1 1 1 1 1 1
1 0 0 1 0 0 0 0 0 1
1 0 0 1 1 1 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 1 0 1 0 1
1 0 0 0 0 1 2 1 0 1
1 0 0 0 0 1 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1
'''

map_data=[list(map(int, line.split())) for line in ex.strip().split('\n')]
# map(함수, 이터러블) : line.split() 된 ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1'] 리스트의 각 요소에 int 적용
# list(map(함수,이터러블)) : map type 객체를 다시 list로 변경
# ex.strip().split('\n') : 문자열 제일 앞뒤의 공백이나 줄바꿈을 없애고, 줄바꿈 단위로 split하여 각 줄을 요소로 하는 리스트로 저장
# [... for line in ...] : 위 리스트의 요소(각 줄)마다 list(map(함수,이터러블))를 반복하여 [] -> 리스트에 넣는 반복 컴프리헨션


x=2; y=2
visited=[]
node=(x-1,y-1)
while True:
    visited.append((x,y))
    if map_data[y-1][x-1]==2:
        map_data[y-1][x-1]=9
        break
    if map_data[y-1][x]==0 or map_data[y-1][x]==2:
        node=(x+1,y)
    elif map_data[y][x-1]==0 or map_data[y][x-1]==2:
        node=(x,y+1)
    else:
        break
    map_data[y-1][x-1]=9
    x,y=node

for i in map_data:
    print(i)
print(visited)