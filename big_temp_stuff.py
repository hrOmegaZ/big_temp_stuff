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

channel = ['ARD2','BEAV','BOIS','CENT','NRMN','STIL','TISH','TULN','WOOD']
with open("BigData2016.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        for x in range(len(channel)):
            if row['STID'] == channel[x]:
                if x == 1:
                    ARD2.append((float(row["TMAX"])))