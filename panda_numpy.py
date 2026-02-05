import numpy as np


A = np.array([[1, 5, 9], [4, 7, 10]])
B = np.array([[2, 5, 8], [4, 6, 10]])


v_stack = np.vstack((A, B))
h_stack = np.hstack((A, B))

print("Vertical Stack:\n", v_stack)
print("\nHorizontal Stack:\n", h_stack)


common = np.intersect1d(A, B)
print("\nCommon Elements:", common)


filtered = A[(A >= 5) & (A <= 10)]
print("\nNumbers in A between 5 and 10:", filtered)


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])

condition = (iris_2d[:, 2] > 1.5) & (iris_2d[:, 0] < 5.0)
filtered_rows = iris_2d[condition]
print("\nFiltered Iris Rows:\n", filtered_rows[:5]) 


import pandas as pd
import numpy as np


df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')


subset = df.loc[::20, ['Manufacturer', 'Model', 'Type']]
print("\nEvery 20th row (Manufacturer, Model, Type):\n", subset)


df['Min.Price'].fillna(df['Min.Price'].mean(), inplace=True)
df['Max.Price'].fillna(df['Max.Price'].mean(), inplace=True)
print("\nMissing values replaced with mean in Min.Price & Max.Price")


df2 = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
rows_gt_100 = df2[df2.sum(axis=1) > 100]
print("\nRows where row sum > 100:\n", rows_gt_100)
