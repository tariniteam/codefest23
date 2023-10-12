import json

from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_repr import RepresentableBase
from sqlalchemy.orm import relationship

from Objects.SupportEnabledCondition import SupportEnabledCondition
from Objects.UserReferral import UserReferral

from Utility.json_encoder import json_encoder

Base = declarative_base(cls=RepresentableBase)


class UserSupportCondition(Base):
    __tablename__ = 'user_support_condition'
    __table_args__ = {"schema": "listening_ear"}

    user_support_enabled_id = Column(Integer, primary_key=True)
    user_referral_id = Column(Integer, ForeignKey(UserReferral.user_referral_id))
    support_enabled_condition_id = Column(Integer, ForeignKey(SupportEnabledCondition.support_enabled_condition_id))
    file_name_creation_id = Column(String(50))
    created_on = Column(Date)
    created_by = Column(String(50))
    modified_on = Column(Date)
    modified_by = Column(String(50))
    deleted_on = Column(Date)
    deleted_by = Column(String(50))
    is_active = Column(Boolean)

    user_referral = relationship('user_referral', backref='user_support_condition')
    support_enabled_condition = relationship('support_enabled_condition', backref='user_support_condition')


def get(session, user_support_enabled_id):
    first = session.query(UserSupportCondition).filter(user_support_enabled_id == user_support_enabled_id).first()
    return json.dumps(first, cls=json_encoder)
