from pydantic import BaseModel

class CustomerData(BaseModel):
    tenure: int
    monthly_charges: float
    total_charges: float
    # Add more fields as needed for churn prediction