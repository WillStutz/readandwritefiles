import csv
from csv import *

infile = ('steps.csv','r')
csvfile = csv.reader(infile,delimiter=',')
next(csvfile)

def main():


    def jan(avg_steps_jan):
        print('Jan:',avg_steps_jan)

        counter_1 = 0
        for record in csvfile:
            month_1 = int(record[0])
            if month_1 == 1:
                steps_1 = int(record[1])
                counter_1 += steps_1
                avg_steps_jan = counter_1/31
        return avg_steps_jan


    jan()

main()




