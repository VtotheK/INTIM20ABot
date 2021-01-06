#!/usr/bin/python3

import iso8601
from datetime import date, time, datetime,timedelta
import pytz
import os 
import io
import uuid
import glob
import mysql.connector
import logutils as lu
from db.connections import dbconnections as dbcon
from eventitem import EventItem


def getmsg(msg,delim):
    index = msg.find(delim)
    ret = msg[index+1:].replace('\n','').replace('\t','').replace('\\','')
    return ret 

def updatedeadlines(events):
    callingproc = os.path.basename(__file__)
    try: 
        conn = mysql.connector.connect(user=dbcon.user,password=dbcon.password,host=dbcon.host,database=dbcon.db)
        cur = conn.cursor()
        for e in events:
            notifyfrom = e.deadline - timedelta(days=e.notifydays)
            params = [0,e.module,e.course,e.title,e.summary,e.userid,e.deadline,notifyfrom]
            cur.callproc('deadlines_set',params)
            conn.commit()
        debugmsg = "Succesfully added new deadlines."
        lu.submitlog(lu.Severity.INFORMATION.value,lu.Issuer.Python.value,callingproc,debugmsg)
    except mysql.connector.Error as error:
        logmsg = 'Failed to add deadlines to db'
        lu.submitlog(lu.Severity.CRITICALERROR.value,lu.Issuer.Python.value,callingproc,debugmsg)
    finally:
        if(conn.is_connected()):
            cur.close()
            conn.close()

def parsefile():
    allevents = []
    for filename in glob.glob('deadline_in/*.ics'):
        f = io.open(filename,mode='r',encoding='utf-8')
    l = f.readlines()
    guid = 0
    for i in range(len(l)):
        if('BEGIN:VEVENT' in l[i]):
            index = i
            event = EventItem()
            while('END:VEVENT' not in l[index]):
                if('SUMMARY' in l[index]):
                    sumrun = index
                    sm = ""
                    while('DESCRIPTION' not in l[sumrun]):
                        sm += l[sumrun].replace('\\n','')
                        sumrun+=1
                    event.summary = getmsg(sm,':')
                elif('DESCRIPTION' in l[index]):
                    descrun = index
                    desc = "" 
                    while('CLASS:PUBLIC' not in l[descrun]):
                        desc += l[descrun].replace('\\n','')
                        descrun+=1
                    d = getmsg(desc,':') 
                    event.description = d
                elif('DTEND' in l[index]):
                    dtend = getmsg(l[index],':')
                    date_obj = iso8601.parse_date(dtend)
                    baddeadline = date_obj.strftime('%Y-%m-%d %H:%M:%S')
                    deadline = datetime.strptime(baddeadline,'%Y-%m-%d %H:%M:%S')
                    deadline = deadline + timedelta(hours=2)
                    event.deadline=deadline
                index+=1 
            allevents.append(event)
    return allevents  



if(__name__=='__main__'):
    events = parsefile()
    print(len(events))
    if(len(events) > 0):
        updatedeadlines(events)
