import string
from .. import db
from dataclasses import dataclass

@dataclass 
class Doodle(db.Model):
    __tablename__ = "doodle"

    id: int
    instructions: string

    id = db.Column(db.Integer, primary_key=True)
    instructions = db.Column(db.String(), nullable=False)

    def __init__(self, id, instructions):
        self.id = id
        self.instructions = instructions

    @staticmethod
    def create(instructions):
        """
        Create new doodle
        """
        doodle = Doodle(None, instructions)
        db.session.add(doodle)
        db.session.commit()
        return doodle

    @staticmethod
    def update(id, instructions):
        """
        Update existing doodle
        """
        doodle = Doodle.query.filter_by(id = id).one()
        doodle.instructions = instructions
        db.session.commit()
        return doodle
    
    @staticmethod
    def delete(id):
        """
        Delete existing doodle
        """
        doodle = Doodle.query.filter_by(id = id).one()
        db.session.delete(doodle)
        db.session.commit()
        return doodle
