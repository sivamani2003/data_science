import pandas as pd
df = pd.read_csv('/Users/sivamani/AP21110010641/data_science/data_day2.csv')
(df.shape) #print dimensions of the dataframe
rows, columns = df.shape
(rows)
(columns)# print number of rows and columns
(df.head(2))#print no of rows required rows from first
(df.tail(2))#print no of rows required rows from last
(df[2:5])#print pandas slicing
(df.columns)#print column names
(df.day)#accessing a column
(type(df['event']))#type of column
(df[['event','day']])#accessing multiple columns
(df['temperature'].max())#max temperature
(df['temperature'].min())#min temperature
(df['temperature'].mean())#mean temperature
(df['temperature'].std())#standard deviation
(df.describe())#summary statistics
(df[df['temperature']>32])#conditional selection
(df[df['temperature']==df['temperature'].max()])#conditional selection
(df['day'][df['temperature']==df['temperature'].max()])#conditional selection
(df.index)#index of the dataframe
(df.set_index('day',inplace=True))#setting index
(df.loc['1/1/2017'])#accessing row by index
(df.reset_index(inplace=True))#resetting index
df.set_index('event',inplace=True)
print(df.loc['Snow'])#accessing row by index