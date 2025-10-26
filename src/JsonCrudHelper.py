import json
from Patient import Patient

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
    
    def write_patient(self, patient: Patient):
        if patient.id is None or patient.id.strip() == "":
            return {"Error": "Invalid Patient ID"}
        else:
            patient.id = patient.id.strip().upper()
        
        patients = self.read_all_patients()        
        if patient.id in patients:
            response = {"Error": "Patient ID already exists"}
        else:
            patients[patient.id] = {
                "name": patient.name,
                "city": patient.city,
                "gender": patient.gender,
                "age": patient.age,
                "height": patient.height,
                "weight": patient.weight,
                "bmi": patient.bmi,
                "verdict": patient.verdict
            } 
            response = self.write_json(patients)

        return response    
                   
    def update_patient(self, patient: Patient):
        if Patient is None or patient.id is None or patient.id.strip() == "":
            return {"Error": "Invalid Patient ID"}
        else:
            patient.id = patient.id.strip().upper()

        patients = self.read_all_patients()
        if patient.id in patients:
            patients[patient.id] = {
                "name": patient.name,
                "city": patient.city,
                "gender": patient.gender,
                "age": patient.age,
                "height": patient.height,
                "weight": patient.weight,
                "bmi": patient.bmi,
                "verdict": patient.verdict
            }
            response = self.write_json(patients)
        else:
            response = {"Error": "Patient not found"}

        return response