import icalendar as i

g = open('deadline_in/example.ics','rb')
gcal = i.Calendar.from_ical(g.read())
for component in gcal.walk():
    print(component.name)
    print(component.get('description'))
    print(component.get('summary'))
    print(component.get('name'))
g.close()
