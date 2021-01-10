from enum import Enum

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
