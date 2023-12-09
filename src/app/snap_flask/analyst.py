from snap_flask.User import User  

class analyst(User):
    def __init__(self, userID, username, firstName, lastName, manager, role, email):
        super().__init__(userID, username, firstName, lastName, manager, role, email)

    