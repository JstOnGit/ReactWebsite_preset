import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from flask import Flask
from flask_cors import CORS
from config import (
    db, SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS, BACKEND_HOST, BACKEND_PORT
)
from api import test_bp
from models.testModel import TestModel

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS

CORS(app)
db.init_app(app)

app.register_blueprint(test_bp, url_prefix='/api')

def initialize_database():
    """Initialize database with exactly one test record"""
    with app.app_context():
        db.create_all()
        
        existing_records = TestModel.query.all()
        
        if len(existing_records) == 0:
            test_record = TestModel(id=0, text="Hello, world.")
            db.session.add(test_record)
            db.session.commit()
            print("Database initialized with test record")
        else:
            print(f"Database already has {len(existing_records)} records")

if __name__ == "__main__":
    initialize_database()
    app.run(host=BACKEND_HOST, port=BACKEND_PORT, debug=True)
