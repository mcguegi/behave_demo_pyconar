from flask import Blueprint, render_template, request, redirect

from extensions import db
from .models import Person, Proposal, Talk

pycon_ar = Blueprint('pycon_ar', __name__)


@pycon_ar.route('/')
def hello_world():
    return 'Hello World!'


@pycon_ar.route('/send_proposal')
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
