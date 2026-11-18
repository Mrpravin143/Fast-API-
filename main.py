from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Its my first FastAPI application! is working fine."}


@app.get("/about")
def read_about():
    return {"message": "This is the about page of my FastAPI application.", "status": "success","version": "1.0.0", "status_code": 200}

@app.get("/customers")
def read_customers(customer_id: int):
    return {"customer_id": customer_id, "Name": "John Doe", "Email": "john.doe@example.com", "Phone": "+1-555-123-4567", "Address": "123 Main St, Anytown, USA", "status": "success", "version": "1.0.0", "status_code": 200}





