from .user import User


class Guest(User):
    def __init__(self, username):
        super().__init__(username)
