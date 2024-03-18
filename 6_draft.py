import re
import os 
import textwrap
from datetime import datetime, date
import re
from abc import ABC, abstractmethod
from dataclasses import dataclass

path = r"C:\Users\Vasili_Yaromenka\Documents\my_learning\Python_for_DQ\Vasili_Yaromenka_PyDQ\feeder_files"


def return_text_blocks(pattern, text):
    # Regular expression pattern
    pattern = fr"\${pattern}_s\$(.*?)\${pattern}_e\$"
    compiled_pattern = re.compile(pattern, re.DOTALL)
    # Find all matches in the text
    matches = compiled_pattern.findall(text)
    # Trim whitespace from matches
    trimmed_matches = [match.strip() for match in matches]
    return trimmed_matches

def is_valid_date(date_str, exclude = None):
    if exclude != None and date_str == exclude:
        return True
    else:
        try:
            datetime.strptime(date_str, '%Y-%m-%d').date()
            return True
        except:
            return False            

def is_future_date(date_str):
    try:
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        days_left = (date - date.today()).days
        if days_left >= 0:
            return True
        else:
            return False
    except:
        return False
    

def is_long_enough(txt, lenth):
    return len(txt.strip()) >= lenth

@dataclass
class PublicationData:
    city: str
    date: str
    body: str

@dataclass
class SportNewsData(PublicationData):
    sport_type: str


# Iterate over files in the directory
for filename in os.listdir(path):
    # Combine directory path with file name
    filepath = os.path.join(path, filename)
    
    # Check if the path is a file
    if os.path.isfile(filepath):
        # Read text from the file
        with open(filepath, "r") as file:
            text = file.read()

        publications = return_text_blocks('pub', text)
        for publication in publications:
            city = return_text_blocks('city', publication) + ['']
            body = return_text_blocks('news', publication) + ['']
            date = return_text_blocks('date', publication) + ['']

            news = PublicationData(city=city[0], body=body[0], date=date[0])

            if is_long_enough(news.city, 3) and is_long_enough(news.body, 6) and is_valid_date(news.date, ''):
                print(f"City: {news.city}")
                print(f"Body: {news.body}")
                print(f"Date: {news.date}")        
            else:
                with open('broken_publications.txt', 'a') as file:
                    date_time = datetime.now().strftime('%Y-%m-%d  %H:%M')
                    file.write(f"{'*'*30} {date_time} {'*'*30} \n {publication} \n")



