# GET /students


# GET /students HTTP/1.1

# Host: localhost:8000
# User-Agent: Chrome
# Accept: application/json
# Authorization: Bearer abc123

# # Everything below the first line is called a Header.


# # Headers usually contain metadata about the request, not the main data itself.



# POST /students/15?active=true

# Authorization: Bearer abc123

# {
#     "name": "Saurabh",
#     "age": 22
# }


# Location	Example
# Path	/students/15
# Query	?active=true
# Header	Authorization: Bearer abc123
# Body	{"name":"Saurabh"}



from typing import Optional
from fastapi import Header, FastAPI

app = FastAPI()


@app.get("/")
def home(language: str = Header()):
    return {
        "language": language
    }
    

@app.get("/")
def home(
    language: Optional[str] = Header(None)
):
    return {
        "language": language
    }



@app.get("/")
def home(
    country: str = Header("India")
):
    return {
        "country": country
    }