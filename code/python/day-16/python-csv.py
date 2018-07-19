import csv
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
    with open('new-name.csv','w') as newfile:
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
    with open('new-name.csv', 'a+') as newfile:
        csvreader = csv.DictReader(newfile, delimiter='\t')
        csvwriter = csv.DictWriter(newfile, delimiter='\t')
    flag=False
    while row in csvreader:
        if(row['Registration No.']==no):
            #do some shit
            flag=True
    if(flag==False):
        print('Incorrect Registration No.')
    elif(flag==True):
        fieldname = ['Name', 'Registration No.', 'Physics',
                     'Chemistry', 'Maths', 'Percentage', 'Course-Opted', 'Flag']
        for rows in csvreader:
            for i in rows:
                while(rows['Registration No.']==no)
        

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
