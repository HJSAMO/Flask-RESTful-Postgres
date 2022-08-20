from flask import Blueprint

api = Blueprint('v1', __name__, url_prefix='/v1')

from . import stats
from . import data
from . import concept
