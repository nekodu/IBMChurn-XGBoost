from pydantic import BaseModel
class userinfo(BaseModel):
    gender:object
    SeniorCitizen:int
    Partner:object
    Dependents:object
    tenure:int
    PhoneService:object
    MultipleLines:object
    InternetService:object
    OnlineSecurity:object
    OnlineBackup:object
    DeviceProtection:object
    TechSupport:object
    StreamingTV:object
    StreamingMovies:object
    Contract:object
    PaperlessBilling:object
    PaymentMethod:object
    MonthlyCharges:float
    TotalCharges:object