from snap_flask.database import crsr, cnxn
from snap_flask.User import User
from flask_login import UserMixin

class mgr( User):
    def __init__(self, userID, username, firstName, lastName, manager, role, email):
        super(mgr, self).__init__(userID, username, firstName, lastName, manager, role, email)
        self.team_role(1)

    def set_role(self, teamRole):
        self.team_role(teamRole)

    def approveAccount(username):
        return

    def unlockAccount(username):
        return
    
    def getOpenBalance(team_role):
        return
    
