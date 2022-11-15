import matplotlib.pyplot as plt
import csv
  

d13c = []
d15n = []
  
with open('Data-Visualizer/baselinedata_corrections.csv','r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        d13c.append(row[0])
        d15n.append(row[1])
  
plt.scatter(d13c, d15n, color = 'g',s = 100)
plt.xticks(rotation = 25)
plt.xlabel('Carbon')
plt.ylabel('Nitrogen')
plt.title('Food chart', fontsize = 20)
  
plt.show()
