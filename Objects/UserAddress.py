import json

from sqlalchemy import Column, ForeignKey, Integer, String, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy_repr import RepresentableBase

from Objects.UserInfo import UserInfo
from Utility.json_encoder import json_encoder

Base = declarative_base(cls=RepresentableBase)


class UserAddress(Base):
    __tablename__ = 'user_address'
    __table_args__ = {"schema": "listening_ear"}

    user_address_id = Column(Integer, primary_key=True)
    user_info_id = Column(Integer, ForeignKey(UserInfo.user_info_id))
    user_address_type = Column(String(20))
    user_flat_number_name = Column(String(20))
    user_flat_address = Column(String(50))
    user_flat_landmark = Column(String(50))
    user_city = Column(String(50))
    user_po = Column(String(50))
    user_zip_code = Column(String(20))
    user_country = Column(String(50))
    created_on = Column(Date)
    created_by = Column(String(50))
    modified_on = Column(Date)
    modified_by = Column(String(50))
    deleted_on = Column(Date)
    deleted_by = Column(String(50))
    is_active = Column(Boolean)

    user_info = relationship('user_info', back_populates='user_address')

def create(session, user_info_id, user_address_type, user_flat_number_name, user_flat_address, user_flat_landmark, user_city, user_po, user_zip_code, user_country, created_on, created_by, modified_on, modified_by, deleted_on, deleted_by, is_active):
    entry = UserAddress(user_info_id=user_info_id, user_address_type=user_address_type, user_flat_number_name=user_flat_number_name, user_flat_address=user_flat_address, user_flat_landmark=user_flat_landmark, user_city=user_city, user_po=user_po, user_zip_code=user_zip_code, user_country=user_country, created_on=created_on, created_by=created_by, modified_on=modified_on, modified_by=modified_by, deleted_on=deleted_on, deleted_by=deleted_by, is_active=is_active)
    session.add(entry)
    session.commit()

def get(session, user_address_id):
    first = session.query(UserAddress).filter(user_address_id=user_address_id).first()
    return json.dumps(first, cls=json_encoder)
