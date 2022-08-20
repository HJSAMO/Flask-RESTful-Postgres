from sqlalchemy import Column, Integer, BigInteger, String, Date, TIMESTAMP, Numeric, Text

from api import db
from api.api_v1.models.concept import Concept


class DrugExposure(db.Model):
    __tablename__ = 'drug_exposure'
    __table_args__ = {'schema': 'de'}

    drug_exposure_id = Column(BigInteger, primary_key=True)
    person_id = Column(BigInteger)
    drug_concept_id = Column(Integer)
    drug_exposure_start_date = Column(Date)
    drug_exposure_start_datetime = Column(TIMESTAMP)
    drug_exposure_end_date = Column(Date)
    drug_exposure_end_datetime = Column(TIMESTAMP)
    verbatim_end_date = Column(Date)
    drug_type_concept_id = Column(Integer)
    stop_reason = Column(String(20))
    refills = Column(Integer)
    quantity = Column(Numeric)
    days_supply = Column(Integer)
    sig = Column(Text)
    route_concept_id = Column(Integer)
    lot_number = Column(String(50))
    provider_id = Column(BigInteger)
    visit_occurrence_id = Column(BigInteger)
    visit_detail_id = Column(BigInteger)
    drug_source_value = Column(String(50))
    drug_source_concept_id = Column(Integer)
    route_source_value = Column(String(50))
    dose_unit_source_value = Column(String(50))

    def as_dict(self):
        r = {}
        for c in self.__table__.columns:
            if c.name.endswith('concept_id'):
                concept = db.session.query(Concept).filter_by(concept_id=getattr(self, c.name)).first()
                if concept:
                    r[c.name[:-2] + 'name'] = concept.concept_name
            r[c.name] = getattr(self, c.name)
        return r
