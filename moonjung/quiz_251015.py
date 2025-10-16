import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1
data = np.array([
    ['Inception', 8.8, 2010],
    ['The Dark Knight', 9.0, 2008],
    ['Interstellar', 8.6, 2014]
])

df = pd.DataFrame(data, columns = ['Title', 'Rating', 'Year'])
df['Rating'] = df['Rating'].astype(float)

print(df)

# 2
data2 = {
 'Title': ['Inception', 'The Dark Knight', 'Interstellar'],
 'Run Time': [148, 152, 169]
}

df2 = pd.DataFrame(data2)
merged = pd.merge(df, df2)
print(merged)

# 3
data3 = [
 ['The Matrix', 8.7, 1999],
 ['Titanic', 7.8, 1997]
]

df3 = pd.DataFrame(data3, columns=['Title', 'Rating', 'Year'])
concated = pd.concat([merged, df3])
print(concated)

# 4
meanVal = concated['Run Time'].mean()
concated['Run Time'] = concated['Run Time'].fillna(meanVal)
print(concated)

# 5
plt.scatter(concated['Rating'], concated['Run Time'])
plt.title('Correlation Between Movie Rating and Run Time')
plt.xlabel('Rating')
plt.ylabel('Run Time')
plt.show()