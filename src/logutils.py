from enum import Enum
import mysql.connector
from debuglevels import Severity,Issuer
from db.connections import dbconnections as dbcon

class Severity(Enum):
    INFORMATION = 1
    NOTIFICATION = 2
    ERROR = 3
    CRITICALERROR = 4
    FATALERROR = 5

class Issuer(Enum):
    Python = 1
    Mysql = 2
    Linux = 3
    Discord = 4

def submitlog(severityid,issuerid,callingproc,message):
    try:
        debugconn = mysql.connector.connect(user=dbcon.user,password=dbcon.password,host=dbcon.host,database=dbcon.logdb)
        debugcur = debugconn.cursor()
        params = [severityid,issuerid,callingproc,message]
        debugcur.callproc('debuginsert',params)
        debugconn.commit()
        debugconn.close()
        debugcur.close()
    except mysql.connector.Error as error:
        print('Something went very wrong here')
        print(error) 
    finally:
        if(debugconn.is_connected()):
            debugconn.close()
            debugcur.close()
