import iso8601
import pytz
import io
import uuid
import glob


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

if(glob.glob('deadline_in/*.ics')):
        print('FUCKYUEA')

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
