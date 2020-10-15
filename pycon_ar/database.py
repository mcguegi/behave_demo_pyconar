from sqlalchemy.exc import SQLAlchemyError

from pycon_ar.models import Person
from extensions import db


def create_person(name: str, last_name: str, email: str, country: str,
                  role):
    person = Person(
        name=name,
        last_name=last_name,
        email=email,
        country=country,
        role=role
    )

    try:
        """ Try to save the person object in DB."""
        db.session.add(person)
        db.session.commit()
        return person
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return None
