import pandas as pd
df=pd.read_csv('pandas1.csv')



x=df['Items']>=5
y=df[df['Items']>=5]
print(x)
print(y)

y.to_csv('pandas2.csv')

df2=pd.read_csv('pandas2.csv')
print(df2)