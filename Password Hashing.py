# user.py
import bcrypt

class User:
    def __init__(self, user_id, password):
        self.user_id = user_id
        self.password_hash = self._hash_password(password)

    def _hash_password(self, password):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt)

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash)
