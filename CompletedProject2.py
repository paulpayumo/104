import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
import pandas as pd

#Reads the data from the csv file below and inputs it into variable y
y = pd.read_csv('WHO-COVID-19-global-data - Pivot Table 1.csv' , sep = ',')
#removes all data except for the data under sum of cumulative cases
y = y['SUM of Cumulative_cases']
#removes all data outside of the 3 month range from April 1, to July 1
y1 = y[94:182]
y2 = y[182: 275]

#Creates an array X, containing the day numbers from 94 to 185 
x = np.array(list(range(94,182))).reshape(-1,1)
#converts y into an array
y1 = np.array(y1).reshape(-1,1)

#Creates a figure for the real data
fig = plt.figure()

#Plots the data from the csv file
plt.plot(x, y1,'-b', label = "Actual World Cases")

#creates labels and title and legend
plt.title('Actual Number of Cases in the world each day')
plt.ylabel('Number of cases in 10 millions')
plt.xlabel('April 1 (Day 94 in CSV) to July 1 (Day 182 in CSV)')
plt.legend()

#creates a polynomial with degree 2 function
poly = PolynomialFeatures(degree=2)
x = poly.fit_transform(x)

#turn on grid
plt.grid(True)

#creates the prediction model 
prediction = linear_model.LinearRegression()
prediction.fit(x,y1)

#Creates a figure for prediction data
fig1 = plt.figure()

#creates a new x value array from 183 to 276 which represents July 2, to October 1
x1 = np.array(list(range(182,275))).reshape(-1,1)
#creates y values based on the created prediction model
y3 = prediction.predict(poly.fit_transform(x1))

#plots the prediction plot vs the actual number of cases
plt.plot(x1, y3, '-r', label = "Predicted # of cases")
plt.plot(x1, y2, '--b', label = "Actual # of cases ")
#turn on grid
plt.grid(True)

#Creates x and y label and title and legend
plt.title('Predicted vs Actual # of Cases in the world each day')
plt.ylabel('Number of cases in 10 millions')
plt.xlabel('July 1 (Day 182 in CSV) to October 1 (Day 276 in CSV)')
plt.legend()

#shows plt
plt.show()
