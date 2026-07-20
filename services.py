from fastapi import HTTPException, status
from schemas import Student, StudentCreate

students: list[Student] = []
next_id = 1


def find_student_index(student_id: int):
    for index, student in enumerate(students):
        if student.id == student_id:
            return index

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Student not found"
    )


def create_student(student: StudentCreate):
    global next_id

    new_student = Student(
        id=next_id,
        name=student.name,
        age=student.age,
        course=student.course,
        cgpa=student.cgpa,
    )

    students.append(new_student)
    next_id += 1

    return new_student