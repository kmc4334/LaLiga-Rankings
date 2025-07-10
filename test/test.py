import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_iris

# numpy 테스트
arr = np.array([1, 2, 3])
print("Numpy 배열:", arr)

# pandas 테스트
data = {'이름': ['민찬', '수지'], '나이': [20, 22]}
df = pd.DataFrame(data)
print("\nPandas 데이터프레임:\n", df)

# matplotlib 테스트 (그래프 그리기)
plt.plot([1, 2, 3], [4, 5, 6])
plt.title('Test Plot')
plt.show()

# sklearn 테스트 (간단 선형회귀)
iris = load_iris()
X = iris.data[:, :1]  # 꽃받침 길이
y = iris.target
model = LinearRegression()
model.fit(X, y)
print("\nSklearn LinearRegression coef:", model.coef_)