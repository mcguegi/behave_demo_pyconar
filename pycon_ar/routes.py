from flask import Blueprint, render_template, request, redirect

from extensions import db
from .database import create_person
from .models import Person, Proposal, Talk, Role

pycon_ar = Blueprint('pycon_ar', __name__)


@pycon_ar.route('/')
def hello_world():
    return 'Hello World, welcome to PyconAr 2020!'


@pycon_ar.route('/register', methods=['GET', 'POST'])
def register_speaker():
    if request.method == 'GET':
        return render_template('register.html')

    name = request.form['name']
    last_name = request.form['last_name']
    email = request.form['email']
    country = request.form['country']
    role = 'SPEAKER'
    result = create_person(name, last_name, email, country, role)

    if result:
        return 'Congrats! You are registered as a Speaker'

    return 'Something happened! Try again.'


@pycon_ar.route('/send_proposal', methods=['POST'])
def send_proposal():
    pass


@pycon_ar.route('/check_status_proposal')
def check_status_proposal():
    pass


@pycon_ar.route('/apply')
def apply_as_a_collaborator():
    pass


@pycon_ar.route('/organizers')
def get_organizers_info():
    pass
