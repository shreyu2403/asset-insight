import csv
import numpy

csvfile = open ('Compactor_modified1', 'r')
reader = csv.reader(csvfile, delimiter=',')
headers = reader.next()

#calculate the size of the grid
x_size = []
y_size =  []

#calculate the size of the array base on the max_value possible(maybe not necessary if you want a normalized size)
for row in reader:
    x_size.append(int(row[2]))
    y_size.append(int(row[3]))

#create an array of the right size with zero
my_array = numpy.zeros((max(x_size)+1,max(y_size)+1), numpy.int16)

#create lists to loop through the array
val_I = range(0, max(x_size)+1, 1)
val_J= range(0, max(y_size)+1, 1)

#loop in the array
reader = csv.reader(csvfile, delimiter=',')
for i in val_I:
    for j in val_J:
        csvfile.seek(0)
        headers = reader.next()
        count = 0
        group = []
        for row in reader:
            if int(row[2]) == i and int(row[3]) == j: #add the value if coordinate match
                if row[1] not in group: #avoid counting to time the same group
                    group.append(row[1])
                    count += 1
        my_array[i,j] = count #add the value to array
# you got your array
print (my_array)