from snap_flask.database import crsr, cnxn
from snap_flask.User import User
from flask_login import UserMixin

class Admin( User):
    def __init__(self, userID, username, firstName, lastName, manager, role, email):
        super(Admin, self).__init__(userID, username, firstName, lastName, manager, role, email)
        self.set_strategy(1)

    def set_strategy(self, strategy):
        self.strategy = strategy

    def approveAccount(username):
        return

    def unlockAccount(username):
        return