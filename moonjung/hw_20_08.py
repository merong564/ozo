from sklearn.linear_model import LogisticRegression

X = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
y = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]

clf = LogisticRegression()
clf.fit(X, y)

pre = clf.predict([[4.5], [6.5]])
print(f'예측 결과: {pre}')