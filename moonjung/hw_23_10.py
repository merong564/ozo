path = r"C:\rokey\python\ch22\logfile.log"
with open(path, "w", encoding="utf-8") as file:
    file.write("2025-03-30 12:00:01 INFO 서버 시작됨\n")
    file.write("2025-03-30 12:05:12 ERROR 데이터베이스 연결 실패\n")
    file.write("2025-03-30 12:10:35 WARNING 응답 속도 저하\n")
    file.write("2025-03-30 12:15:45 ERROR 사용자 인증 실패\n")

import re
p = re.compile('^2025-03-30')

with open(path, 'r', encoding='utf-8') as file:
    result = [line.strip() for line in file if p.match(line)]

for i in result:
    print(i)
