from enum import Enum
from extensions import db


class Role(Enum):
    ATTENDEE = 'ATTENDEE'
    SPEAKER = 'SPEAKER'
    COLLABORATOR = 'COLLABORATOR'
    ORGANIZER = 'ORGANIZER'


class Status(Enum):
    DRAFT = 'DRAFT'
    IN_REVIEW = 'IN REVIEW'
    APPROVED = 'APPROVED'
    REJECTED = 'REJECTED'


class Level(Enum):
    BASIC = 'BASIC'
    INTERMEDIATE = 'INTERMEDIATE'
    HARD = 'HARD'


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(512))
    last_name = db.Column(db.String(512))
    email = db.Column(db.String(512))
    country = db.Column(db.String(512))
    role = db.Column(db.Enum(Role))


class Proposal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    status = db.Column(db.Enum(Status), default=Status.DRAFT)
    level = db.Column(db.Enum(Level), default=Level.BASIC)
    description = db.Column(db.String(512))
    speaker_id = db.Column(db.Integer, db.ForeignKey('person.id'),
                           nullable=False)


class Talk(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    proposal_id = db.Column(db.Integer, db.ForeignKey('proposal.id'),
                            nullable=False)
    youtube_link = db.Column(db.String(512))
