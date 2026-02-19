from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import engine, Base
from auth import get_current_user, authenticate_user, create_access_token, get_db, get_password_hash
from models import CustomerData, UserCreate, Token, User, UserResponse
from churn_model import predict_churn_probability
from datetime import timedelta

app = FastAPI(
    title="ClientSense API",
    description="A powerful churn prediction and customer-insights engine",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "ClientSense API - Churn Prediction and Customer Insights"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_password = get_password_hash(user.password)
    db_user = User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return UserResponse(id=db_user.id, username=db_user.username, is_active=db_user.is_active)

@app.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

# Placeholder for churn prediction endpoint
@app.post("/predict_churn")
def predict_churn(customer: CustomerData, current_user: User = Depends(get_current_user)):
    prob = predict_churn_probability(customer.dict())
    return {"churn_probability": prob, "risk_level": "high" if prob > 0.5 else "low"}