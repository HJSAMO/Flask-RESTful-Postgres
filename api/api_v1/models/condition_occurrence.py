from sqlalchemy import Column, Integer, BigInteger, String, Date, TIMESTAMP

from api import db
from api.api_v1.models.concept import Concept


class ConditionOccurrence(db.Model):
    __tablename__ = 'condition_occurrence'
    __table_args__ = {'schema': 'de'}

    condition_occurrence_id = Column(BigInteger, primary_key=True)
    person_id = Column(BigInteger)
    condition_concept_id = Column(Integer)
    condition_start_date = Column(Date)
    condition_start_datetime = Column(TIMESTAMP)
    condition_end_date = Column(Date)
    condition_end_datetime = Column(TIMESTAMP)
    condition_type_concept_id = Column(Integer)
    condition_status_concept_id = Column(Integer)
    stop_reason = Column(String(20))
    provider_id = Column(BigInteger)
    visit_occurrence_id = Column(BigInteger)
    visit_detail_id = Column(BigInteger)
    condition_source_value = Column(String(50))
    condition_source_concept_id = Column(Integer)
    condition_status_source_value = Column(String(50))

    def as_dict(self):
        r = {}
        for c in self.__table__.columns:
            if c.name.endswith('concept_id'):
                concept = db.session.query(Concept).filter_by(concept_id=getattr(self, c.name)).first()
                if concept:
                    r[c.name[:-2] + 'name'] = concept.concept_name
            r[c.name] = getattr(self, c.name)
        return r
