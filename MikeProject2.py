#Data from https://covid19.who.int/
#Created another CSV by making a pivot table with the dates and the sums for each date

import matplotlib.pyplot as plt
import numpy as np



data = []
oldData = []
selectedData = []
numbers = []
oldNumbers = []
count = 0

f = open("./Edited WHO-COVID-19-global-data.csv")
for line in f:
    data.append(line.split(","))
    
for i in range(1, len(data) - 1):
    oldNumbers.append(i)
    date = data[i][0]
    year = int(data[i][0][0:4])
    month = int(data[i][0][5:7])
    day = int(data[i][0][8:10])
    oldData.append(int(data[i][1].strip("'")))
    #print(date)
    if(month > 2 and month < 6):
        numbers.append(count + 59)
        count += 1
        selectedData.append(int(data[i][1].strip("'")))
        #numbers.append(count)
        #plt.plot(numbers, int(data[i][1].strip("'")))
        #plt.plot(i, 1)
        #plt.plot(date, int(data[i][1].strip("'")))
        #selectedData.append(data[i][1].split())
        
#print(selectedData)

plt.plot(numbers, selectedData, 'b')
plt.plot(oldNumbers, oldData, 'b')

numbers = np.array(numbers).reshape(-1, 1)
selectedData = np.array(selectedData).reshape(-1, 1)
#print(numbers)
#graph = linear_model.LinearRegression()
#graph.fit(numbers, selectedData)


#print(f.readlines()[59:150])

"""
reader = csv.DictReader(f)
for i, row in enumerate(reader):
    print(row[0])
    if(i > 10):
        break
f.close()
"""
