from flask import Flask

server = Flask(__name__, static_folder='static', template_folder='templates')

from webapp import api
