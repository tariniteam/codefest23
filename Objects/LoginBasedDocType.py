from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_repr import RepresentableBase

Base = declarative_base(cls=RepresentableBase)


class LoginBasedDocType(Base):
    __tablename__ = 'login_based_doc_type'
    __table_args__ = {"schema": "listening_ear"}

    login_based_doc_type_id = Column(Integer, primary_key=True, autoincrement=True)
    login_based_doc_type = Column(String(50))
    created_on = Column(Date)
    created_by = Column(String(50))
    modified_on = Column(Date)
    modified_by = Column(String(50))
    deleted_on = Column(Date)
    deleted_by = Column(String(50))
    is_active = Column(Boolean)


def create(session, login_based_doc_type, created_on, created_by, modified_on, modified_by, deleted_on, deleted_by, is_active):
    entry = LoginBasedDocType(login_based_doc_type=login_based_doc_type, created_on=created_on, created_by=created_by, modified_on=modified_on, modified_by=modified_by, deleted_on=deleted_on, deleted_by=deleted_by, is_active=is_active)
    session.add(entry)
    session.commit()


def get(session, login_based_doc_type_id):
    first: LoginBasedDocType = session.query(LoginBasedDocType).filter(login_based_doc_type_id == login_based_doc_type_id).first()
    return first
