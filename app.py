import uvicorn
from fastapi import FastAPI
from features import userinfo
import numpy as np
import pandas as pd
import pickle
# App objesi oluşturuldu.
app = FastAPI()
pickle_in=open("xgboost_pickle.pkl","rb")
classifier =pickle.load(pickle_in)

@app.get('/')
def index():
    return {'message': 'Hello world'}

@app.post('/predict')
def predict_churn(data:userinfo):
    data = data.dict()
    print(data)
    Gender=data['gender']
    SeniorCitizen=data['SeniorCitizen']
    Dependents=data['Dependents']
    Tenure=data['tenure']
    PhoneService=data['PhoneService']
    MultipleLines=data['MultipleLines']
    InternetService=data['InternetService']
    OnlineSecurity=data['OnlineSecurity']
    OnlineBackup=data['OnlineBackup']
    DeviceProtection=data['DeviceProtection']
    TechSupport=data['TechSupport']
    StreamingTv=data['StreamingTv']
    StreamingMovies=data['StreamingMovies']
    Contract=data['Contract']
    PaperlessBilling=data['PaperlessBilling']
    PaymentMethod=data['PaymentMethod']
    MonthlyCharges=data['MonthlyCharges']
    TotalCharges=data['TotalCharges']

    prediction=classifier.predict([[Gender,
                                SeniorCitizen,
                                Dependents,
                                Tenure,
                                PhoneService,
                                MultipleLines,
                                InternetService,
                                OnlineSecurity,
                                OnlineBackup,
                                DeviceProtection,
                                TechSupport,
                                StreamingTv,
                                StreamingMovies,
                                Contract,
                                PaperlessBilling,
                                PaymentMethod,
                                MonthlyCharges,
                                TotalCharges]])
    if(prediction[0]==0):
        prediction="Eleman seninle"
    else:
        prediction="Elemanı kaçırdın"
    return {'prediction':prediction}

if __name__ == '__main__':
    uvicorn.run(app,host='127.0.0.1',port=8000)
