from fastapi import FastAPI
from models import CustomerData
from churn_model import predict_churn_probability

app = FastAPI(
    title="ClientSense API",
    description="A powerful churn prediction and customer-insights engine",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "ClientSense API - Churn Prediction and Customer Insights"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Placeholder for churn prediction endpoint
@app.post("/predict_churn")
def predict_churn(customer: CustomerData):
    prob = predict_churn_probability(customer.dict())
    return {"churn_probability": prob, "risk_level": "high" if prob > 0.5 else "low"}