import csv
import numpy as np
from statistics import mean
from sklearn import linear_model
import matplotlib.pyplot as plt


dates = []
X = [[],[],[],[],[]]
y = []


def get_data(filename):
    with open(filename, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)  # skipping column names
        for row in csvFileReader:
            dates.append(int(row[0].split('-')[0]))
            X[0].append(float(row[1]))
            X[1].append(float(row[2]))
            X[2].append(float(row[3]))
            X[3].append(float(row[5]))
            y.append(float(row[4]))
    return


get_data('aapl.csv')

model = linear_model.LinearRegression()
model.fit(X,y)

for xs in X:
    print(model.predict(xs))

