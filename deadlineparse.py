import icalendar as i
import iso8601
import pytz
import io
import uuid

class EventItem:
    def __init__(self,ident=None,summary=None,description=None,deadline=None,notifydays=7):
        self.ident = ident
        self.summary = summary
        self.description = description 
        self.deadline = deadline
        self.notifydays= notifydays 

def getmsg(msg,delim):
    index = msg.find(delim)
    ret = msg[index+1:].replace('\n','').replace('\t','').replace('\\','')
    return ret 

'''
_date_utc=_date_obj.astimezone(pytz.utc)
_date_utc_zformat=_date_utc.strftime('%Y-%m-%dT%H:%M:%SZ')
g = io.open('deadline_in/icalexport.ics',mode='r',encoding='utf-8')
gcal = i.Calendar.from_ical(g.read())
for component in gcal.walk():
    if
    print(component.get('description'))
    print(component.get('summary'))
    print(component.get('name'))
g.close()
'''

f = io.open('deadline_in/icalexport.ics',mode='r',encoding='utf-8')
l = f.readlines()
allevents = []
guid = 0
for i in range(len(l)):
    if('BEGIN:VEVENT' in l[i]):
        index = i
        event = EventItem()
        if(__debug__):
            event.ident = uuid.uuid4().hex
        while('END:VEVENT' not in l[index]):
            if('SUMMARY' in l[index]):
                event.summary = getmsg(l[index],':')
            elif('DESCRIPTION' in l[index]):
                run = index
                desc = "" 
                while('CLASS:PUBLIC' not in l[run]):
                    desc += l[run].replace('\\n','')
                    run+=1
                d = getmsg(desc,':') 
                event.description = d
            elif('DTEND' in l[index]):
                dtend = getmsg(l[index],':')
                date_obj = iso8601.parse_date(dtend)
                event.deadline = date_obj.strftime('%Y-%m-%d %H:%M:%S')
                
            index+=1 
        allevents.append(event)


for k in range(len(allevents)):
    print(allevents[k].ident)
    print(allevents[k].summary)
    print(allevents[k].description)
    print(allevents[k].deadline)
    print()
    print()
    print()
    print()
s = "20201130T220000Z"


_date_obj=iso8601.parse_date(s)
d = _date_obj.strftime('%Y-%m-%d %H:%M:%S')
print(_date_obj)
print(d)

