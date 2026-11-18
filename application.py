from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Data save thevnyasaathi temporary dictionary (Database)
applications_db = {}

class LoanApplication(BaseModel):
    customer_id: int
    age: int
    income: float

# 1. Data POST kara aani Save kara
@app.post("/loan-application")
def process_loan_application(application: LoanApplication):
    # Tujha logic
    if application.age < 18 and application.income < 20000:
        decision = "Rejected"
    else:
        decision = "Approved"

    # Aalela purna data aani decision dictionary madhe SAVE kara
    applications_db[application.customer_id] = {
        "customer_id": application.customer_id,
        "age": application.age,
        "income": application.income,
        "decision": decision
    }

    return {
        "message": "Application submit jhale",
        "customer_id": application.customer_id,
        "decision": decision
    }

# 2. GET request ne save kelela data paha
@app.get("/applications/{customer_id}")
def get_application(customer_id: int):
    # Jar customer_id database madhe asel, tar purna data dakhva
    if customer_id in applications_db:
        return applications_db[customer_id]
    else:
        return {"error": "Ha customer id sapadla nahi"}