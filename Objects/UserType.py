import json

from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_repr import RepresentableBase
from Utility.json_encoder import json_encoder

Base = declarative_base(cls=RepresentableBase)


class UserType(Base):
    __tablename__ = 'UserType'
    __table_args__ = {"schema": "listening_ear"}

    user_type_id = Column(Integer, primary_key=True, autoincrement=True)
    user_type_name = Column(String(50))
    created_on = Column(Date)
    created_by = Column(String(50))
    modified_on = Column(Date)
    modified_by = Column(String(50))
    deleted_on = Column(Date)
    deleted_by = Column(String(50))
    is_active = Column(Boolean)


def create(session, user_type_name, created_on, created_by, modified_on, modified_by, deleted_on, deleted_by, is_active):
    user_type = UserType(user_type_name=user_type_name, created_on=created_on, created_by=created_by, modified_on=modified_on, modified_by=modified_by, deleted_on=deleted_on, deleted_by=deleted_by, is_active=is_active)
    session.add(user_type)
    session.commit()


def get(session, user_type_id):
    first = session.query(UserType).filter(user_type_id == user_type_id).first()
    return json.dumps(first, cls=json_encoder)
