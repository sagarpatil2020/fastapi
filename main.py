# Importing FastAPI 
from fastapi import FastAPI
from pydantic import BaseModel

# Creating an instance of FastAPI
app = FastAPI()


# Defining a route for the root endpoint ("/")
@app.get("/")
# Function to handle requests to the root endpoint ("/")
def read_root():
    return {"Message": "Hello - World"}

@app.get("/about")
def read_about():
    return {"Message": "About - Page"}


# Path parameter - It is used for send dynamic values in the URL
@app.get("/name/{name}")
def read_name(name: str):
    return {"Message": f"Hello - {name}"}


@app.get("/items/{item_id}")
def read_items(item_id: int):
        return {"item_id": item_id}


#Query parameter - It is used for send dynamic values in the URL
@app.get("/emp/{emp_dept}")
def read_emp_dept(emp_dept: str, dept_id: int):
    return {"Message": f"Emp department - {emp_dept} - Dept ID - {dept_id}"}


@app.get("/shopping/{shopping_item}")
def read_shopping_item(shopping_item: str, shopping_company: str | None = None):
    return {"Message": f"Shopping item - {shopping_item} - Company - {shopping_company}"}


#post method - It is used for create new resources 
# In this example, we are creating a new student resource

#we use pydantic model to define the structure of the request body
class Student(BaseModel):
     name:str
     age:int

@app.post("/student")
def read_student(student: Student):
    return {"Message": f"Student - {student.name} - Age - {student.age}"}
