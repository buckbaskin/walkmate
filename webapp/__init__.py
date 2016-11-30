from flask import Flask

server = Flask(__name__, static_folder='static', template_folder='templates')
server.config['SECRET_KEY'] = 'super secret key do not share with anyone'

from webapp import api
