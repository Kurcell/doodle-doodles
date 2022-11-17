from .. import db
from dataclasses import dataclass

@dataclass 
class Doodle(db.Model):
    __tablename__ = "doodle"
    
    id = db.Column(db.Integer, primary_key=True)
    instructions = db.Column(db.String(500), nullable=False)

    @staticmethod
    def create(instructions):
        """
        Create new doodle
        """
        doodle = Doodle(instructions)
        db.session.add(doodle)
        db.session.commit()
