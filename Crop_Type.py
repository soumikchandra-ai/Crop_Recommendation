import pandas as pd
from Training_Crop_Type_Model import rfc
from Training_Crop_Type_Model import le_crop

def crop_pred(N,P,K,temp,humid,pH,rainfall):
    input_data=[N,P,K,temp,humid,pH,rainfall]
    input_features=['N','P','K','temperature','humidity','ph','rainfall']
    
    input_df=pd.DataFrame([input_data],columns=input_features)
    y_pred=rfc.predict(input_df)
    
    crop_type=le_crop.inverse_transform(y_pred)
    print(crop_type)