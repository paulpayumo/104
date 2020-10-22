import numpy as np
import matplotlib.pyplot as plt
#from sklearn.linear_model import linear_model
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
import pandas as pd

# DATA SET UP
data = pd.read_csv('OWCoronaCasesTest.csv' , sep = ',')
data = data[['ID','World']]
data = data[60:150]
print(data)

x = np.array(data['ID']).reshape(-1,1)
y = np.array(data['World']).reshape(-1,1)
plt.plot(y,'-b', label = "Actual World Cases")

poly = PolynomialFeatures(degree=2)
x = poly.fit_transform(x)

#TRAINING DATA
model = linear_model.LinearRegression()
model.fit(x,y)
accuracy = model.score(x,y)
print('Accuracy:',round(accuracy*100,3),'%')
"""
f = model.predict(x)
plt.plot(f, '--r')
"""
#PREDICTION
print('Predition of Cases at day 240:')
print((round(int(model.predict(poly.fit_transform([[240]]))))/1000000),'Million')

x1 = np.array(list(range(151,241))).reshape(-1,1)
y1 = model.predict(poly.fit_transform(x1))
y= np.concatenate((y, y1), axis = 0)
plt.plot(y, '--g', label = "Prediction")
plt.legend()
plt.ylabel('World Cases x(1e7)')
plt.xlabel('Day of the Year(0 = 60 days)')
plt.show()
