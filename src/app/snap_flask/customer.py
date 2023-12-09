from snap_flask.database import crsr, cnxn

class Customer():
    def __init__(self, customerNbr):
        super().__init__()
        self.id = customerNbr
        result = crsr.execute("SELECT SUM(Amount) amount FROM transactions WHERE customerNbr = ? AND Status = 1", (self.id,)).fetchone()
        self.openBal = result[0] if result else 0

        result = crsr.execute("SELECT COUNT(*) count FROM transactions WHERE customerNbr = ? AND Status = 1", (self.id,)).fetchone()
        self.openCount = result[0] if result else 0

        result = crsr.execute("SELECT B.firstName +' ' + B.lastName, supportType, B.emailAddress FROM support A LEFT JOIN Users B ON A.userID = B.username WHERE A.customerID = ?", (self.id,)).fetchall()
        self.support = result if result else []

        result = crsr.execute('SELECT [customerName],[customerChannel],[soldToNbr],[payerNbr],[altPayer],[altPayer2],[salesA],[salesB],[salesC],[salesD],[salesE],[planTo],[planToDescritpion] FROM [dbo].[customers] WHERE [customerNbr] = ? ', (self.id,)).fetchone()
        print(len(result))
        self.name = result[0] if result else [] if len(result) >= 12 else None
        self.channel = result[1] if result else [] if len(result) >= 12 else None
        self.soldTo = result[1] if result else [] if len(result) >= 12 else None  # Ensure index exists
        self.payer = result[2] if result else [] if len(result) >= 12 else None  # Ensure index exists
        self.altPayer = result[3] if result else [] if len(result) >= 12 else None  # Ensure index exists
        self.altPayer2 = result[4] if result else [] if len(result) >= 12 else None  # Ensure index exists
        self.salesA = result[5] if result else [] if len(result) >= 12 else None  # Ensure index exists
        self.salesB = result[6] if result else [] if len(result) >= 12 else None  # Ensure index exists
        self.salesC = result[7] if result else [] if len(result) >= 12 else None  # Ensure index exists
        self.salesD = result[8] if result else [] if len(result) >= 12 else None  # Ensure index exists
        self.salesE = result[9] if result else [] if len(result) >= 12 else None  # Ensure index exists
        self.planTo = result[10] if result else [] if len(result) >= 12 else None  # Ensure index exists
        self.planToName = result[11] if result else [] if len(result) >= 12 else None  # Ensure index exists
        

        



    def get_id(self):
        return str(self.id)
    
