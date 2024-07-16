import pandas as pd
df = pd.read_csv('/Users/sivamani/AP21110010641/data_science/data.csv')
(df['Temperature'].max()) #max temaperature
(df['EST'][df['Events'] == 'Rain'])#dates fro rain
df.fillna(0, inplace=True)#filling na values with 0
(df['WindSpeedMPH'].mean())# mean of wind speed
