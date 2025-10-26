from config import db

class TestModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "text": self.text
        }