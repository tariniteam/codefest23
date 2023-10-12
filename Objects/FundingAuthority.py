import json

from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_repr import RepresentableBase
from Utility import json_encoder

Base = declarative_base(cls=RepresentableBase)


class FundingAuthority(Base):
    __tablename__ = 'funding_authority'
    __table_args__ = {"schema": "listening_ear"}

    funding_authority_id = Column(Integer, primary_key=True)
    funding_authority_name_or_word = Column(String(30))
    ngo_entity_name = Column(String(30))
    created_on = Column(Date)
    created_by = Column(String(50))
    modified_on = Column(Date)
    modified_by = Column(String(50))
    deleted_on = Column(Date)
    deleted_by = Column(String(50))
    is_active = Column(Boolean)


def create(session, funding_authority_name_or_word, ngo_entity_name, created_on, created_by, modified_on, modified_by, deleted_on, deleted_by, is_active):
    entry = FundingAuthority(funding_authority_name_or_word=funding_authority_name_or_word, ngo_entity_name=ngo_entity_name, created_on=created_on, created_by=created_by, modified_on=modified_on, modified_by=modified_by, deleted_on=deleted_on, deleted_by=deleted_by, is_active=is_active)
    session.add(entry)
    session.commit()


def get(session, funding_authority_id):
    first = session.query(FundingAuthority).filter(funding_authority_id=funding_authority_id).first()
    return json.dump(first, c=json_encoder)
