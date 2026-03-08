import pandas as pd

from Crop_Type import df

df1=df.drop(['fertilizer_name'],axis=1)

#Label Encoding the columns in df1
from sklearn.preprocessing import LabelEncoder
le1=LabelEncoder()
le2=LabelEncoder()

df1['soil_type']=le1.fit_transform(df['soil_type'])
df1['crop_type']=le2.fit_transform(df['crop_type'])
