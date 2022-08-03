from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from database import Base

class PatientTable(Base):
    __tablename__ = 'patient'
    id = Column(Integer, primary_key=True)
    firstname = Column(String(30), nullable=False)
    lastname = Column(String(30), nullable=False)
    date_of_birth = Column(Date, nullable=False) #
    sex = Column(String(30), nullable=False)
    children = relationship("AcquisitionTable")


class AcquisitionTable(Base):
    __tablename__ = 'acquisition'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey("patient.id"))
    eye_type = Column(String(30), nullable=False)
    site_name = Column(String(30), nullable=False)
    date_taken = Column(Date, nullable=False) #
    operator_name = Column(String(30), nullable=False)