# ClientSense API

A powerful churn prediction and customer-insights engine designed for businesses seeking to retain more customers and increase lifetime value.

## Features

- Predictive churn scoring
- Customer sentiment analysis
- Engagement monitoring
- Automated early-warning alerts
- Recommendations for targeted retention actions
- User authentication and authorization
- Database integration with SQLAlchemy

## Installation

1. Clone the repository
2. Create virtual environment: `python -m venv .venv`
3. Activate: `.venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`

## Running the API

`uvicorn main:app --reload`

Then visit http://127.0.0.1:8000/docs for interactive API docs.

## Authentication

- Register a new user: POST `/register` with username and password
- Login: POST `/token` with form data to get JWT token
- Use the token in Authorization header for protected endpoints

## Endpoints

- GET / : Welcome message
- GET /health : Health check
- POST /register : Register a new user
- POST /token : Login and get access token
- POST /predict_churn : Predict churn (requires authentication)