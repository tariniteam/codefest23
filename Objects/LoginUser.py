import json

from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean

from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_repr import RepresentableBase

from Objects.UserType import UserType
from Objects.LoginBasedDocType import LoginBasedDocType
from Utility.json_encoder import json_encoder

Base = declarative_base(cls=RepresentableBase)


class LoginUser(Base):
    __tablename__ = 'login_user'
    __table_args__ = {"schema": "listening_ear"}

    login_user_id = Column(Integer, primary_key=True, autoincrement=True)
    login_user_name = Column(String(20))
    login_user_type_id = Column(Integer, ForeignKey(UserType.user_type_id))
    login_based_doc_type_id = Column(Integer, ForeignKey(LoginBasedDocType.login_based_doc_type_id))
    login_based_doc_type_number = Column(String(20))
    user_dob = Column(Date)
    user_password = Column(String(20))
    created_on = Column(Date)
    created_by = Column(String(50))
    modified_on = Column(Date)
    modified_by = Column(String(50))
    deleted_on = Column(Date)
    deleted_by = Column(String(50))
    is_active = Column(Boolean)

    user_type = relationship('UserType', backref='login_user')
    login_user_type = relationship('login_based_doc_type', backref='login_user')


def create(session, login_user_name, login_user_type_id, login_based_doc_type_id , login_based_doc_type_number, user_dob, user_password, created_on, created_by, modified_on, modified_by, deleted_on, deleted_by, is_active):
    entry = LoginUser(login_user_name=login_user_name, login_user_type_id=login_user_type_id, login_based_doc_type_id=login_based_doc_type_id, login_based_doc_type_number=login_based_doc_type_number, user_dob=user_dob, user_password=user_password, created_on=created_on, created_by=created_by, modified_on=modified_on, modified_by=modified_by, deleted_on=deleted_on, deleted_by=deleted_by, is_active=is_active)
    session.add(entry)
    session.commit()


def get(session, login_user_id):
    first = session.query(LoginUser).filter(login_user_id=login_user_id).first()
    return json.dumps(first, cls=json_encoder)
