#4. List the data for rentals with “Lease Start Date” between 1st June 1999 and 31st August 2007
#    a. Output the data to the console with dates formatted as DD/MM/YYYY

import csv
import datetime

datafile = open('Python Developer Test Dataset.csv','r')

data = csv.reader(datafile, delimiter=',')
next(data)

start_date = (datetime.datetime.strptime("1 Jun 1999", "%d %b %Y"))
end_date   = (datetime.datetime.strptime("31 Aug 2007", "%d %b %Y"))

for item in data:
    lease_start_date =(datetime.datetime.strptime(item[7], "%d %b %Y") )
    #print("start:", start_date, "lease:", lease_start_date, "end", end_date)
    if start_date < lease_start_date < end_date:
        item[7] = ( datetime.datetime.strptime(item[7] , "%d %b %Y").strftime('%d/%m/%Y') )
        print(item)

datafile.close()

    

    

