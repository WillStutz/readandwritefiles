import csv
from csv import *

def main():

    infile = open('steps.csv','r')
    csvfile = csv.reader(infile)
    next(csvfile)
    
    counter_1 = 0
    counter_2 = 0
    counter_3 = 0
    counter_4 = 0
    counter_5 = 0
    counter_6 = 0
    counter_7 = 0
    counter_8 = 0
    counter_9 = 0
    counter_10 = 0
    counter_11 = 0
    counter_12 = 0


    for record in csvfile:
        if int(record[0]) == 1:
            steps_1 = int(record[1])
            counter_1 += steps_1
            avg_steps_jan = counter_1/31
        elif int(record[0]) == 2:
            steps_2 = int(record[1])
            counter_2 += steps_2
            avg_steps_feb = counter_2/28
        elif int(record[0]) == 3:
            steps_3 = int(record[1])
            counter_3 += steps_3
            avg_steps_mar = counter_3/31
        elif int(record[0]) == 4:
            steps_4 = int(record[1])
            counter_4 += steps_4
            avg_steps_apr = counter_4/30
        elif int(record[0]) == 5:
            steps_5 = int(record[1])
            counter_5 += steps_5
            avg_steps_may = counter_5/31
        elif int(record[0]) == 6:
            steps_6 = int(record[1])
            counter_6 += steps_6
            avg_steps_jun = counter_6/30
        elif int(record[0]) == 7:
            steps_7 = int(record[1])
            counter_7 += steps_7
            avg_steps_jul = counter_7/31
        elif int(record[0]) == 8:
            steps_8 = int(record[1])
            counter_8 += steps_8
            avg_steps_aug = counter_8/31
        elif int(record[0]) == 9:
            steps_9 = int(record[1])
            counter_9 += steps_9
            avg_steps_sep = counter_9/30
        elif int(record[0]) == 10:
            steps_10 = int(record[1])
            counter_10 += steps_10
            avg_steps_oct = counter_10/31
        elif int(record[0]) == 11:
            steps_11 = int(record[1])
            counter_11 += steps_11
            avg_steps_nov = counter_11/30
        elif int(record[0]) == 12:
            steps_12 = int(record[1])
            counter_12 += steps_12
            avg_steps_dec = counter_12/31
        
    outfile =  open('avg_steps.csv','w')
    csvwriter =csv.writer(outfile)
    headers = ['Month','Average']
    csvwriter.writerow(headers)

    csvwriter.writerow(['Jan:',avg_steps_jan])
    csvwriter.writerow(['Feb:',avg_steps_feb])
    csvwriter.writerow(['Mar:',avg_steps_mar])
    csvwriter.writerow(['Apr:',avg_steps_apr])
    csvwriter.writerow(['May:',avg_steps_may])
    csvwriter.writerow(['Jun:',avg_steps_jun])
    csvwriter.writerow(['Jul:',avg_steps_jul])
    csvwriter.writerow(['Aug:',avg_steps_aug])
    csvwriter.writerow(['Sep:',avg_steps_sep])
    csvwriter.writerow(['Oct:',avg_steps_oct])
    csvwriter.writerow(['Nov:',avg_steps_nov])
    csvwriter.writerow(['Dec:',avg_steps_dec])


   
        

    

main()
