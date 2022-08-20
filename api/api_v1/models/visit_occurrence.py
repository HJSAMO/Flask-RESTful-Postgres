from sqlalchemy import Column, Integer, BigInteger, String, Date, TIMESTAMP

from api import db
from api.api_v1.models.concept import Concept


class VisitOccurrence(db.Model):
    __tablename__ = 'visit_occurrence'
    __table_args__ = {'schema': 'de'}

    visit_occurrence_id = Column(BigInteger, primary_key=True)
    person_id = Column(BigInteger)
    visit_concept_id = Column(Integer)
    visit_start_date = Column(Date)
    visit_start_datetime = Column(TIMESTAMP)
    visit_end_date = Column(Date)
    visit_end_datetime = Column(TIMESTAMP)
    visit_type_concept_id = Column(Integer)
    provider_id = Column(BigInteger)
    care_site_id = Column(BigInteger)
    visit_source_value = Column(String(50))
    visit_source_concept_id = Column(Integer)
    admitted_from_source_value = Column(String(50))
    admitted_from_concept_id = Column(Integer)
    discharge_to_source_value = Column(String(50))
    discharge_to_concept_id = Column(Integer)
    preceding_visit_occurrence_id = Column(BigInteger)

    def as_dict(self):
        r = {}
        for c in self.__table__.columns:
            if c.name.endswith('concept_id'):
                concept = db.session.query(Concept).filter_by(concept_id=getattr(self, c.name)).first()
                if concept:
                    r[c.name[:-2] + 'name'] = concept.concept_name
            r[c.name] = getattr(self, c.name)
        return r
