import numpy as np
import matplotlib.pyplot as plt
#from sklearn.linear_model import linear_model
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
import pandas as pd

# DATA SET UP
data = pd.read_csv('OWCoronaCasesTest.csv' , sep = ',')
data = data[['ID','World']]
print(data.head())

x = np.array(data['ID']).reshape(-1,1)
y = np.array(data['World']).reshape(-1,1)
plt.plot(y,'-b')

poly = PolynomialFeatures(degree=3)
x = poly.fit_transform(x)
#print(x)

#TRAINING DATA
model = linear_model.LinearRegression()
model.fit(x,y)
accuracy = model.score(x,y)
print('Accuracy:',round(accuracy*100,3),'%')

f = model.predict(x)
plt.plot(f, '--r')

#PREDICTION
days = 2
print('Predition of Cases after',{days},'days:')
print((round(int(model.predict(poly.fit_transform([[294+days]]))))/1000000,2),'Million')

x1 = np.array(list(range(1,234+days))).reshape(-1,1)
y1 = model.predict(poly.fit_transform(x1))
plt.plot(y1, '--g')
plt.show()
