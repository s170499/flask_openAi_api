from . import db

class Q_and_A(db.Model):
    question = db.Column(db.String(500), primary_key=True)
    answer = db.Column(db.String(500), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"Q_and_A {self.question}, answer {self.answer}, registered on {self.timestamp}"
        
    







