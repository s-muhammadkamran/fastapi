from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal

class Patient(BaseModel):
    id: Annotated[str, Field(..., description='Patient ID', examples=['P031', "P032"])]
    
    name: Annotated[str, Field(..., description='Patient Name', examples=["Ahmed Salama"])]
    
    city: Annotated[str, Field(..., description="City where the patient is living", examples=["Jeddah", "Makkah", "Riyadh"])]
    
    age: Annotated[int, Field(..., description="Age of the patient", examples=[30, 50], gt=0, lt=120)]
    
    gender: Annotated[Literal['Male', 'Female', 'Others'], Field(..., description="Gender of the patient", examples=["Male", "Female", "Others"])]
    
    height: Annotated[float, Field(..., description="Height in cm", examples=[165, 174], gt=30, lt=300)]
    
    weight: Annotated[float, Field(..., description="Weight in kgs", examples=[89, 79] ,gt=1, lt=500)]
    
    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / ((self.height / 100) ** 2), 2)
    
    @computed_field
    @property
    def verdict(self) -> str:
        bmi_value = self.bmi
        if bmi_value < 18.5:
            return "Underweight"
        elif 18.5 <= bmi_value < 24.9:
            return "Normal"
        elif 25.0 <= bmi_value < 29.9:
            return "Overweight"
        else:
            return "Obese"