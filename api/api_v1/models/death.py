from sqlalchemy import Column, Integer, BigInteger, Date, TIMESTAMP

from api import db
from api.api_v1.models.concept import Concept


class Death(db.Model):
    __tablename__ = 'death'
    __table_args__ = {'schema': 'de'}

    person_id = Column(BigInteger, primary_key=True)
    death_date = Column(Date)
    death_datetime = Column(TIMESTAMP)
    death_type_concept_id = Column(Integer)
    cause_concept_id = Column(BigInteger)
    cause_source_value = Column(Integer)
    cause_source_concept_id = Column(BigInteger)

    def as_dict(self):
        r = {}
        for c in self.__table__.columns:
            if c.name.endswith('concept_id'):
                concept = db.session.query(Concept).filter_by(concept_id=getattr(self, c.name)).first()
                if concept:
                    r[c.name[:-2] + 'name'] = concept.concept_name
            r[c.name] = getattr(self, c.name)
        return r
