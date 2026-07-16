from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from pydantic import BaseModel

app = FastAPI()


class StudentCreate(BaseModel):
    name: str
    age: int
    course: str
    cgpa: float


class Student(BaseModel):
    id : int
    name: str
    age: int
    course: str
    cgpa: float

students = []
next_id = 1


def find_student_index(student_id: int):
    for index, student in enumerate(students):
        if(student.id == student_id):
            return index
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Student not found"
    )


@app.post("/students", response_model=Student, status_code=status.HTTP_201_CREATED)
def create_student(student: StudentCreate):
    global next_id
    new_student = Student(
        id=next_id,
        name=student.name,
        age=student.age,
        course=student.course,
        cgpa=student.cgpa
    )
    next_id+=1
    students.append(new_student)
    return new_student


@app.get("/students", response_model=list[Student], status_code=status.HTTP_200_OK)
def get_students():
    return students


@app.get("/students/{student_id}", response_model=Student, status_code=status.HTTP_200_OK)
def get_student(student_id: int):
    index = find_student_index(student_id)
    return students[index]
        

@app.put("/students/{student_id}", response_model=Student, status_code=status.HTTP_200_OK)
def update_student(student_id: int, updated_student:StudentCreate):
    index = find_student_index(student_id)
    students[index].name = updated_student.name
    students[index].age = updated_student.age
    students[index].course = updated_student.course
    students[index].cgpa = updated_student.cgpa
    return students[index]


@app.delete("/students/{student_id}", status_code=status.HTTP_200_OK)
def delete_student(student_id: int):
    index = find_student_index(student_id)
    del students[index]
    return{
        "message" : "Student Deleted Successfully!"
    }



@app.get("/students/filter", response_model=list[Student])
def filter_students(course: str, cgpa: float):
    filtered_students = []
    for student in students:
        if (
            student.course.lower() == course.lower()
            and student.cgpa == cgpa
        ):
            filtered_students.append(student)
    return filtered_students




# # python3 -m uvicorn main:app --reload (to reload the site everytime something is changed)