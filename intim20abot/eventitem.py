class EventItem:
    def __init__(self,userid=None,course=None,title=None,module=None,summary=None,description=None,deadline=None,notifydays=7):
        self.summary = summary
        self.description = description 
        self.deadline = deadline
        self.notifydays= notifydays 
        self.module = module
        self.course=course
        self.title=title
        self.userid = userid
