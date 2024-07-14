from functools import wraps
from flask import request, jsonify
from ..models import businesses
from ..utils.exceptions import NotFoundException


def json_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.is_json:
            return f(*args, **kwargs)
        return jsonify({'message': 'Request content type must be application/json'}), 400
    return decorated_function

def business_exists(f):
    @wraps(f)
    def decorated_function(fein, *args, **kwargs):
        fein = str(fein)
        if fein not in businesses:
            raise NotFoundException('Business not found')
        return f(fein, *args, **kwargs)
    return decorated_function
