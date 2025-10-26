from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

BACKEND_DIR = os.path.abspath(os.path.dirname(__file__))
INSTANCE_FOLDER = os.path.join(BACKEND_DIR, "instance")

os.makedirs(INSTANCE_FOLDER, exist_ok=True)

SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(INSTANCE_FOLDER, 'database.db')}"
SQLALCHEMY_TRACK_MODIFICATIONS = False

BACKEND_HOST = "localhost"
BACKEND_PORT = 4269
