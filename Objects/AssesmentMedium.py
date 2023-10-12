import json

from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_repr import RepresentableBase

from Utility.json_encoder import json_encoder

Base = declarative_base(cls=RepresentableBase)


class AssessmentMedium(Base):
    __tablename__ = 'assesment_medium'
    __table_args__ = {"schema": "listening_ear"}

    assesment_medium_id = Column(Integer, primary_key=True)
    assesment_medium = Column(String(20))
    created_on = Column(Date)
    created_by = Column(String(50))
    modified_on = Column(Date)
    modified_by = Column(String(50))
    deleted_on = Column(Date)
    deleted_by = Column(String(50))
    is_active = Column(Boolean)


def get(session, assesment_medium_id):
    first = session.query(AssessmentMedium).filter(assesment_medium_id == assesment_medium_id).first()
    return json.dumps(first, cls=json_encoder)
