from webapp import server as app
from webapp.wordid import wordset_to_integer, integer_to_wordset

from flask_login import LoginManager, UserMixin

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

user_database = {
    wordset_to_integer('jane.doe'): {
        'uuid': wordset_to_integer('jane.doe'),
        'first_name': 'Jane',
        'last_name': 'Doe',
        'email': 'example@case.edu',
        'password': 'password'
    }
}

class User(UserMixin):
    def __init__(self, uuid, first_name, last_name, email, **kwargs):
        self.uuid = uuid
        self.username = integer_to_wordset(uuid)
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    @classmethod
    def build(self, username):
        if wordset_to_integer(username) in user_database:
            return User(**user_database[wordset_to_integer(username)])
        return None

    def get_id(self):
        return self.uuid

@login_manager.user_loader
def load_user(user_str_id):
    integer_user_id = wordset_to_integer(user_str_id)
    if integer_user_id < 0:
        return None
    if integer_user_id not in user_database:
        return None
    # TODO implement this with the actual database
    else:
        return User(**user_database[integer_user_id])
