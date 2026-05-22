from fastapi import FastAPI

app = FastAPI()

employee_database = [
    {"id": 1, "name": "Alice Vance", "role": "Senior Developer", "department": "Engineering"},
    {"id": 2, "name": "Julian Thorne", "role": "Data Analyst", "department": "Analytics"}
]


@app.get("/")
def home_page():
    return {"message": "Welcome to the Company Internal Employee Management API system!"}

@app.get("/employees")
def get_all_employees():
    return employee_database