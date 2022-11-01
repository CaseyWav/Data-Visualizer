from matplotlib import pyplot as plt
import csv
import numpy as np

filename = 'baselinedata_corrections.csv'

def readFile(filename):
    f = open(filename, encoding='UTF8')
    d13c = []
    d15n = []
  
    with open(filename,'r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        for row in lines:
            d13c.append(row[0])
            d15n.append(int(row[1]))
  
    plt.scatter(d13c, d15n, color = 'g',s = 100)
    plt.xticks(rotation = 25)
    plt.xlabel('Carbon')
    plt.ylabel('Nitrogen')
    plt.title('Food chart', fontsize = 20)
  
    plt.show()

    f.close()