import json

from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_repr import RepresentableBase

from Utility.json_encoder import json_encoder

Base = declarative_base(cls=RepresentableBase)


class FundingService(Base):
    __tablename__ = 'funding_service'
    __table_args__ = {"schema": "listening_ear"}

    funding_service_id = Column(Integer, primary_key=True)
    funding_service_type = Column(String(20))
    created_on = Column(Date)
    created_by = Column(String(50))
    modified_on = Column(Date)
    modified_by = Column(String(50))
    deleted_on = Column(Date)
    deleted_by = Column(String(50))
    is_active = Column(Boolean)

def create(session, funding_service_type, created_on, created_by, modified_on, modified_by, deleted_on, deleted_by, is_active):
    entry = FundingService(funding_service_type=funding_service_type, created_on=created_on, created_by=created_by, modified_on=modified_on, modified_by=modified_by, deleted_on=deleted_on, deleted_by=deleted_by, is_active=is_active)
    session.add(entry)
    session.commit()

def get(session, funding_service_id):
    first = session.query(FundingService).filter(funding_service_id=funding_service_id).first()
    return json.dumps(first, cls=json_encoder)
