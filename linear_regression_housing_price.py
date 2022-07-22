import numpy as np
import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt

df = pd.read_csv("Housing_price.csv")

"""
df.head()
x = df['Area'].values
x_reshape = x.reshape(len(x), 1)

print(x_reshape)
plt.scatter(df.Area, df.Price, color='red', marker='+')
plt.xlabel("Area(sq ft )")
plt.ylabel("Price(Tk)")
plt.show()

reg = linear_model.LinearRegression()

reg.fit(x_reshape, df.Price)

print(reg.predict([[3100]]))
print(reg.predict([[3200]]))


"""

plt.scatter(df.Area, df.Price, color='red', marker='+')
plt.xlabel("Area(sq ft )")
plt.ylabel("Price(Tk)")
plt.show()

reg = linear_model.LinearRegression()

reg.fit(df[['Area']], df.Price)

print(reg.predict([[3100]]))
print(reg.predict([[3200]]))