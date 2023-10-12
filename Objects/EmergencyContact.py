from sqlalchemy import Column, ForeignKey, Integer, String, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy_repr import RepresentableBase

from Objects.UserInfo import UserInfo

Base = declarative_base(cls=RepresentableBase)


class EmergencyContact(Base):
    __tablename__ = 'emergency_contact'
    __table_args__ = {"schema": "listening_ear"}

    user_emergency_contact_id = Column(Integer,primary_key=True)
    user_info_id = Column(Integer, ForeignKey(UserInfo.user_info_id))
    user_emergency_contact_name = Column(String(50))
    user_emergency_contact_address = Column(String)
    user_emergency_contact_phone = Column(String(20))
    user_emergency_contact_email = Column(String(20))
    created_on = Column(Date)
    created_by = Column(String(50))
    modified_on = Column(Date)
    modified_by = Column(String(50))
    deleted_on = Column(Date)
    deleted_by = Column(String(50))
    is_active = Column(Boolean)

    user_info = relationship('user_info', back_populates='emergency_contact')
    

def create(session, user_info_id, user_emergency_contact_name, user_emergency_contact_address, user_emergency_contact_phone, user_emergency_contact_email, created_on, created_by, modified_on, modified_by, deleted_on, deleted_by, is_active):
    entry = EmergencyContact(user_info_id=user_info_id, user_emergency_contact_name=user_emergency_contact_name, user_emergency_contact_address=user_emergency_contact_address, user_emergency_contact_phone=user_emergency_contact_phone, user_emergency_contact_email=user_emergency_contact_email, created_on=created_on, created_by=created_by, modified_on=modified_on, modified_by=modified_by, deleted_on=deleted_on, deleted_by=deleted_by, is_active=is_active)
    session.add(entry)
    session.commit()

def get(session, user_emergency_contact_id):
    first = session.query(EmergencyContact).filter(user_emergency_contact_id=user_emergency_contact_id).first()
    return first
