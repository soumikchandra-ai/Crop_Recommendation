import pandas as pd

from Crop_Type import df

df1=df.drop(['fertilizer_name'],axis=1)

#Label Encoding the columns in df1
from sklearn.preprocessing import LabelEncoder
le1=LabelEncoder()
le2=LabelEncoder()

df1['soil_type']=le1.fit_transform(df['soil_type'])
df1['crop_type']=le2.fit_transform(df['crop_type'])

#Training the model
X=df1.drop(['crop_type'],axis=1)
y=df1['crop_type']

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

from sklearn.ensemble import RandomForestClassifier
rfc=RandomForestClassifier(n_estimators=100)

rfc.fit(X_train,y_train)

y_pred=rfc.predict(X_test)

from sklearn.metrics import accuracy_score
accuracy=accuracy_score(y_test,y_pred)