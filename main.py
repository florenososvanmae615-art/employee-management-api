from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Company Internal Employee Management System")

class Employee(BaseModel):
    id: int
    name: str
    role: str
    department: str

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

@app.get("/employees/{employee_id}")
def get_single_employee(employee_id: int):
    for employee in employee_database:
        if employee["id"] == employee_id:
            return employee
    raise HTTPException(status_code=404, detail="Employee not found")

@app.post("/employees")
def add_new_employee(employee: Employee):
    for e in employee_database:
        if e["id"] == employee.id:
            raise HTTPException(status_code=400, detail="Employee ID already exists")
    
    new_emp_dict = employee.model_dump()
    employee_database.append(new_emp_dict)
    return {"message": "Employee added successfully!", "employee": new_emp_dict}