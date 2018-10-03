import pandas as pd
df=pd.read_csv('./pandas1.csv') #reading the csv file
#print(df.head()) #printing 1st five records

x=df[['Values']]
#print(x.head()) #printing for a specific column

y=df[['Values','Range']] #printing a set of specific columns
#print(y.head()) 
m = df.iloc[0, 0] #iloc allows to locate a cell using coordinates
print(m)
n=df.loc[3,'Range'] #loc allows to locate similar based on the column name
print(n)
o=df.iloc[0:2,0:2] #iloc also used for saving from a range of val, making the variable a dataframe
print(o)
p=df.loc[0:2,'Names':'Range'] #loc same thing just by using column name
print(p)
