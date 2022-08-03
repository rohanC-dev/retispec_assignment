import datetime

from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware
from database import db_session
from model import PatientTable

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/patient")  # create a new patient
def create_patient(firstname: str, lastname: str, dob: datetime.date, sex: str):
    patient = PatientTable()
    patient.firstname = firstname
    patient.lastname = lastname
    patient.date_of_birth = dob
    patient.sex = sex

    db_session.add(patient)
    db_session.commit()
    return {"Success": True}

@app.get("/patient/{patient_id}")  # get patient by id
def read_patient(patient_id: int):
    patient = db_session.query(PatientTable).filter(PatientTable.id == patient_id).first()

    if not patient:
        return {"Success": False,
                "Reason": "Patient Not Found"}

    return patient


@app.get("/patient/")  # get patient by first and last name
def read_patient(firstname: str, lastname: str):
    return db_session.query(PatientTable).filter(PatientTable.firstname == firstname, PatientTable.lastname == lastname).first()

@app.delete("/patient/{patient_id}")  # delete a patient
def delete_patient(patient_id: int):
    patient = db_session.query(PatientTable).filter(PatientTable.id == patient_id).first()

    if not patient:
        return {"Success": False,
                "Reason": "Patient Not Found"}

    db_session.delete(patient)
    db_session.commit()
    return {"Success": True}

