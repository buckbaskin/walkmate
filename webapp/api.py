from webapp import server as router

from flask import render_template

@router.route('/')
def index():
    return render_template('index.html')


@router.route('/trip')
def tripfinder():
    return render_template('find_trip.html')