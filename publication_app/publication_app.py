from pub_classes import News, PrivateAd, SportNews
from pub_txt_functions import publish_txt
from pub_json_functions import publish_json
from pub_xml_functions import publish_xml
from pub_csv_module import letters_counts, words_counts




news = News()
private_add = PrivateAd()
event_announcement = SportNews()



input_comment = """Choose your publication type 
1 - News, 
2 - Private Ad, 
3 - Sport News
4 - Pulish from txt files
5 - Pulish from json files
6 - Pulish from xml files
Enter 1-6: 
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
        publish_txt()
        is_valid_input = True
        print("txt files have been proccessed\n")
    elif pub_type == '5':
        publish_json()
        is_valid_input = True
        print("json files have been proccessed\n")
    elif pub_type == '6':
        publish_xml()
        is_valid_input = True
        print("xml files have been proccessed\n")
    else:   
        print("Enter a valid input")

     
    if is_valid_input:
        if pub_type in {'1', '2', '3'}:
            p.publish_from_input()

    words_counts('feed')
    letters_counts('feed')
