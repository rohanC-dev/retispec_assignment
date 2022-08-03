import datetime
import os

from fastapi import FastAPI, HTTPException, File, UploadFile
from fastapi.responses import FileResponse
from starlette.middleware.cors import CORSMiddleware
from database import db_session
from model import PatientTable, AcquisitionTable
from sqlalchemy import desc

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/acquisition") # creating a new acquisition
async def create_acq(patient_id: int, eye_type: str, sitename: str, date_taken: datetime.date, operator_name: str, image: UploadFile = File(...)):
    acquisition = AcquisitionTable()
    acquisition.patient_id = patient_id
    acquisition.eye_type = eye_type
    acquisition.site_name = sitename
    acquisition.date_taken = date_taken
    acquisition.operator_name = operator_name

    db_session.add(acquisition)
    db_session.commit()

    acquisition_id = db_session.query(AcquisitionTable).order_by(AcquisitionTable.id.desc()).first().id

    extension = os.path.splitext(image.filename)[1]
    try:
        contents = await image.read()
        with open(image.filename, 'wb') as f:
            f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the image"}
    finally:
        await image.close()

    os.rename(image.filename, "image_" + str(acquisition_id) + str(extension))
    return {"Success": True, "message": f"Successfuly uploaded {image.filename}"}

@app.get("/acquisitions/{patient_id}") # listing all acquisitions for a particular patient
def list_acq(patient_id: int): #select * from acquisition inner join patient on acquisition.patient_id = patient.id;
    return db_session.query(AcquisitionTable).join(PatientTable).filter(AcquisitionTable.patient_id == patient_id).all()


@app.delete("/acquisition/{acquisition_id}") # deleting an acquisition
def delete_acq(acquisition_id: int):
    acquisition = db_session.query(AcquisitionTable).filter(AcquisitionTable.id == acquisition_id).first()

    if not acquisition:
        return {"Success": False,
                "Reason": "Acquisition Not Found"}

    db_session.delete(acquisition)
    db_session.commit()
    return {"Success": True}


@app.get("/acquisition/{acquisition_id}") # downloading an image
def download_img(acquisition_id: int):
    file_name = "image_" + str(acquisition_id) + ".jpg"
    file_path = "/usr/src/server/" + file_name
    return FileResponse(path=file_path, media_type='application/octet-stream', filename=file_name)