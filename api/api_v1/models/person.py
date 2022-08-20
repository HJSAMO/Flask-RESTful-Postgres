from sqlalchemy import Column, Integer, BigInteger, String, DateTime

from api import db
from api.api_v1.models.concept import Concept


class Person(db.Model):
    __tablename__ = 'person'
    __table_args__ = {'schema': 'de'}

    person_id = Column(BigInteger, primary_key=True)
    gender_concept_id = Column(Integer)
    year_of_birth = Column(Integer)
    month_of_birth = Column(Integer)
    day_of_birth = Column(Integer)
    birth_datetime = Column(DateTime)
    race_concept_id = Column(Integer)
    ethnicity_concept_id = Column(Integer)
    location_id = Column(BigInteger)
    provider_id = Column(BigInteger)
    care_site_id = Column(BigInteger)
    person_source_value = Column(String(50))
    gender_source_value = Column(String(50))
    gender_source_concept_id = Column(Integer)
    race_source_value = Column(String(50))
    race_source_concept_id = Column(Integer)
    ethnicity_source_value = Column(String(50))
    ethnicity_source_concept_id = Column(Integer)

    def as_dict(self):
        r = {}
        for c in self.__table__.columns:
            if c.name.endswith('concept_id'):
                concept = db.session.query(Concept).filter_by(concept_id=getattr(self, c.name)).first()
                if concept:
                    r[c.name[:-2] + 'name'] = concept.concept_name
            r[c.name] = getattr(self, c.name)
        return r
