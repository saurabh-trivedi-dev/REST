
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator, computed_field
from typing import List, Dict, Optional, Annotated

app = FastAPI()


class Office(BaseModel):
    zipcode: str
    city: str
    state: str


class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, title="Name of the patient", description="Give the name of the patient in less than 50 chars", examples=['Nitish', 'Saurabh'])]
    age: int = Field(gt=0, lt=120)
    height : float
    weight: Annotated[float, Field(gt=0, strict=True)]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    married: Annotated[bool, Field(default=None, description="Is the person married or not")]
    contact_details: Optional[Dict[str, str]] = None
    email: Optional[EmailStr] = None
    linkedin_url: Optional[AnyUrl] = None
    office: Office


    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['hdfc.com', 'icici.com']
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError("Not a valid email")
        return value


    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()


    @field_validator('age', mode='after')
    @classmethod
    def age_validator(cls, value):
        if 0< value <100:
            return value
        else:
            raise ValueError("Age is not valid")


    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age>60 and 'emergency' not in model.contact_details:
            raise ValueError("Emergency Contact Not Given")
        return model


    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2), 2)
        return bmi


def insert_patient(patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)

    print(patient.office.city)

    print(patient.bmi)

    if patient.married == None:
        print("Still Virgin")
    else:
        print(patient.married)

    for allergy in patient.allergies:
        print(allergy)

    print(patient.contact_details)
    
    print("Data Inserted!")


office_address = {'zipcode':'340', 'city':"Unnao", 'state':"UP"}
address1 = Office(**office_address)


patient_info = {'name':'Saurabh', 'office':address1, 'email':'saurabh@hdfc.com', 'age':67, 'weight':76.6, 'height':1.75, 'allergies':['pollen', 'dust'], 'contact_details':{"address":"46, Adarsh Nagar", 'emergency':"saurabh@gmail.com"}}
patient1 = Patient(**patient_info)

insert_patient(patient1)

temp_dict = patient1.model_dump()
temp_dict_include = patient1.model_dump(include=['name', 'age'])
temp_dict_exclude = patient1.model_dump(exclude=['weight'])
temp_json = patient1.model_dump_json()

print(temp_dict)
print(temp_dict_include)
print(temp_dict_exclude)
print(temp_json)



