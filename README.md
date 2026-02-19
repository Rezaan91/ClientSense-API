# ClientSense API

A powerful churn prediction and customer-insights engine designed for businesses seeking to retain more customers and increase lifetime value.

## Features

- Predictive churn scoring
- Customer sentiment analysis
- Engagement monitoring
- Automated early-warning alerts
- Recommendations for targeted retention actions

## Installation

1. Clone the repository
2. Create virtual environment: `python -m venv .venv`
3. Activate: `.venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`

## Running the API

`uvicorn main:app --reload`

Then visit http://127.0.0.1:8000/docs for interactive API docs.

## Endpoints

- GET / : Welcome message
- GET /health : Health check
- POST /predict_churn : Predict churn (placeholder)