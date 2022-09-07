import csv
from csv import *

def main():

    infile = open('EmployeePay.csv','r')
    csvfile = csv.reader(infile)
    next(csvfile)
    
    counter = 0
    
    for record in csvfile:
        counter += 1
        pay = float(record[3])
        bonus  = float(record[4])
        bonus_pay = (1+bonus)*pay
        print(counter,'.',record[1],record[2],bonus_pay)
        input()

    csvfile.close()


main()



