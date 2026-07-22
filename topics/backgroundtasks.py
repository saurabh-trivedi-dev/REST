
from fastapi import FastAPI, BackgroundTasks

app = FastAPI()


def send_email():
    print("Email Sent")

@app.post("/register")
def register(background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email)
    return{
        "message": "User Registered"
    }



def send_email(email: str):
    print(f"Email sent to {email}")

@app.post("/register")
def register(background_tasks: BackgroundTasks):
    background_tasks.add_task(
        send_email,
        "saurabh@gmail.com"
    )
    return {"message": "Registered"}