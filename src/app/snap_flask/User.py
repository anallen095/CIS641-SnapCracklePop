from snap_flask.database import crsr, cnxn
from flask_login import UserMixin
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user


class User(UserMixin):
    def __init__(self, userID, username,firstName, lastName, manager, role, email):
        super(User, self).__init__()
        self.id = userID
        self.username = username
        self.name = firstName + ' '+ lastName
        self.firstName = firstName
        self.manager = manager
        self.role = role
        self.email = email
        
        result = crsr.execute("Select SUM(Amount) amount from transactions A LEFT JOIN support B  on a.customerNbr = b.customerID Where b.userID = ?", (self.username,)).fetchone()
        self.openBal = result[0] if result else 0

        result = crsr.execute("SELECT COUNT(*) count FROM transactions A LEFT JOIN support B  on a.customerNbr = b.customerID Where b.userID = ?", (self.username,)).fetchone()
        self.openCount = result[0] if result else 0

        result = crsr.execute(" Select B.customerName, B.customerName, B.customerChannel from support a LEFT JOIN customers B on a.customerID = B.customerNbr Where userID = ?", (self.username,)).fetchall()
        self.support = result if result else []



        self.admin = role
 


    def get_id(self):
        return str(self.username)
    
    def reset_password(pw):
        return 
    
    def update_support(self,customerNbr):
        return
    
    def set_openBal(self): 
        return 
    
    def getAtRisk(self):
        return
    
    @property
    def get_username(self):
        return self.username
    
