from fastapi import FastAPI, Path, Query, HTTPException
from fastapi.responses import JSONResponse
from JsonCrudHelper import JsonCrudHelper
from Patient import Patient

app = FastAPI()

helper = JsonCrudHelper()

@app.get("/")
async def hello():
    return {"Message": "Patient Management System API."}

@app.get("/about")
async def about():
    return {"Info": "This API manages patient records and appointments."}

@app.get("/view")
async def get_patients():
    response = helper.read_all_patients()

    if "Error" in response:
        raise HTTPException(status_code=404, detail=response["Error"])
    else:
        return response

@app.get("/view/{patient_id}")
async def get_patient_by_id(patient_id: str = Path(..., description='The ID of the patient to retrieve', example='P001')):
    response = helper.read_patient(patient_id)

    if "Error" in response:
        raise HTTPException(status_code=404, detail=response["Error"])
    else:
        return response
    
@app.get('/sort')
async def sort_patients(sort_by: str = Query(..., description='Sort on the basis of height, weight or bmi'), order: str = Query('asc', description='sort in asc or desc order')):

    valid_sort_fields = ['height', 'weight', 'bmi']
    valid_order_values = ['asc', 'desc']

    sort_by = sort_by.lower().strip()
    order = order.lower().strip()

    if sort_by not in valid_sort_fields:
        raise HTTPException(status_code=400, detail=f"Invalid sort field. Must be one of {valid_sort_fields}")
    if order not in valid_order_values:
        raise HTTPException(status_code=400, detail=f"Invalid order. Must be {valid_order_values}.")
    
    response = helper.read_all_patients()
    print(response)
    
    if "Error" in response:
        raise HTTPException(status_code=404, detail=response["Error"])
    else:
        response = sorted(response.values(), key=lambda x: x.get(sort_by, 0), reverse=(order=='desc'))
        return response
    
@app.post("/add")
async def add_patient(patient: Patient):
    response = helper.write_patient(patient)

    if "Error" in response:
        raise HTTPException(status_code=400, detail=response["Error"])
    else:
        return JSONResponse(status_code=201, content={"Message": "Patient added successfully."})
    
@app.put("/update")
async def update_patient(patient: Patient):
    response = helper.update_patient(patient)

    if "Error" in response:
        raise HTTPException(status_code=400, detail=response["Error"])
    else:
        return JSONResponse(status_code=201, content={"Message": "Patient updated successfully."})