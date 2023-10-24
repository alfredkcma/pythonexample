import csv
import math
from scipy import stats
from ma import gen_signal

gen_signal('1299.HK.csv', 5, 30)

# perform t.test

with open('1299.HK.csv') as f:
    csvr = csv.reader(f)
    alldata = [line for line in csvr]
    alldata.pop(0)
    buy_and_hold = [math.log(float(alldata[i+1][5]) / float(alldata[i][5])) for i in range(len(alldata) - 1)]

with open('1299.HK_signal.csv') as f:
    csvr = csv.reader(f)
    alldata = [line for line in csvr]
    alldata.pop(0)
    buy_signal = [math.log(float(alldata[i+1][1]) / float(alldata[i][1])) for i in range(len(alldata) - 1) if int(alldata[i][4]) == 1]


print(stats.ttest_ind(buy_and_hold, buy_signal, equal_var=True))
