# A cookie is a small piece of data that the server stores in the client's browser.

# Login
#    ↓
# Server sends cookie
#    ↓
# Browser stores it
#    ↓
# Browser automatically sends it on future requests


from fastapi import FastAPI, Cookie, Response

app = FastAPI()


@app.get("/")
def home(session_id: str = Cookie()):
    return {
        "session": session_id
    }


@app.get("/login")
def login(response: Response):
    response.set_cookie(
        key="session_id",
        value="abc123"
    )
    return {"message": "Logged in"}


@app.get("/logout")
def logout(response: Response):
    response.delete_cookie("session_id")
    return {"message": "Logged out"}


# Cookies Summary!!
# Store small data in the browser.
# Browser sends them automatically.
# Read with Cookie().
# Set with response.set_cookie().
# Delete with response.delete_cookie().
# Common in traditional web apps.
# JWT in the Authorization header is more common for REST APIs.