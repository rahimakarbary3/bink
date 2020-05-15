#1. Read in the attached file
#    a. Produce a list sorted by “Current Rent” in ascending order
#    b. Obtain the first 5 items from the resultant list and output to the console

import csv

def RentExtract():
    datafile = open('Python Developer Test Dataset.csv','r')

    data = csv.reader(datafile, delimiter=',')

    print(next(data, None))

    sort = sorted(data,key= lambda x: float(x[10]))

    count = 0

    for line in sort:
        count += 1
        print(line)
        if count > 4:
            break

    datafile.close()

    return count