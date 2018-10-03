with open("./simple.txt", "r") as file:
    #filetxt1 = file.readline() #reads a single line
    #filetxt2=file.readlines() #reads all the lines

print(filetxt1)



"""with open("./simple.txt","r") as file:
    filetxt1=file.readline(1)#reads 1 character of the 1st line
    filetxt2=file.readline(10)#reads the next 10 character of the line, if 1st line ends move to 2nd
                                #to continue read until 10 characters are read

print(filetxt1)
print(filetxt2)"""

linelist=[]
with open("./simple.txt", "r") as file:
    for line in file:
        #print(line,end="")
        linelist.append(line)#saving into a list to use later

print(linelist)

#print(filetxt1)
