#below uses a list and its content to write into a text file line by line

"""lines=['A\n','B\n','C\n','D\n']
with open('./write.txt', 'w') as file:
    for line in lines:
        file.write(line)"""

#below writes all lines at once using writelines

lines = ['A\n', 'B\n', 'C\n', 'D\n']
with open('./write.txt', 'a') as file:#a mode appends, w mode writes
    file.writelines(lines)
