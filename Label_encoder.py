import pandas as pd

df=pd.read_csv('crop.csv')

#Label Encoding the crop_type column
from sklearn.preprocessing import LabelEncoder
le_crop=LabelEncoder()
le_soil=LabelEncoder()
le_fertilizer=LabelEncoder()
df['Crop']=le_crop.fit_transform(df['Crop'])
df['Soil']=le_soil.fit_transform(df['Soil'])
df['Fertilizer']=le_fertilizer.fit_transform(df['Fertilizer'])

#Refining the dataframe
df_refined=df.drop('Remark',axis=1)