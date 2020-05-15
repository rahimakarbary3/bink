#3. Create a dictionary containing tenant name and a count of masts for each tenant
#       a. Output the dictionary to the console in a readable form

import csv

def TotalMast():
    datafile = open('Python Developer Test Dataset.csv','r')

    data = csv.DictReader(datafile, delimiter=',')

    no_of_masts = 0

    key = data.fieldnames[6] 
    names = []

    for row in data:
        no_of_masts = no_of_masts + 1
        names.append(row.get(key))
    result = {key: names}

    print(key)
    print("----------------------")
    print(names,sep = ",")

    print("Total Number of Masts") 
    print("----------------------")
    print (no_of_masts)

    datafile.close()
    
    return no_of_masts

    
    







