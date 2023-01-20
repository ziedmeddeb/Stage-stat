import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def addlabels(x,y,n):
    for i in range(len(x)):
         axis[n].text(i, y[i]//2, round(y[i],3), ha = 'center')

df= pd.read_csv('Comparison-RSRP1.csv',skiprows=[1])
df.head()

x = np.array(["TELECOM", "OOREDOO", "ORANGE"])
c=['cyan','red','orange']
figure, axis = plt.subplots(nrows=3, figsize=(10,15))

avg = np.array([df['TT'].mean(),df['OO'].mean(),df['OR'].mean()])

max = np.array([df['TT'].max(),df['OO'].max(),df['OR'].max()])

min=np.array([df['TT'].min(),df['OO'].min(),df['OR'].min()])

axis[0].invert_yaxis()
axis[0].bar(x, avg,width=0.3,color=c)
axis[0].set_title("Average")
addlabels(x,avg,0)


axis[1].invert_yaxis()
axis[1].bar(x, max,width=0.3,color=c)
axis[1].set_title("Max")
addlabels(x,max,1)

axis[2].invert_yaxis()
axis[2].bar(x, min,width=0.3,color=c)
axis[2].set_title("Min")
addlabels(x,min,2)


plt.title("Min")
figure.tight_layout(pad=5.0)
plt.show()








