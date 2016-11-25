from webapp import server as app
from webapp.wordid import wordset_to_integer, integer_to_wordset

from flask_login import LoginManager, UserMixin

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self, user_id, first_name, last_name):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self._is_authenticated = False

    def get_id(self):
        return wordset_to_integer(self.user_id)

    @property
    def is_autheticated(self):
        return self._is_autheticated

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

@login_manager.user_loader
def load_user(user_id):
    integer_user_id = wordset_to_integer(user_id)
    if integer_user_id < 0:
        return None
    # TODO implement this with the actual database
    else:
        return User(user_id, 'Jane', 'Doe')
