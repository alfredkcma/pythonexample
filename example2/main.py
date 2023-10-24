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
    buy_and_hold = []

with open('1299.HK_signal.csv') as f:
    csvr = csv.reader(f)
    alldata = [line for line in csvr]
    alldata.pop(0)
    buy_signal = []


print(stats.ttest_ind(buy_and_hold, buy_signal, equal_var=True))
