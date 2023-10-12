from sqlalchemy import Column, ForeignKey, Integer, String, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy_repr import RepresentableBase

from Objects.UserInfo import UserInfo
from Objects.UserReferral import UserReferral

Base = declarative_base(cls=RepresentableBase)


class UserGPSurgeryDetail(Base):
    __tablename__ = 'user_gp_surgery_detail'
    __table_args__ = {"schema": "listening_ear"}

    user_gp_surgery_detail_id = Column(Integer, primary_key=True)
    user_info_id = Column(Integer, ForeignKey(UserInfo.user_info_id))
    user_referral_id = Column(Integer, ForeignKey(UserReferral.user_referral_id))
    user_gp_surgery_name = Column(String(20))
    user_gp_surgery_nhs_number = Column(String(50))
    user_gp_surgery_address = Column(String)
    user_gp_surgery_city = Column(String(50))
    user_gp_surgery_po = Column(String(50))
    user_gp_surgery_country = Column(String(50))
    created_on = Column(Date)
    created_by = Column(String(50))
    modified_on = Column(Date)
    modified_by = Column(String(50))
    deleted_on = Column(Date)
    deleted_by = Column(String(50))
    is_active = Column(Boolean)

    user_info = relationship('user_info', back_populates='user_gp_surgery_detail')

def create(session, user_info_id, user_referral_id, user_gp_surgery_name, user_gp_surgery_nhs_number, user_gp_surgery_address, user_gp_surgery_city, user_gp_surgery_po, user_gp_surgery_country, created_on, created_by, modified_on, modified_by, deleted_on, deleted_by, is_active):
    entry = UserGPSurgeryDetail(user_info_id=user_info_id, user_referral_id=user_referral_id, user_gp_surgery_name=user_gp_surgery_name, user_gp_surgery_nhs_number=user_gp_surgery_nhs_number, user_gp_surgery_address=user_gp_surgery_address, user_gp_surgery_city=user_gp_surgery_city, user_gp_surgery_po=user_gp_surgery_po, user_gp_surgery_country=user_gp_surgery_country, created_on=created_on, created_by=created_by, modified_on=modified_on, modified_by=modified_by, deleted_on=deleted_on, deleted_by=deleted_by, is_active=is_active)
    session.add(entry)
    session.commit()

def get(session, user_gp_surgery_detail_id):
    first = session.query(UserGPSurgeryDetail).filter(user_gp_surgery_detail_id=user_gp_surgery_detail_id).first()
    return first
