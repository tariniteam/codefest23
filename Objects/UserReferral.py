import json

from sqlalchemy import Column, ForeignKey, Integer, String, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy_repr import RepresentableBase
from Objects.LoginUser import LoginUser
from Utility.json_encoder import json_encoder

Base = declarative_base(cls=RepresentableBase)


class UserReferral(Base):
    __tablename__ = 'user_referral'
    __table_args__ = {"schema": "listening_ear"}

    user_referral_id = Column(Integer, primary_key=True)
    login_user_id = Column(Integer, ForeignKey(LoginUser.login_user_id))
    created_on = Column(Date)
    created_by = Column(String(50))
    modified_on = Column(Date)
    modified_by = Column(String(50))
    deleted_on = Column(Date)
    deleted_by = Column(String(50))
    is_active = Column(Boolean)

    login_user = relationship('login_user', back_populates='user_referral')


def create(session, login_user_id, created_on, created_by, modified_on, modified_by, deleted_on, deleted_by, is_active):
    entry = UserReferral(login_user_id=login_user_id, created_on=created_on, created_by=created_by, modified_on=modified_on, modified_by=modified_by, deleted_on=deleted_on, deleted_by=deleted_by, is_active=is_active)
    session.add(entry)
    session.commit()


def get(session, user_referral_id):
    first = session.query(UserReferral).filter(user_referral_id=user_referral_id).first()
    return json.dumps(first, cls=json_encoder)
