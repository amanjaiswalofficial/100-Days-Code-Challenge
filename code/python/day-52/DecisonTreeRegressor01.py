import pandas as pd
from sklearn.tree import DecisionTreeRegressor
# Path of the file to read
iowa_file_path = './train.csv'

#to read the file
home_data = pd.read_csv(iowa_file_path)

#to print the columns from the file
#print(home_data.columns) 

#which column to predict
y = home_data.SalePrice 

#columns to be used to calculate prediction
feature_names = ['LotArea', 'YearBuilt', '1stFlrSF',
                 '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']

#using columns to determine X
X = home_data[feature_names] 

#print(X.describe()) 

#first few columns
#print(X.head()) 

#random state allows randomization of values to be used in the training
#change as per need to determine prediction i.e. 1,2,3...
iowa_model = DecisionTreeRegressor(random_state=1)

#fitting/training the model
iowa_model.fit(X, y)

#predict the model
predictions = iowa_model.predict(X)

#print the prediction, no idea how to use so far
print(predictions)

