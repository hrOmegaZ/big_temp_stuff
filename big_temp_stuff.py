import csv
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