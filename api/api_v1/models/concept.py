from sqlalchemy import Column, Integer, String, Date

from api import db


class Concept(db.Model):
    __tablename__ = 'concept'
    __table_args__ = {'schema': 'de'}

    concept_id = Column(Integer, primary_key=True)
    concept_name = Column(String(255))
    domain_id = Column(String(20))
    vocabulary_id = Column(String(20))
    concept_class_id = Column(String(20))
    standard_concept = Column(String(1))
    concept_code = Column(String(50))
    valid_start_date = Column(Date)
    valid_end_date = Column(Date)
    invalid_reason = Column(String(1))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
