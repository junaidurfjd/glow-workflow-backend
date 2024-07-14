from flask import Blueprint, request, jsonify
from ..controllers.business_controller import BusinessController
from ..utils.docorators import json_required
business_bp = Blueprint('business', __name__)

@business_bp.route('/businesses', methods=['POST'])
@json_required
def create_business():
    data = request.get_json()
    business = BusinessController.create_business(data)
    return jsonify(business), 201

@business_bp.route('/businesses/<string:fein>/approve_market', methods=['PUT'])
@json_required
def approve_market(fein):
    data = request.get_json()
    business = BusinessController.approve_market(fein, data)
    return jsonify(business), 200
    

@business_bp.route('/businesses/<string:fein>/approve_sales', methods=['PUT'])
@json_required
def approve_sales(fein):
    data = request.get_json()
    
    business = BusinessController.approve_sales(fein, data)
    return jsonify(business), 200
   

@business_bp.route('/businesses/<string:fein>/won', methods=['PUT'])
def set_won(fein):
    business = BusinessController.set_won(fein)
    return jsonify(business), 200
   

@business_bp.route('/businesses/<string:fein>/lost', methods=['PUT'])
def set_lost(fein):
    business = BusinessController.set_lost(fein)
    return jsonify(business), 200
   

@business_bp.route('/businesses/<string:fein>', methods=['GET'])
def get_business(fein):
    business = BusinessController.get_business(fein)
    return jsonify(business), 200

