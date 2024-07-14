from flask import jsonify
from .exceptions import NotFoundException, BadRequestException

def register_error_handlers(app):
    @app.errorhandler(NotFoundException)
    def handle_not_found_error(error):
        response = jsonify({'message': error.message})
        response.status_code = 404
        return response

    @app.errorhandler(BadRequestException)
    def handle_bad_request_error(error):
        response = jsonify({'message': error.message})
        response.status_code = 400
        return response

    @app.errorhandler(500)
    def internal_server_error(error):
        response = jsonify({'message': 'Internal server error', 'error': str(error)})
        response.status_code = 500
        return response
