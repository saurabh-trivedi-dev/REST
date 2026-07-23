
from fastapi import FastAPI, HTTPException, Path, Query
import json

app = FastAPI()


def load_data():
    with open('patients.json', 'r') as file:
        data = json.load(file)
    return data


@app.get("/")
def home():
    return {
        "message":"Patients App!"
    }


@app.get("/about")
def about():
    return{
        "message":"A web app where the doctor can keep track of their patient's details."
    }


@app.get("/view")
def view():
    data = load_data()
    return data


@app.get("/patients/{patient_id}")
def patient(patient_id: str = Path(..., description="Id of the patient", example="P001")):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient Not Found!")


@app.get("/sort")
def sort_patients(sort_by: str = Query(..., description="Choose from height, weight or bmi"), order: str = Query('asc', description="Choose between asc and desc")):
    data = load_data()

    valid_sort_fields = ['height', 'weight', 'bmi']
    valid_order_fields = ['asc', 'desc']

    sort_order = True if order=='desc' else False

    if sort_by not in valid_sort_fields:
        raise HTTPException(status_code=400, detail=f"Choose from {valid_sort_fields}")

    if order not in valid_order_fields:
        raise HTTPException(status_code=400, detail=f"Choose from {valid_order_fields}")

    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)
    return sorted_data

    

