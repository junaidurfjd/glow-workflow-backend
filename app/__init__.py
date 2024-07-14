from flask import Flask
from .views.business_view import business_bp
from .utils.error_handling import register_error_handlers

def create_app():
    app = Flask(__name__)
    app.register_blueprint(business_bp)
    register_error_handlers(app)
    return app
