from flask import Blueprint, jsonify
from models.testModel import TestModel

test_bp = Blueprint('test', __name__)

@test_bp.route('/test', methods=['GET'])
def get_test_data():
    try:
        test_records = TestModel.query.all()
        return jsonify([record.to_json() for record in test_records])
    except Exception as e:
        return jsonify({"error": str(e)}), 500