import pandas as pd

df=pd.read_excel('crop.xlsx')

df=df.rename(columns={'label':'crop_type'})
#Label Encoding the crop_type column
from sklearn.preprocessing import LabelEncoder
le_crop=LabelEncoder()

df['crop_type']=le_crop.fit_transform(df['crop_type'])
print(df.head())

#Defining X and y
X=df.drop(df['crop_type'],axis=1)
y=df['crop_type']

#Spliting X and y into train and test dataset
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
