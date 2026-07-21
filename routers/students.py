from fastapi import APIRouter, status
from schemas import Student, StudentCreate
from services import (
    students,
    create_student,
    find_student_index
)

router = APIRouter(prefix="/students")


@router.post(
    "",
    response_model=Student,
    status_code=status.HTTP_201_CREATED,
)
def add_student(student: StudentCreate):
    return create_student(student)


@router.get(
    "",
    response_model=list[Student],
    status_code=status.HTTP_200_OK,
)
def get_students():
    return students


@router.get(
    "/{student_id}",
    response_model=Student,
    status_code=status.HTTP_200_OK,
)
def get_student(student_id: int):
    index = find_student_index(student_id)
    return students[index]


@router.put(
    "/{student_id}",
    response_model=Student,
    status_code=status.HTTP_200_OK,
)
def update_student(student_id: int, updated_student: StudentCreate):
    index = find_student_index(student_id)

    students[index].name = updated_student.name
    students[index].age = updated_student.age
    students[index].course = updated_student.course
    students[index].cgpa = updated_student.cgpa

    return students[index]


@router.delete(
    "/{student_id}",
    status_code=status.HTTP_200_OK,
)
def delete_student(student_id: int):
    index = find_student_index(student_id)

    del students[index]

    return {
        "message": "Student Deleted Successfully!"
    }


@router.get(
    "/filter",
    response_model=list[Student],
)
def filter_students(course: str, cgpa: float):
    filtered_students = []

    for student in students:
        if (
            student.course.lower() == course.lower()
            and student.cgpa == cgpa
        ):
            filtered_students.append(student)

    return filtered_students