import json
from Patient import Patient
from PatientUpdate import PatientUpdate

class JsonCrudHelper:
    def __init__(self, file_path : str ='../data/patients.json'):
        self.file_path = file_path
        
    def read_json(self):
        try:
            with open(self.file_path , 'r') as file:
                response = json.load(file)
        except Exception as ex:
            response = {"Error": str(ex)}
        return response
    
    def write_json(self, patients: dict):
        try:
            with open(self.file_path , 'w') as file:
                json.dump(patients, file, indent=4)
            response = {"Message": "Success"}
        except Exception as ex:
            response = {"Error": str(ex)}
        return response
    
    def read_all_patients(self):
        return self.read_json()
    
    def read_patient(self, patient_id: str):
        if patient_id is None or patient_id.strip() == "":
            return {"Error": "Invalid Patient ID"}
        else:
            patient_id = patient_id.strip().upper()

        patients = self.read_all_patients()
        if patient_id in patients:
            return patients[patient_id]
        else:
            return {"Error": "Patient not found"}
    
    def add_patient(self, patient: Patient):
        if patient is None or patient.id is None or patient.id.strip() == "":
            return {"Error": "Invalid Patient ID"}
        else:
            patient.id = patient.id.strip().upper()
        
        patients_data = self.read_all_patients()        
        if patient.id in patients_data:
            response = {"Error": "Patient ID already exists"}
        else:
            patients_data[patient.id] = patient.model_dump(exclude={'id'})
            response = self.write_json(patients_data)
        return response    
                   
    def update_patient(self, patient_id: str, patient: PatientUpdate):
        if patient is None or patient_id is None or patient_id.strip() == "":
            response = {"Error": "Invalid Patient ID or No Details to update"}
        else:
            patient_id = patient_id.strip().upper()

        patients_data = self.read_all_patients()
        print(f"Updated Patient Data: {patient}")
                
        if patient_id not in patients_data:
            response = {"Error": "Patient with provided ID not found"}
        else:
            print("Inside Update")
            existing_p_info = patients_data[patient_id]
            print(f"Existing Patient Data: {existing_p_info}")
            updated_p_info = patient.model_dump(exclude_unset=True, exclude_none=True)

            for key, value in updated_p_info.items():
                existing_p_info[key] = value

            existing_p_info['id'] = patient_id
            existing_p_info = (Patient(**existing_p_info)).model_dump(exclude={'id'}) 
            patients_data[patient_id] = existing_p_info
            response = self.write_json(patients_data)

        return response
    
    def delete_patient(self, patient_id: str):
        if patient_id is None or patient_id.strip() == "":
            return {"Error": "Invalid Patient ID"}
        else:
            patient_id = patient_id.strip().upper()

        patients_data = self.read_all_patients()        
        if patient_id not in patients_data:
            response = {"Error": "Patient with provided ID not found"}
        else:
            del patients_data[patient_id]
            response = self.write_json(patients_data)
        return response