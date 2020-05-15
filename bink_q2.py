#2. From the list of all mast data, create a new list of mast data with “Lease Years” = 25 years.
#    a. Output the list to the console, including all data fields
#    b. Output the total rent for all items in this list to the console
import csv

datafile = open('Python Developer Test Dataset.csv','r')

data = csv.reader(datafile, delimiter=',')

lease_list = [x for x in data if "25" in x]

total = 0

print("Lease Years = 25 years") 
print("----------------------")

for row in lease_list:
    print(*row, sep = ", ")  

    total += (float(row[10]))
    

print("----------------------")  
print('Total rental is...', '%.2f' % total)

datafile.close()