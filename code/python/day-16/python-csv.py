import csv

with open('student.csv','r') as csv_file:
    csv_reader=csv.reader(csv_file)

    for line in csv_reader:
        #print(line) to print each row with all it's entries
        #print(line[2]) to print only the 3rd entry in each row's data