class UserLogin():
    def from_db(self, user_id, db):
        self.__user = db.

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.__user['id'])