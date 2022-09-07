import csv
from csv import *
def main():

    infile = open('customers.csv', 'r')
    csvfile = csv.reader(infile)
    next(csvfile)
    
    outfile = open('Customers_Country.csv','w',newline = '')
    
    csvwrite = csv.writer(outfile)

    categories = ['Full Name', 'Country']

    csvwrite.writerow(categories)

    counter = 0

    for record in csvfile:
        csvwrite.writerow([record[1],record[2],record[4]])
        counter += 1

    print(counter)
        
    infile.close()
    outfile.close()


main()