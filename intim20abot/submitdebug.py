from debuglevels import Severity,Issuer
from db.connections import dbconnections as dbcon

def submit(severityid,issuerid,callingproc,message):
    try:
        debugconn = mysql.connector.connect(user=dbcon.user,password=dbcon.password,host=dbcon.host,database=dbcon.logdb)
        debugcur = conn.cursor()
        params = [severityid,issuerid,callingproc,message]
        debugcur.callproc('debuginsert',params)
        debugconn.commit()
        debugconn.close()
        debugcur.close()
    except mysql.connector.Error as error:
        print('Something went very wrong here')
        print(error) 
