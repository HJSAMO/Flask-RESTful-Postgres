from flask import request
from sqlalchemy import or_

from . import api
from .models.concept import Concept
from .. import db
from ..utils import pagination_encoder


@api.route('/concept', methods=['GET'])
def get_concept():
    keyword = request.args.get('keyword') or None
    page = request.args.get('page') or 1
    data = db.session.query(Concept)
    if keyword:
        data = data.filter(or_(Concept.concept_name.like('%' + keyword + '%'),
                               Concept.domain_id.like('%' + keyword + '%')))
    data = data.paginate(page=int(page), per_page=10)
    return pagination_encoder(data)
