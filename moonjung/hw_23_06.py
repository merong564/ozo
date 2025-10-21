import json

dict = {
    "name": "홍길동",
    "age": 25,
    "city": "서울"
}

with open ('data.json', 'w') as file:
    json.dump(dict, file, indent=4, ensure_ascii=False)     # ensure_ascii=False 옵션: 한글 안깨지게 함

