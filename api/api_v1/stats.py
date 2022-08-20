from sqlalchemy import func

from . import api
from .models.death import Death
from .models.person import Person
from .models.visit_occurrence import VisitOccurrence
from .. import db


@api.route('/stats', methods=['GET'])
def get_stats():
    total_patient = db.session.query(func.count(Person.person_id)).scalar()
    total_visit = db.session.query(func.count(VisitOccurrence.visit_occurrence_id)).scalar()

    patient_gender = db.session.query(
        func.count(Person.gender_concept_id), Person.gender_concept_id
    ).group_by(Person.gender_concept_id).all()
    patient_ethnicity = db.session.query(
        func.count(Person.ethnicity_concept_id), Person.ethnicity_concept_id
    ).group_by(Person.ethnicity_concept_id).all()
    patient_race = db.session.query(
        func.count(Person.race_concept_id), Person.race_concept_id
    ).group_by(Person.race_concept_id).all()
    patient_death = db.session.query(func.count(Death.person_id)).scalar()

    visit_type = db.session.query(
        func.count(VisitOccurrence.visit_type_concept_id), VisitOccurrence.visit_type_concept_id
    ).group_by(VisitOccurrence.visit_type_concept_id).all()

    # TODO: 방문 - 유형별 성별 인종별 민족별 연령대별

    result = {
        'patient': {
            'total': total_patient,
            'gender': dict((y, x) for x, y in patient_gender),
            'ethnicity': dict((y, x) for x, y in patient_ethnicity),
            'race': dict((y, x) for x, y in patient_race),
            'death': patient_death
        },
        'visit': {
            'total': total_visit,
            'visit_type': dict((y, x) for x, y in visit_type),
        }
    }
    return result
