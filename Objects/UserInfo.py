import json

from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_repr import RepresentableBase

from Objects.UserType import UserType
from Objects.LoginUser import LoginUser
from Utility.json_encoder import json_encoder

Base = declarative_base(cls=RepresentableBase)


class UserInfo(Base):
    __tablename__ = 'user_info'
    __table_args__ = {"schema": "listening_ear"}

    user_info_id = Column(Integer, primary_key=True)
    user_type_id = Column(Integer, ForeignKey(UserType.user_type_id))
    login_user_id = Column(Integer, ForeignKey(LoginUser.login_user_id))
    user_first_name = Column(String(20))
    user_middle_name = Column(String(20))
    user_last_name = Column(String(20))
    user_mail_id = Column(String(20))
    created_on = Column(Date)
    created_by = Column(String(50))
    modified_on = Column(Date)
    modified_by = Column(String(50))
    deleted_on = Column(Date)
    deleted_by = Column(String(50))
    is_active = Column(Boolean)

    user_type = relationship('UserType', backref='user_info')
    login_user = relationship('login_user', backref='user_info')


def create(session, user_type_id, login_user_id, user_first_name, user_middle_name, user_last_name,user_mail_id, created_on, created_by, modified_on, modified_by, deleted_on, deleted_by, is_active):
    entry = UserInfo(user_type_id=user_type_id, login_user_id=login_user_id, user_first_name=user_first_name, user_middle_name=user_middle_name, user_last_name=user_last_name, user_mail_id=user_mail_id, created_on=created_on, created_by=created_by, modified_on=modified_on, modified_by=modified_by, deleted_on=deleted_on, deleted_by=deleted_by, is_active=is_active)
    session.add(entry)
    session.commit()


def get(session, user_info_id):
    first = session.query(UserInfo).filter(user_info_id=user_info_id).first()
    return json.dumps(first, cls=json_encoder)
