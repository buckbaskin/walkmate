from webapp import server as router

from flask import render_template

@router.route('/')
def index():
    return render_template('index.html')
