import matplotlib.pyplot as plt
import csv
import pandas as pd
  

data = pd.read_csv('')
type = data['type']
specifics = data['specifics']
d13c = data['d13C']
d15n = data['d15N']

plt.scatter(d13c,d15n, edgecolor='black', linewidth=1, alpha=0.75)
  
plt.xlabel('Carbon')
plt.ylabel('Nitrogen')
plt.title('Food chart')
  
plt.tight_layout()
plt.show()
