# Dependency : A function that FastAPI automatically calls before your endpoint.

from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()

def greet():
    print("Running Dependency")

@app.get("/")
def home(x = Depends(greet)):
    print("Running Endpoint")
    return {"message": "Hello"}


def get_name():
    return "Saurabh"

@app.get("/name")
def name(name = Depends(get_name)):
    print("Running /name Endpoint")
    return {
        "message": f"Hello {name}"
    }


def multiply():
    return 5 * 10

@app.get("/multiply")
def multiply(value = Depends(multiply)):
    return {
        "result": value + 20
    }


def get_age():
    print("Getting age...")
    return 22

@app.get("/age")
def age(age = Depends(get_age)):
    print("Inside endpoint")
    return {
        "age_after_10_years": age + 10
    }



def verify_user():
    token = "abc123"

    if token != "secret":
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )


@app.get("/user")
def user(user = Depends(verify_user)):
    return {"message" : "User Found!!"}



def verify():
    raise HTTPException(
        status_code=401,
        detail="Not Authorized"
    )


@app.get("/verify")
def verify(user = Depends(verify)):
    print("Inside endpoint")
    return {
        "message": "Hello"
    }


def check():
    print("Checking...")

    raise HTTPException(
        status_code=401,
        detail="Unauthorized User On Checking"
    )

@app.get("/check")
def check(x = Depends(check)):
    print("Inside Home")
    return {
        "message": "Hello"
    }



def verify_user():
    raise HTTPException(
        status_code=401,
        detail="Unauthorized User and DB"
    )

# def verify_user():
#     print("Verifying User...")

def get_db():
    print("Connecting Database...")

@app.get("/verifyuserdb")
def verifyuserdb(
    user = Depends(verify_user),
    db = Depends(get_db)
):
    print("Inside Home")
    return {
        "message": "Hello"
    }


@app.get("/underscore")
def underscore(_ = Depends(verify_user)):
    return {"message" : "Hi"}