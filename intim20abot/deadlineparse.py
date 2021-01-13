#!/usr/bin/python3

import iso8601
import pytz
import shutil
import os 
import io
import uuid
import glob
import mysql.connector
import logutils as lu
from db.connections import dbconnections as dbcon
from eventitem import EventItem
from datetime import date, time, datetime,timedelta

files = []

def getmsg(msg,delim):
    index = msg.find(delim)
    ret = msg[index+1:].replace('\n','').replace('\t','').replace('\\','')
    return ret 

def updatedeadlines(events):
    callingproc = os.path.basename(__file__)
    success = False
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
        success = True
    except mysql.connector.Error as error:
        logmsg = 'Failed to add deadlines to db'
        lu.submitlog(lu.Severity.CRITICALERROR.value,lu.Issuer.Python.value,callingproc,debugmsg)
    finally:
        if(conn.is_connected()):
            cur.close()
            conn.close()
    return success

def getevents():
    allevents = []
    for filename in glob.glob('deadline_in/*.ics'):
        files.append(filename)
        f = io.open(filename,mode='r',encoding='utf-8')
        line = f.readlines()
        guid = 0
        for i in range(len(line)):
            if('BEGIN:VEVENT' in line[i]):
                index = i
                event = EventItem()
                while('END:VEVENT' not in line[index]):
                    if('SUMMARY' in line[index]):
                        sumrun = index
                        sm = ""
                        while('DESCRIPTION:' not in line[sumrun]):
                            sm += line[sumrun].replace('\\n','')
                            sumrun+=1
                        event.summary = getmsg(sm,':')
                    elif('DESCRIPTION' in line[index]):
                        descrun = index
                        desc = "" 
                        while('CLASS:PUBLIC' not in line[descrun]):
                            desc += line[descrun].replace('\\n','')
                            descrun+=1
                        d = getmsg(desc,':') 
                        event.description = d
                    elif('DTEND:' in line[index]):
                        dtend = getmsg(line[index],':')
                        date_obj = iso8601.parse_date(dtend)
                        baddeadline = date_obj.strftime('%Y-%m-%d %H:%M:%S')
                        deadline = datetime.strptime(baddeadline,'%Y-%m-%d %H:%M:%S')
                        deadline = deadline + timedelta(hours=2)
                        event.deadline=deadline
                    index+=1 
                allevents.append(event)
    return allevents  

def moveicsfiles(folder):
    path = 'deadline_in/' + folder
    for i in range(len(files)):
        shutil.move(files[i],path)

if(__name__=='__main__'):
    events = getevents()
    print(len(events))
    if(len(events) > 0):
        if(updatedeadlines(events)):
            moveicsfiles('processed')
        else:
            moveicsfiles('errored')
