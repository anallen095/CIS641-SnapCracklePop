
import pyodbc

cnxn_str = ('Driver={SQL Server};' 'Server=DESKTOP-GV28CEC\SQLEXPRESS;' 'Database=snap;' 'Trusted_connection=yes;')

cnxn = pyodbc.connect(cnxn_str, autocommit=True)
crsr = cnxn.cursor()

def duplicate():
    data = crsr.execute('SELECT docNum, COUNT(docNum) FROM transactions GROUP BY docNum HAVING COUNT(docNum) >1')

    if data:
        return True
    else: 
        return False



