def find_target_plusminus(numbers,target):
    num=0
    # 2진수의 바탕이 될 수
    checked=[]
    # checked 는 경로 확인용, 결과에는 불필요
    count=0
    # target 도달 경로 개수
    while True:
        num_sum=0
        # +-계산결과
        num_path_str=f'{num:0{len(numbers)}b}'
        # 2진수 표현법 중 f-string 방식, format() 함수 방식도 거의 비슷
        # 앞에 0이 없으면 자릿수는 남지만 공백처리됨
        # bin(num)[2:].zfill(length)도 가능. '0b10101'같은 식이라 앞의 2자리를 슬라이스
        num_path=list(num_path_str)
        for i in range(len(num_path)):
            if num_path[i]=='1':
                num_sum+=numbers[i]
            else:
                num_sum-=numbers[i]
        if num_sum==target:
            checked.append(num_path)
            count+=1
        if '0' not in num_path:
            break
        num+=1
    print(checked)
    return count

numbers1=[1,1,1,1,1]
target1=3
print(find_target_plusminus(numbers1,target1))

numbers2=[4,1,2,1]
target2=4
print(find_target_plusminus(numbers2,target2))