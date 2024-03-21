from dataclasses import dataclass, field
from datetime import datetime



@dataclass
class PubblicationData:
    pub_body: str
    pub_date: str = field(default='')
    status: bool  = field(default = True)
    decision: str = field(default = '')

    def __post_init__(self):

        if not self.pub_date.strip():
            self.pub_date = datetime.now().strftime('%Y-%m-%d %H:%M')

        try:
            datetime.strptime(self.pub_date, '%Y-%m-%d %H:%M')
        except ValueError:
            try:
                datetime.strptime(self.pub_date, '%Y-%m-%d')
            except ValueError:
                self.status = False
                self.decision += "/Invalid pub_date format /"

        if len(self.pub_body) < 6:
                self.status = False
                self.decision += "/ To short pub_body /"  

@dataclass
class NewsData(PubblicationData):
    pub_city: str = field(default = None)
    pub_type: str = field(default = 'news')
    

    def __post_init__(self):
        super().__post_init__()  # to call parent's __post_init__

        if len(self.pub_city) < 3:
            self.status = False
            self.decision += "/ To short pub_city /"  


@dataclass
class PrivateAddData(PubblicationData):
    exp_date: str = field(default = None)
    days_left: str = field(default=None)
    pub_type: str = field(default='ad')

    
    def __post_init__(self):
        super().__post_init__()

        try:
            date = datetime.strptime(self.exp_date, '%Y-%m-%d').date()
            days_left = (date - datetime.now().date()).days
            if days_left < 0:
                self.status = False
                self.decision += "/ exp_date in the past /"
            self.days_left = str(days_left)
        except BaseException:
            self.status = False
            self.decision = "/ Invalid exp_date format /"

@dataclass
class SportNewsData(NewsData):
    sport_type: str = field(default = None)
    pub_type: str = field(default='sport_news')

    
    def __post_init__(self):
        super().__post_init__()

        if len(self.sport_type) < 3:
            self.status = False
            self.decision += "/ To short sport_type /"        

