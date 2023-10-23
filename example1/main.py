import csv
import numpy
import matplotlib.pyplot as plt
with open("hsbclife.csv") as f:
    csvf = csv.reader(f)
    irrlist = []
    yearlist = []
    for i, line in enumerate(csvf):
        if i > 0:
            yearlist.append(int(line[0]))
            cashflow = [-float(line[-1]) / float(yearlist[-1]) for k in range(yearlist[-1])]
            cashflow.append(float(line[4]))
            irrlist.append(numpy.irr(cashflow))
fig, ax = plt.subplots()
ax.plot(yearlist, irrlist, label="Ex Ante")

with open("real.csv") as f:
    csvf = csv.reader(f)
    rirrlist = []
    ryearlist = []
    for i, line in enumerate(csvf):
        if i > 0:
            ryearlist.append(int(line[0]))
            rcashflow = [cashflow[0] for k in range(ryearlist[-1])]
            rcashflow.append(float(line[1]) + float(line[2]))
            rirrlist.append(numpy.irr(rcashflow))

ax.plot(ryearlist, rirrlist, label="Ex Post")
plt.show()
