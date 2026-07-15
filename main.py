from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Student(BaseModel):
    name: str
    age: int
    course: str
    cgpa: float

students = []

@app.post("/students")
def create_student(student: Student):
    students.append(student)
    return {
        "message": "Student Created Successfully!",
        "student": student
    }


@app.get("/students")
def get_students():
    return students

@app.get("/students/{name}")
def get_student(name: str):

    for student in students:
        if student.name.lower() == name.lower():
            return student
    
    return {"error": "No Matching Student"}






# python3 -m uvicorn main:app --reload (to reload the site everytime something is changed)