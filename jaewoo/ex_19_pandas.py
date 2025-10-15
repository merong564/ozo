import pandas as pd                          # pandas 라이브러리를 pd 별칭으로 임포트
import numpy as np                           # numpy 라이브러리를 np 별칭으로 임포트

data = [                                      # 직원 정보를 담은 딕셔너리 리스트(샘플 데이터)
    {"emp_id":1,"name":"A","dept":"Sales","salary":4200,"hire_date":"2022-01-10","bonus":500},
    {"emp_id":2,"name":"B","dept":"Sales","salary":3900,"hire_date":"2021-11-03","bonus":None},
    {"emp_id":3,"name":"C","dept":"Eng","salary":6100,"hire_date":"2020-05-14","bonus":1000},
    {"emp_id":4,"name":"D","dept":"Eng","salary":5800,"hire_date":"2019-09-30","bonus":600},
    {"emp_id":5,"name":"E","dept":"HR","salary":3600,"hire_date":"2023-03-01","bonus":300},
    {"emp_id":6,"name":"F","dept":"HR","salary":None,"hire_date":"2022-12-15","bonus":200},
    {"emp_id":7,"name":"G","dept":"Eng","salary":7200,"hire_date":"2018-07-22","bonus":1500},
]

df = pd.DataFrame(data)                       # 리스트→DataFrame으로 변환

df["hire_date"] = pd.to_datetime(df["hire_date"])  # 문자열 날짜를 datetime 타입으로 변환
df["year"] = df["hire_date"].dt.year               # 입사 연도만 추출해 새 열 year 생성

dept_mean = df.groupby("dept")["salary"].transform("mean")  # 부서별 salary 평균을 각 행에 브로드캐스트
df["salary"] = df["salary"].fillna(dept_mean)               # salary 결측치(NaN)를 같은 부서 평균으로 대체

df["bonus"] = df["bonus"].fillna(0)                 # 보너스 결측치는 0으로 채움
df["total_comp"] = df["salary"] + df["bonus"]       # 총보상 = 급여 + 보너스

overall_mean_salary = df["salary"].mean()           # 전체 평균 급여 계산
mean_by_dept = df.groupby("dept")["salary"].mean()  # 부서별 평균 급여 계산

top2_per_dept = (                                   # 부서별 total_comp 상위 2명 추출
    df.sort_values(["dept","total_comp"], ascending=[True,False])  # 부서 오름차순, 총보상 내림차순 정렬
      .groupby("dept")                               # 부서별 그룹화
      .head(2)                                       # 각 그룹에서 상위 2행
)

pivot_cnt = pd.pivot_table(                          # 피벗테이블 생성: 연도×부서별 인원 수
    df, index="year", columns="dept", values="emp_id",
    aggfunc="count", fill_value=0
)

dept_mean2 = df.groupby("dept")["salary"].transform("mean")  # z-score용 부서별 평균
dept_std2  = df.groupby("dept")["salary"].transform("std")   # z-score용 부서별 표준편차
df["salary_z"] = (df["salary"] - dept_mean2) / dept_std2     # (급여-부서평균)/부서표준편차

print("=== 전체 평균 급여 ===")                 # 결과 출력 시작
print(overall_mean_salary)                      # 전체 평균 급여 값 출력
print("\n=== 부서별 평균 급여 ===")            # 구분 텍스트 출력
print(mean_by_dept)                             # 부서별 평균 급여 시리즈 출력
print("\n=== 부서별 상위 2명(총보상) ===")     # 구분 텍스트 출력
print(top2_per_dept[["dept","name","total_comp"]])  # 부서·이름·총보상만 표시
print("\n=== 연도×부서 직원 수 ===")            # 구분 텍스트 출력
print(pivot_cnt)                                # 피벗 테이블 출력
print("\n=== z-score 미리보기 ===")            # 구분 텍스트 출력
print(df[["dept","name","salary","salary_z"]])  # 부서, 이름, 급여, z-score 컬럼만 출력
    