import textwrap
from datetime import datetime, date
import re
from abc import ABC, abstractmethod
import re
import os 
import sys
from pub_data_classes import *
from pub_classes import *



news = News()
private_add = PrivateAd()
event_announcement = SportNews()

path = os.path.abspath(os.path.dirname(__file__))  
pff = PublishFromFiles(os.path.join(path, "feeder_files"))


input_comment = """Choose your publication type 
1 - News, 
2 - Private Ad, 
3 - Sport News
4 - Pulic all from folder
Enter 1-4: 
"""

while True:
    is_valid_input = False

    pub_type = input(input_comment)

    if pub_type == '1':
        p = news
        is_valid_input = True
    elif pub_type == '2':
        p = private_add
        is_valid_input = True
    elif pub_type == '3':
        p = event_announcement
        is_valid_input = True
    elif pub_type == '4':
        p = pff
        is_valid_input = True
    else:   
        print("Enter a valid input")

     
    if is_valid_input:
        if pub_type == '4':
            pff.publish_all()
        else:
            p.publish_from_input()
