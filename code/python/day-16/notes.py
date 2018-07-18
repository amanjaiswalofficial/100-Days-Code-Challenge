import csv
"""with open('student.csv','r') as csv_file:
    #no delimiter here, hence, dont know how to read data, in what format
    csv_reader=csv.reader(csv_file)
    #below code reads the file based on delimiter , hence every 2 elements having , in between are 2 different elements
    csv_reader=csv.reader(csv_file,delimiter=','

    for line in csv_reader:
        #print(line) to print each row with all it's entries
        #print(line[2]) to print only the 3rd entry in each row's data

        #below code is to take data from above students file and then, using - as a delimiter, write it to a new file named new-name
        with open('new-name.csv','w') as new-file:
            csv_writer=csv.writer(new-file, delimiter='-') OR
            csv_writer=csv.writer(new-file, delimiter='\t')

            for line in csv_reader:
                csv_writer.writerow(line)"""
Arr = ['aman', 'chaitanya', 'amit', 'deepanshu', 'ajay', 'saurav']
with open('new-name.csv', 'a') as newfile:
    csv_writer = csv.writer(newfile, delimiter='\t')
    csv_writer.writerow(Arr)

"""with open('new-name.csv') as newfile:
    csv_reader = csv.reader(newfile, delimiter='')
    for row in csv_reader:
        print(row)"""
        
#tip
#generally on readin the first row containing the col names also read, to avoid, use
#next(csv_reader) this skips the first line and then will print when we use for loop


#using dictreader
csv_reader=csv.DictReader(filename)
for line in csv_reader:
    print(line)
    print(line['email'])#here email being the key
    and any other possible combination

#using dictwriter
fieldnm=['Name','CLass','etc']
csv_writer=csv.DictWriter(filename,fieldnames=fieldnm,delimiter='\t')
csv_writer.writeheader()#this is optional, this only writes the first row as the fieldnames values
for row in csv_writer:
    csv_writer.writerow(row)

#assignment: to store only name and class, no etc
fieldnm = ['Name', 'CLass']#remove etc from the field names
csv_writer = csv.DictWriter(filename, fieldnames=fieldnm, delimiter='\t')
# this is optional, this only writes the first row as the fieldnames values
csv_writer.writeheader()
for row in csv_writer:
    del row['etc']#delete the value from each entry as well
    csv_writer.writerow(row)#write the remaining in the csv file
