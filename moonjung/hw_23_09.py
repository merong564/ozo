import matplotlib.pyplot as plt

fruits = ['Apple', 'Banana', 'Strawberry', 'Blueberry', 'Grape']
sales = [240, 180, 150, 120, 100]

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.bar(fruits, sales, color='pink')
plt.title('과일별 판매량')
plt.xlabel('과일 종류')
plt.ylabel('판매량')
plt.show()