import numpy as np
import matplotlib.pyplot as plot
import parse_csv, matplotlib

data=parse_csv.reading_csv('data.csv')

x1=[]
y1=[]
for point in data:
    if point['survived']==1 and type(point['age'])==float and type(point['fare'])==float:
        x1.append(point['age'])
        y1.append(point['fare'])

x0=[]
y0=[]
for point in data:
    if point['survived']==0 and type(point['age'])==float and type(point['fare'])==float:
        x0.append(point['age'])
        y0.append(point['fare'])

matplotlib.rcParams['axes.unicode_minus'] = False
fig = plot.figure()
ax = fig.add_subplot(111)
plot.yscale('log')
plot.xlabel('Age')
plot.ylabel("Ticket's fare paid (allegedly in British pounds)")
ax.plot(x1,y1, 'o',color='b')
ax.plot(x0,y0, 'o',color='r')
ax.set_title('Age vs. fare cost')
#plot.show()
plot.savefig('plot1.pdf')
plot.savefig('plot1.png')
plot.close()




