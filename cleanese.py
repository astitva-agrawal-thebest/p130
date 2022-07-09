import pandas as pd
import csv
df = pd.read_csv("total_stars.csv")
print(df.columns)
df.drop(['Unnamed: 0','Unnamed: 6', 'Star_name1', 'Distance1', 'Mass1', 'Radius1','Luminosity'],axis=1,inplace=True)
finaldata=df.dropna()
finaldata.reset_index(drop=True,inplace=True)
finaldata.to_csv("main.csv")