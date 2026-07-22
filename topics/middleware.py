# A middleware is code that runs before and after every request.

# Request
#    ↓
# Middleware (Before)
#    ↓
# Endpoint
#    ↓
# Middleware (After)
#    ↓
# Response

# Why use Middleware?

# Things that should happen for every request:

# Logging
# Measure request time
# CORS
# Security
# Rate limiting

# Instead of repeating code in every endpoint.



from fastapi import FastAPI, Request

app = FastAPI()


@app.middleware("http")
async def my_middleware(request: Request, call_next):
    print("Before")

    response = await call_next(request)

    print("After")

    return response

@app.get("/")
def home():
    print("Inside Home")
    return {"message": "Hello"}



from fastapi.responses import JSONResponse

@app.middleware("http")
async def test(request: Request, call_next):
    return JSONResponse(
        status_code=403,
        content={"message": "Blocked"}
    )


# Middleware Summary
# ✅ Runs for every request.
# ✅ Can execute code before and after the endpoint.
# ✅ Uses await call_next(request) to continue the request.
# ✅ Must return a Response object.
# ✅ Common uses:
# Logging
# Timing
# CORS
# Authentication (less commonly than Depends)
# Rate limiting