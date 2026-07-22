

from fastapi import FastAPI, UploadFile, File

app = FastAPI()


@app.post("/")
def upload(file: UploadFile = File()):

    content = file.file.read()

    return{
        "size": len(content)
    }


app.post("/upload")
def upload(files: list[UploadFile] = File()):

    return {
        "count": len(files)
    }


@app.post("/upload")
def upload(file: UploadFile = File()):

    with open(file.filename, "wb") as f:
        f.write(file.file.read())

    return {"message": "Uploaded"}





# Static Files

# Static files are files that are served as they are, without processing.

# Examples:

# Images (.png, .jpg)
# CSS
# JavaScript
# PDFs
# Fonts


from fastapi.staticfiles import StaticFiles

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)