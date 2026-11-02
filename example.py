# house price predict:

import pandas as pd
import numpy as np
from sklearn import linear_model
df = pd.read_csv(r'C:\Users\Dell\OneDrive\Documents\example1.csv')
reg = linear_model.LinearRegression()
reg.fit(df[['area','bedrooms','age']],df.price)
coeeficent = reg.coef_
print(coeeficent)
intercept = reg.intercept_
print(intercept)
predict = reg.predict([[3000,4,15]])
print(predict)