import json

from sqlalchemy import Column, ForeignKey, Integer, String, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy_repr import RepresentableBase

from Objects.UserInfo import UserInfo
from Objects.UserReferral import UserReferral
from Utility.json_encoder import json_encoder

Base = declarative_base(cls=RepresentableBase)


class UserQuestionaries(Base):
    __tablename__ = 'user_questionaries'
    __table_args__ = {"schema": "listening_ear"}

    user_questionaries_id = Column(Integer, primary_key=True)
    user_info_id = Column(Integer, ForeignKey(UserInfo.user_info_id))
    user_referral_id = Column(Integer, ForeignKey(UserReferral.user_referral_id))
    age_under_17 = Column(Boolean)
    employment_status = Column(String(50))
    employement_status_other = Column(String(50))
    any_impairment_health_condtn_learning_difference = Column(String(20))
    received_therapy_in_past = Column(Boolean)
    received_other_psychological_service = Column(Boolean)
    mental_health_condition = Column(Boolean)
    ever_received_mental_health_assessment = Column(Boolean)
    ever_try_to_harm_yourseft = Column(Boolean)
    currently_on_medication_for_psychological_problems = Column(Boolean)
    any_traumatic_experiences_still_affecting_now = Column(Boolean)
    are_there_any_other_professionals_working_with_you = Column(Boolean)
    your_difficulties = Column(String)
    how_long_you_have_been_in_problems = Column(Integer)
    are_you_referring_for_bereavement_support = Column(Boolean)
    date_of_the_most_recent_bereavement = Column(Date)
    your_main_difficulty = Column(String(50))
    any_legal_or_court_cases_pending = Column(Boolean)
    armed_force_or_depended_armed_force = Column(String(50))
    require_interpreter = Column(Boolean)
    how_you_hear_abt_service = Column(String)
    created_on = Column(Date)
    created_by = Column(String(50))
    modified_on = Column(Date)
    modified_by = Column(String(50))
    deleted_on = Column(Date)
    deleted_by = Column(String(50))
    is_active = Column(Boolean)

    user_info = relationship('user_info', back_populates='user_questionaries')
    user_referral = relationship('user_referral', back_populates='user_questionaries')

def create(session, user_info_id, user_referral_id, age_under_17, employment_status, employement_status_other, any_impairment_health_condtn_learning_difference, received_therapy_in_past, received_other_psychological_service, mental_health_condition, ever_received_mental_health_assessment, ever_try_to_harm_yourseft, currently_on_medication_for_psychological_problems, any_traumatic_experiences_still_affecting_now, are_there_any_other_professionals_working_with_you, your_difficulties, how_long_you_have_been_in_problems, are_you_referring_for_bereavement_support, date_of_the_most_recent_bereavement, your_main_difficulty, any_legal_or_court_cases_pending, armed_force_or_depended_armed_force, require_interpreter, how_you_hear_abt_service, created_on, created_by, modified_on, modified_by, deleted_on, deleted_by, is_active):
    entry = UserQuestionaries(user_info_id=user_info_id, user_referral_id=user_referral_id, age_under_17=age_under_17, employment_status=employment_status, employement_status_other=employement_status_other, any_impairment_health_condtn_learning_difference=any_impairment_health_condtn_learning_difference, received_therapy_in_past=received_therapy_in_past, received_other_psychological_service=received_other_psychological_service, mental_health_condition=mental_health_condition, ever_received_mental_health_assessment=ever_received_mental_health_assessment, ever_try_to_harm_yourseft=ever_try_to_harm_yourseft, currently_on_medication_for_psychological_problems=currently_on_medication_for_psychological_problems, any_traumatic_experiences_still_affecting_now=any_traumatic_experiences_still_affecting_now, are_there_any_other_professionals_working_with_you=are_there_any_other_professionals_working_with_you, your_difficulties=your_difficulties, how_long_you_have_been_in_problems=how_long_you_have_been_in_problems, are_you_referring_for_bereavement_support=are_you_referring_for_bereavement_support, date_of_the_most_recent_bereavement=date_of_the_most_recent_bereavement, your_main_difficulty=your_main_difficulty, any_legal_or_court_cases_pending=any_legal_or_court_cases_pending, armed_force_or_depended_armed_force=armed_force_or_depended_armed_force, require_interpreter=require_interpreter, how_you_hear_abt_service=how_you_hear_abt_service, created_on=created_on, created_by=created_by, modified_on=modified_on, modified_by=modified_by, deleted_on=deleted_on, deleted_by=deleted_by, is_active=is_active)
    session.add(entry)
    session.commit()

def get(session, user_questionaries_id):
    first = session.query(UserQuestionaries).filter(user_questionaries_id=user_questionaries_id).first()
    return json.dumps(first, cls=json_encoder)
