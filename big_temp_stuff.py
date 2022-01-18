import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

Avg_Max = []
Avg_Min = []
TMIN = 200
TMAX = 0

ARD2 = []
BEAV = []
BOIS = []
CENT = []
NRMN = []
STIL = []
TISH = []
TULN = []
WOOD = []

TMAX = [0,0,0,0,0,0,0,0,0]
TMIN = [200,200,200,200,200,200,200,200,200]

channel = ['ARD2','BEAV','BOIS','CENT','NRMN','STIL','TISH','TULN','WOOD']
with open("BigData2016.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        for x in range(len(channel)):
            if float(row['TMAX']) > 200 or float(row['TMAX']) < -200:
                pass
            else:
                if row['STID'] == channel[x]:
                    if x == 0:
                        ARD2.append((float(row["TMAX"])))
                        if float(row['TMAX']) > TMAX[0]:
                            TMAX[0] = float(row['TMAX'])
                    elif x == 1:
                        BEAV.append((float(row["TMAX"])))
                        if float(row['TMAX']) > TMAX[1]:
                            TMAX[1] = float(row['TMAX'])
                    elif x == 2:
                        BOIS.append((float(row["TMAX"])))
                        if float(row['TMAX']) > TMAX[2]:
                            TMAX[2] = float(row['TMAX'])
                    elif x == 3:
                        CENT.append((float(row["TMAX"])))
                        if float(row['TMAX']) > TMAX[3]:
                            TMAX[3] = float(row['TMAX'])
                    elif x == 4:
                        NRMN.append((float(row["TMAX"])))
                        if float(row['TMAX']) > TMAX[4]:
                            TMAX[4] = float(row['TMAX'])
                    elif x == 5:
                        STIL.append((float(row["TMAX"])))
                        if float(row['TMAX']) > TMAX[5]:
                            TMAX[5] = float(row['TMAX'])
                    elif x == 6:
                        TISH.append((float(row["TMAX"])))
                        if float(row['TMAX']) > TMAX[6]:
                            TMAX[6] = float(row['TMAX'])
                    elif x == 7:
                        TULN.append((float(row["TMAX"])))
                        if float(row['TMAX']) > TMAX[7]:
                            TMAX[7] = float(row['TMAX'])
                    else:
                        WOOD.append((float(row["TMAX"])))
                        if float(row['TMAX']) > TMAX[8]:
                            TMAX[8] = float(row['TMAX'])
            if float(row['TMIN']) > 200 or float(row['TMIN']) < -200:
                pass
            else:
                if row['STID'] == channel[x]:
                    if x == 0:
                        ARD2.append((float(row["TMIN"])))
                        if float(row['TMIN']) < TMIN[0]:
                            TMIN[0] = float(row['TMIN'])
                    elif x == 1:
                        BEAV.append((float(row["TMIN"])))
                        if float(row['TMIN']) < TMIN[1]:
                            TMIN[1] = float(row['TMIN'])
                    elif x == 2:
                        BOIS.append((float(row["TMIN"])))
                        if float(row['TMIN']) < TMIN[2]:
                            TMIN[2] = float(row['TMIN'])
                    elif x == 3:
                        CENT.append((float(row["TMIN"])))
                        if float(row['TMIN']) < TMIN[3]:
                            TMIN[3] = float(row['TMIN'])
                    elif x == 4:
                        NRMN.append((float(row["TMIN"])))
                        if float(row['TMIN']) < TMIN[4]:
                            TMIN[4] = float(row['TMIN'])
                    elif x == 5:
                        STIL.append((float(row["TMIN"])))
                        if float(row['TMIN']) < TMIN[5]:
                            TMIN[5] = float(row['TMIN'])
                    elif x == 6:
                        TISH.append((float(row["TMIN"])))
                        if float(row['TMIN']) < TMIN[6]:
                            TMIN[6] = float(row['TMIN'])
                    elif x == 7:
                        TULN.append((float(row["TMIN"])))
                        if float(row['TMIN']) < TMIN[7]:
                            TMIN[7] = float(row['TMIN'])
                    else:
                        WOOD.append((float(row["TMIN"])))
                        if float(row['TMIN']) < TMIN[8]:
                            TMIN[8] = float(row['TMIN'])
    for x in range(len(channel)):
        print(f'{channel[x]}: Max Temp = {TMAX[x]}, Min Temp = {TMIN[x]}')
        
# libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.array([1,2,3,4,5,6,7,8,9])
y = TMAX
y1 = TMIN

plt.plot(x, y, label='Maximum')
plt.plot(x,y1, 'r-.', label='Minimum')

leg = plt.legend(loc='center')
plt.xlabel("Channel")
plt.ylabel("Temperature")
plt.title("Weather Channel's Maximums and Minimums Temperature")

plt.show()

'''# Make a data frame
df=pd.DataFrame({'x': range(1,11), 'y1': np.random.randn(10), 'y2': np.random.randn(10)+range(1,11), 'y3': np.random.randn(10)+range(11,21), 'y4': np.random.randn(10)+range(6,16), 'y5': np.random.randn(10)+range(4,14)+(0,0,0,0,0,0,0,-3,-8,-6), 'y6': np.random.randn(10)+range(2,12), 'y7': np.random.randn(10)+range(5,15), 'y8': np.random.randn(10)+range(4,14) })

# Change the style of plot
plt.style.use('seaborn-darkgrid')

# set figure size
my_dpi=100
plt.figure(figsize=(5, 5), dpi=my_dpi)
 
# plot multiple lines
for column in df.drop('x', axis=1):
    plt.plot(df['x'], df[column], marker='', color='grey', linewidth=1, alpha=0.5)

# Now re do the interesting curve, but biger with distinct color
plt.plot(df['x'], df['y5'], marker='', color='blue', linewidth=3, alpha=0.5)
 
# Change x axis limit
plt.xlim(0,12)
 
# Let's annotate the plot
num=0
for i in df.values[9][1:]:
    num+=1
    name=list(df)[num]
    if name != 'y5':
        plt.text(10, i, name, horizontalalignment='right', size='small', color='grey')

# And add a special annotation for the group we are interested in
plt.text(10, df.y5.tail(1), 'Mr Orange', horizontalalignment='right', size='small', color='orange')
 
# Add titles
plt.title("Weather Channel's Maxs and Mins", loc='left', fontsize=12, fontweight=0, color='Green')
plt.xlabel("Temperature")
plt.ylabel("Channel")

# Show the graph
plt.show()'''