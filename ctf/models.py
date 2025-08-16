from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Team(db.Model):
    id = db.Columnn(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    score = db.Column(db.Integer, default=0)
    start_time = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Team{self.name}>'