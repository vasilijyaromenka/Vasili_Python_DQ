import os
from pub_data_classes import *
from pub_classes import *
from pub_functions import *
from pub_csv_module import *



news = News()
private_add = PrivateAd()
event_announcement = SportNews()



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
        publish_all()
        is_valid_input = True
    else:   
        print("Enter a valid input")

     
    if is_valid_input:
        if pub_type in {'1', '2', '3'}:
            p.publish_from_input()

    words_counts('feed')
    letters_counts('feed')