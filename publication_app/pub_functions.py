import os
import re
from typing import Dict, Any
from pub_data_classes import *
from pub_classes import *



txt = """
$pub_s$
$city_s$
new yourk
$city_e$

$date_s$
2024-03-30
$date_e$

$news_s$
the bOdy OF ThE valid news 2
$news_e$

$pub_e$
"""

def find_match( pattern, text):
    # Regular expression pattern
    re_pattern = fr"\${pattern}_s\$(.*?)\${pattern}_e\$"
    matches = re.search(re_pattern, text, re.DOTALL)

    return matches.group(1).strip() if matches else ''


def text_parser(text: str) -> Dict[str, Any]:
    publications = re.findall(r'\$pub_s\$(.*?)\$pub_e\$', text, re.DOTALL)
    parsed_data = []
    unparsed_data = []

    for pub in publications:
        
        city = find_match('city', pub)
        date = find_match('date', pub)
        news_body = find_match('news', pub)
        ad_body = find_match('pr_ad', pub)
        sport_type = find_match('sp_type', pub)
        sport_body = find_match('sp_news', pub)

        result = None
        if city and sport_type and sport_body:
            result = SportNewsData(pub_body=sport_body, pub_city=city, pub_date=date, sport_type=sport_type)
        elif city and news_body:
            result = NewsData(pub_body=news_body, pub_city=city, pub_date=date)
        elif date and ad_body:
            result = PrivateAddData(pub_body=ad_body, exp_date=date)
        else:
            unparsed_data.append(f"Unparsed publication \n{pub}")
        
        if result:
            if result.status:
                parsed_data.append(result)
            else:
                unparsed_data.append(f"Bad {str(result.pub_type.capitalize())} data\n{result.decision} \n{pub}")


    return {"parsed_data": parsed_data, "unparsed_data": unparsed_data}



def fider_path(folder = '', directory = ''):
    if not folder:
        folder = 'feeder_files'
    if not directory: 
        directory = os.path.abspath(os.path.dirname(__file__)) 

    folder_path = os.path.join(directory, "feeder_files")
    return folder_path



def txt_parser(fider_path):
    text = ''
    
    for filename in os.listdir(fider_path):
        # get full file path
        filepath = os.path.join(fider_path, filename)

        # check the path and read the entire text from file
        if os.path.isfile(filepath) and filepath.endswith('.txt'):
            try:
                with open(filepath, "r") as file:
                    file_content = file.read()
                    if file_content:
                        text += file_content
                os.remove(filepath)
            except Exception as e:
                text = f" $pub_s$ An unexpected error with {filename} occurred: {e} $pub_e$"

    if not text:
        text = ' $pub_s$ No txt-files found $pub_e$'

    return text 



def write_involid_publications(unparsed_text, file_name = 'file_unparsed_pubs.txt' ):
    text = f"{'-'*70} \n{unparsed_text}\n"
    try:
        with open(file_name, 'a') as file:
            file.write(text)
    except Exception as e:
        raise OSError(f"An unexpected error occurred: {e}")
        


def publish_all(folder = '', directory = ''):
    path = fider_path(folder, directory)

    text = txt_parser(path)

    unparsed_data = text_parser(text)["unparsed_data"]
    date_time = datetime.now().strftime('%Y-%m-%d  %H:%M')
    unparsed_header = f" {'*' * 25} {date_time} {'*' * 25}"
    write_involid_publications(unparsed_header)
    for rec in unparsed_data:
        write_involid_publications(rec)


    parsed_data = text_parser(text)["parsed_data"]

    if not isinstance(parsed_data, list):
        parsed_data = [parsed_data]

    for rec in parsed_data:

        if rec.pub_type == 'news':
            a = News()
        elif rec.pub_type == 'ad':
            a = PrivateAd()
        elif rec.pub_type == 'sport_news':
            a = SportNews()
    
    
        a.publish_data(rec)


