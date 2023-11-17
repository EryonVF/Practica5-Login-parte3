from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, username, password, fullname, usertype):
        self.id = id
        self.username = username
        self.password = password
        self.fullname = fullname
        self.usertype = usertype
