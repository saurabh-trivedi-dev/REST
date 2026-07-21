from fastapi import FastAPI
from routers.students import router as student_router

app = FastAPI()

app.include_router(student_router)




# python3 -m uvicorn main:app --reload


# REST/
# │
# ├── main.py
# ├── schemas.py
# ├── services.py
# ├── database.py
# │
# ├── models.py
# │
# └── routers/
#     ├── students.py
#     ├── auth.py
#     └── chat.py