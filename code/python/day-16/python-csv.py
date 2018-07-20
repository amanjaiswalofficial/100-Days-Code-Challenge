import csv
import os
def choice():
    print('Enter your choice:')
    print('1.Enter Data')
    print('2.Edit Data')
    print('3.Display Data')
    print('4.Make Data Active/Inactive')
    ch=int(input('Enter your choice:'))
    return ch

c=choice()

# this is optional, this only writes the first row as the fieldnames value
if(c==1):
    with open('new-name.csv','a+') as newfile:
        fieldname = ['Name', 'Registration No.', 'Physics',
                     'Chemistry', 'Maths', 'Percentage', 'Course-Opted', 'Flag']
        csvwriters = csv.DictWriter(newfile, fieldnames=fieldname, delimiter='\t')
        csvwriters.writeheader()
        row=[]
        choice=True
        while(choice==True):
            data=dict()
            for i in range(len(fieldname)):
                val=str(input(fieldname[i]+':'))
                data[str(fieldname[i])]=val
            row.append(data)
            ch=str(input('Any more entries(Y/N):'))
            if(ch=='Y'):
                choice=True
            elif(ch=='N'):
                choice=False
            else:
                choice=False
                print('Wrong entry')    
        for r in row:
            csvwriters.writerow(r)

elif(c==2):
    no=int(input('Enter registration number to edit the data for a record:'))
    fieldname = ['Name', 'Registration No.', 'Physics',
                 'Chemistry', 'Maths', 'Percentage', 'Course-Opted', 'Flag']
    copy = []
    flag = False
    row = []
    with open('new-name.csv', 'r+') as newfile:
        csvreader = csv.DictReader(newfile, delimiter='\t')
        csvwriter = csv.DictWriter(newfile,fieldnames=fieldname, delimiter='\t')    
        for row in csvreader:
            if(int(row['Registration No.']) == no):
                flag = True
                continue
            else:
                copy.append(row)
        if(flag == False):
            print('Incorrect Registration No.')
        elif(flag == True):
            print('New Record Details:')
            row['Name'] = str(input('New name:'))
            row['Registration No.'] = str(input('New registration no.:'))
            row['Physics'] = str(input('Physics:'))
            row['Chemistry'] = str(input('Chemistry:'))
            row['Maths'] = str(input('Maths:'))
            row['Percentage'] = str(input('Percentage:'))
            row['Course-Opted'] = str(input('Course Opted:'))
            row['Flag'] = str(input('Flag:'))
            temp = []
            temp = row.copy()
            print(copy)
            print(temp)
            
    os.remove('new-name.csv')
    with open('new-name.csv', 'w') as newfile:
        csvwriter = csv.DictWriter(newfile,fieldnames=fieldname, delimiter='\t')
        csvwriter.writeheader()
        for x in copy:
            csvwriter.writerow(x)
            

elif(c==3):
    fieldname = ['Name', 'Registration No.', 'Physics',
                 'Chemistry', 'Maths', 'Percentage', 'Course-Opted','Flag']
    with open('new-name.csv','r') as newfile:
        csvreader=csv.DictReader(newfile,delimiter='\t')
        print()
        for rows in csvreader:
            for i in rows:
                print(str(i)+":"+str(rows[i]))
            print()
            """print(rows['Name']+'\t'+rows['Registration No.']+'\t'+rows['Physics'] + '\t' +
                  rows['Chemistry']+'\t'+rows['Maths']+'\t'+rows['Percentage']+'\t'+rows['Course-Opted'])"""

"""import csv
fieldname = ['Name', 'Registration No.', 'Physics',
             'Chemistry', 'Maths', 'Percentage', 'Course-Opted', 'Flag']
#myDictData = [{'ID': '3794', 'CountryCode': 'USA','District': 'California'},{'ID': '3795', 'CountryCode': 'USA','District': 'Illinois'},{'ID': '3796', 'CountryCode': 'USA', 'District': 'Texas'},{'ID': '3797', 'CountryCode': 'USA', 'District': 'Pennsylvania'}]
#myFilePath = os.path.join(filePath, 'MyDictionary.csv')

with open('./new-file.csv', 'w', newline='') as myCSVFile:
    csvWriter = csv.DictWriter(myCSVFile, fieldnames=fieldname, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
    csvWriter.writeheader()
    for data in myDictData:
        csvWriter.writerow(data)"""
