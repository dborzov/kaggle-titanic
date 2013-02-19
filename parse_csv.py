
import csv
import numpy as np


def reading_csv(file_name):
    csv_file = csv.reader(open(file_name, 'rb')) #Load in the csv file
    header = csv_file.next() #Skip the fist line as it is a header
    data=[] #Create a variable called 'data'
    for row in csv_file: #Skip through each row in the csv file
        point=dict([]) # A dictionary  with all person's attributes
        for _,column in enumerate(header):
            try:
                point[column]=np.float(row[_])
            except:
                point[column]=row[_]
        data.append(point) #adding each row to the data variable
    data = np.array(data) #Then convert from a list to an array
    return data


