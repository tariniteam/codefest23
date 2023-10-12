import json

from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_repr import RepresentableBase
from sqlalchemy.orm import relationship

from Objects.LoginUser import LoginUser
from Objects.SupportEnabledCondition import SupportEnabledCondition
from Objects.UserReferral import UserReferral

from Utility.json_encoder import json_encoder

Base = declarative_base(cls=RepresentableBase)


class ReferralStatus(Base):
    __tablename__ = 'referral_status'
    __table_args__ = {"schema": "listening_ear"}

    referral_status_id = Column(Integer, primary_key=True)
    user_referral_id = Column(Integer, ForeignKey(UserReferral.user_referral_id))
    assesment_type = Column(String(20))
    workflow_changed_by = Column(Integer, ForeignKey(LoginUser.login_user_id))
    created_on = Column(Date)
    created_by = Column(String(50))
    modified_on = Column(Date)
    modified_by = Column(String(50))
    deleted_on = Column(Date)
    deleted_by = Column(String(50))
    is_active = Column(Boolean)

    login_user = relationship('login_user', backref='referral_status')
    user_referral = relationship('user_referral', backref='referral_status')


def get(session, referral_status_id):
    first = session.query(ReferralStatus).filter(referral_status_id == referral_status_id).first()
    return json.dumps(first, cls=json_encoder)
