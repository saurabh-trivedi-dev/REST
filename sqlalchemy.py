# The table becomes a class.
# Each row becomes an object of that class.
# Each column becomes an attribute of the object.

# Think of the Engine as the bridge between your Python program and the database.
# Session is what you use to perform database operations.

# Engine : Connects to the database
# Session : Used to interact with the database


# Install SQLAlchemy
# pip install sqlalchemy
# python -m pip install sqlalchemy


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///students.db")

Session = sessionmaker(bind=engine)

session = Session()

session.commit()
session.close()



from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    age: Mapped[int]

Base.metadata.create_all(bind=engine)


student = Student(
    name="Alice",
    age=20
)

session.add(student)
session.commit()


student = session.get(Student, 10)

if student is None:
    print("Student not found")
else:
    print(student.name)


student = session.get(Student, student_id)

if student is None:
    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


student = session.get(Student, 1)
student.age = 21
session.commit()


student5 = session.get(Student, 5)
if student5 is None:
    print("Student Not Found")
else:
    session.delete(student5)
    session.commit()




from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key= True)
    title: Mapped[str]
    price: Mapped[float]

Base.metadata.create_all(bind=engine)


book1 = Book(title="FastApI Book", price=499)
session.add(book1)
session.commit()


book = session.get(Book, 1)
print(book.title)
print(book.price)


book = session.get(Book, 1)
book.price = 599.0
session.commit()


book = session.get(Book, 100)
if book is None:
    print("Book not found")
else:
    book.price = 599.0
    session.commit()


book = session.get(Book, book_id)
if book is None:
    raise HTTPException(
        status_code=404,
        detail="Book not found"
    )
book.price = 599.0
session.commit()



book = session.get(Book, 1)
session.delete(book)
session.commit()


book = session.get(Book, 100)
if book is None:
    print("Book not found")
else:
    session.delete(book)
    session.commit()

