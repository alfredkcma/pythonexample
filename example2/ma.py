import csv

def gen_signal(data, short, long):
    """
    this code genereate signals and write to csv
    data is the filename from data downloaded from YHF
    short is the number of days for short line MA
    long is the number of days for long line MA
    """
    outfilename = data[0:-4] + '_signal' + data[-4:]
    print(outfilename)
    csvw = csv.writer(open(outfilename, 'w'))
    csvw.writerow(['Date', 'Adj Close', 'SMA', 'LMA', 'BuySignal'])
    with open(data) as f:
        csvr = csv.reader(f)
        pricelist = []
        for i, line in enumerate(csvr):
            if i > 0:
                price = float(line[5])
                pricelist.append(price)
                if len(pricelist) >= long:
                    sma = short
                    lma = long
                    csvw.writerow([line[0], line[5], sma, lma, int(sma >= lma)])

