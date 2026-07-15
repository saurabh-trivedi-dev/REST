from fastapi import FastAPI
from fastapi import HTTPException
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


@app.get("/students/filter")
def filter_students(course: str, cgpa: float):
    filtered_students = []
    for student in students:
        if (
            student.course.lower() == course.lower()
            and student.cgpa == cgpa
        ):
            filtered_students.append(student)
    return filtered_students


@app.get("/students/{name}")
def get_student(name: str):

    for student in students:
        if student.name.lower() == name.lower():
            return student
    
    raise HTTPException(status_code=404, detail="Student not found")


@app.put("/students/{name}")
def update_student(name: str, updated_student:Student):
    for index, student in enumerate(students):
        if(student.name.lower() == name.lower()):
            updated_student.name = student.name
            students[index] = updated_student
            return {
                "message" : "Student Found!!",
                "student" : updated_student
            }
    raise HTTPException(status_code=404, detail="Student is not in the records!")


@app.delete("/students/{name}")
def delete_student(name: str):
    for index, student in enumerate(students):
        if student.name.lower() == name.lower():
            del students[index]
            return {
                "message" : "Student Deleted Successfully!"
            }
    raise HTTPException(status_code=404, detail="Student is not in the records!")


# python3 -m uvicorn main:app --reload (to reload the site everytime something is changed)