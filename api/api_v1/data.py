from flask import request

from api.api_v1.models.person import Person
from . import api
from .models.condition_occurrence import ConditionOccurrence
from .models.death import Death
from .models.drug_exposure import DrugExposure
from .models.visit_occurrence import VisitOccurrence
from .. import db
from ..utils import pagination_encoder


@api.route('/data/<table>', methods=['GET'])
def get_data(table):
    data = db.session

    if table == 'person':
        data = data.query(Person)
    elif table == 'visit_occurrence':
        data = data.query(VisitOccurrence)
    elif table == 'condition_occurrence':
        data = data.query(ConditionOccurrence)
    elif table == 'drug_exposure':
        data = data.query(DrugExposure)
    elif table == 'death':
        data = data.query(Death)
    else:
        return

    # TODO: Keyword 검색 Like 검색으로 변경
    column = request.args.get('column') or None
    keyword = request.args.get('keyword') or None
    if column and keyword:
        d = {column: keyword}
        data = data.filter_by(**d)

    page = request.args.get('page') or 1
    data = data.paginate(page=int(page), per_page=10)
    return pagination_encoder(data)
