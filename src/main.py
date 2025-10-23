from fastapi import FastAPI
from CrudHelper import CrudHelper

app = FastAPI()

helper = CrudHelper()

@app.get("/")
async def hello():
    return {"Message": "Patient Management System API."}

@app.get("/about")
async def about():
    return {"Info": "This API manages patient records and appointments."}

@app.get("/view")
async def get_patients():
    patients = helper.read_json()
    return patients