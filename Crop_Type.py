import pandas as pd
from sklearn.preprocessing import LabelEncoder

#Reading the csv file
df=pd.read_csv('crop.csv')

#Renaming the columns
df=df.rename(columns={'Soil Type':'soil_type','Fertilizer Name':'fertilizer_name','Crop Type':'crop_type'})

#Transforming the columns having text to number through encoding
#(1)soil_type
from sklearn.preprocessing import LabelEncoder
le1=LabelEncoder()

le1.fit(df['soil_type'])
# print(le1.classes_)
le1.transform(df['soil_type'])
# print(le1.inverse_transform([4,2,0]))

#(2)crop_type
from sklearn.preprocessing import LabelEncoder
le2=LabelEncoder()

le2.fit(df['crop_type'])
# print(le2.classes_)
le2.transform(df['crop_type'])
# print(le2.inverse_transform([4,2,0]))

#(3)fertilizer_name
from sklearn.preprocessing import LabelEncoder
le3=LabelEncoder()

le3.fit(df['fertilizer_name'])
# print(le3.classes_)
le3.transform(df['fertilizer_name'])
# print(le3.inverse_transform([4,2,0]))