import textwrap
from datetime import datetime, date
import re
from abc import ABC, abstractmethod
from dataclasses import dataclass
import re
import os 
import sys

# sys.path.append("/path/to/your/module/hw_04_task_3_vasili_yaromenka")
from hw_04_task_3_vasili_yaromenka import normalize_case

class Publcation:
    def __init__(self):
        self.pub_name = self.__class__.__name__
        self.length = 70 # max line length
        self.file_path = r"feed.txt"
        self.pub_body = None

    
    def user_input(self, text_comment = ""):
        return input(text_comment)

    def set_pub_body(self):
        is_valid_input = False
        while not is_valid_input:
            pub_body = self.user_input("Enter your publication text. Minimum 6 characters: \n")
            if len(pub_body) >= 6:
                is_valid_input = True
            else:
                print('Too short!')
        self.pub_body = pub_body

    @abstractmethod
    def pub_end(self):
        pass

    def read_data_class(self, data_instance):
        # Get attribute names of News class
        publication_attributes = vars(self)
        # Get attribute names of the input data class
        data_attributes = vars(data_instance)

        # Iterate over attribute names of News class
        for attr_name in publication_attributes:
            # Check if the attribute exists in the input data class
            if attr_name in data_attributes:
                # Set the attribute of News class with the value from the input data class
                setattr(self, attr_name, getattr(data_instance, attr_name))


    def pub_generator(self):
        llen = self.length 
        pub_end = self.pub_end()
        pub_body = self.pub_body

        # split class name into space separated words
        head_words = re.findall(r'[A-Z][a-z]*', self.pub_name)
        pub_name = ' '.join(head_words)

        # place pub_name in the senter of the header and wrap it into '---'
        spaces = int((70 - len(pub_name))/2)
        header = f"\n{llen * '-' }\n{spaces * ' ' + pub_name }\n{llen * '-'}\n\n  "

        # fit post text into the feed length
        pub_lines =  textwrap.wrap(pub_body, width=llen) 
        pub_txt = ("\n".join(pub_lines)).capitalize()

        result = f"{header}\n{pub_txt}\n\n{pub_end}"
        return result

    def write_to_file(self, post):
        post = self.pub_generator()
        try:
            with open(self.file_path, 'a') as file:
                file.write(post)
        except IOError as e:
            print(f"An error occurred while writing to the file: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}") 

    @abstractmethod
    def publish_from_input(self):
        pass

    
    def publish_from_data_class(self, data_instance):
        self.read_data_class(data_instance)
        post = self.pub_generator()
        self.write_to_file(post)     

        
        
        


class News(Publcation):
    def __init__(self):
        super().__init__()
        self.city = None
        self.news_date = None

    def set_news_date(self):
        news_date_str = self.user_input("Enter news date (YYYY-MM-DD) or leave empty for current date:\n")  
        if news_date_str == "":
            is_valid_input = True
        else:
            is_valid_input = False
            while not is_valid_input:                
                try:
                    self.news_date = datetime.strptime(news_date_str, '%Y-%m-%d').date()
                    is_valid_input = True
                except ValueError:
                    print("Invalid date format. Use 'YYYY-MM-DD'.")     


    def set_city(self):
        is_valid_input = False
        while not is_valid_input:
            city = self.user_input("Enter the city. Minimum 3 characters:\n")
            if len(city) >= 3:
                is_valid_input = True
            else:
                print('Too short!')
        self.city = city


    def pub_end(self):
        if self.news_date == '':
            news_date = datetime.now().strftime('%Y-%m-%d  %H:%M')
        else:
            news_date = self.news_date
        pub_end = f"{self.city.title()}, {news_date}."
        return pub_end
    
    def publish_from_input(self):
        self.set_pub_body()
        self.set_news_date()
        self.set_city()
        post = self.pub_generator()

        self.write_to_file(post)      
        print(f"Your post has been published: \n{post}")    
        print(self.length * '-') 



class PrivateAd(Publcation):
    def __init__(self):
        super().__init__()
        self.exp_date = None
        self.days_left = None


    def set_exp_date(self):
        is_valid_input = False
        while not is_valid_input:
            exp_date_str = self.user_input("Enter expirational date(YYYY-MM-DD):\n")
            try:
                exp_date = datetime.strptime(exp_date_str, '%Y-%m-%d').date()
            except ValueError:
                print("Invalid date format. Please use 'YYYY-MM-DD'.")
            else:
                days_left = (exp_date - date.today()).days
                if days_left >= 0:
                        is_valid_input = True
                else:
                    print("End date cannot be in the past")

        self.exp_date = exp_date_str

    def calc_days_left(self):
        exp_date = datetime.strptime(self.exp_date, '%Y-%m-%d').date()
        days_left = (exp_date - date.today()).days
        self.days_left = days_left
 
                

    def pub_end(self):
        self.calc_days_left()
        if self.days_left == 0:
            pub_end = f"Actual until: {self.exp_date}, expires today."
        else:
            pub_end = f"Actual until: {self.exp_date}, {self.days_left} days left."
        return pub_end
    
    def publish_from_input(self):
        self.set_pub_body()
        self.set_exp_date()
        post = self.pub_generator()

        self.write_to_file(post)      
        print(f"Your post has been published: \n{post}")    
        print(self.length * '-') 
    



class SportNews(News):
    def __init__(self):
        super().__init__()
        self.sport_type = None

    def set_sport_type(self):
        is_valid_input = False
        while not is_valid_input:
            sport = self.user_input("Enter the sport type. Minimum 3 characters:\n")
            if len(sport) >= 3:
                is_valid_input = True
            else:
                print('Too short!')
        self.sport_type = sport.title()

    def pub_end(self):
        if self.news_date == '':
            news_date = datetime.now().strftime('%Y-%m-%d  %H:%M')
        else:
            news_date = self.news_date
        pub_end = f"{self.sport_type.title()} news, {self.city.title()}, {news_date}."
        return pub_end

    def publish_from_input(self):
        self.set_pub_body()
        self.set_news_date()
        self.set_city()
        self.set_sport_type()
        post = self.pub_generator()

        self.write_to_file(post)      
        print(f"Your post has been published: \n{post}")    
        print(self.length * '-') 

@dataclass
class PubblicationData:
    pub_body: str

@dataclass
class NewsData(PubblicationData):
    city: str
    news_date: str

@dataclass
class PrivateAddData(PubblicationData):
    exp_date: str

@dataclass
class SportNewsData(NewsData):
    sport_type: str



class PublishFromFiles:
    def __init__(self, folder_path ):
        self.folder_path = folder_path
        self.news_lst = []
        self.privet_ad_lst = []
        self.sport_news_lst = []
        self.news = None
        self.privet_ad = None
        self.sport_news = None

        

    def return_text_blocks(self, pattern, text):
        # Regular expression pattern
        pattern = fr"\${pattern}_s\$(.*?)\${pattern}_e\$"
        compiled_pattern = re.compile(pattern, re.DOTALL)
        # Find all matches in the text
        matches = compiled_pattern.findall(text)
        # Trim whitespace from matches
        trimmed_matches = [match.strip() for match in matches]
        return trimmed_matches

    def is_valid_date(self, date_str, exclude = None):
        if exclude != None and date_str == exclude:
            return True
        else:
            try:
                datetime.strptime(date_str, '%Y-%m-%d').date()
                return True
            except:
                return False            

    def is_not_past_date(self, date_str):
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
            days_left = (date - date.today()).days
            if days_left >= 0:
                return True
            else:
                return False
        except:
            return False
        

    def is_long_enough(self, txt, lenth):
        return len(txt.strip()) >= lenth
    
    def write_involid_publications(self, publication_text, comment):
        date_time = datetime.now().strftime('%Y-%m-%d  %H:%M')                                
        with open('broken_publications.txt', 'a') as file:
            file.write(f"{'*'*30} {date_time}; {comment.upper()}: \n{publication_text}\n")

    def instantinate_classes(self):
        self.news = News()
        self.privet_ad = PrivateAd()
        self.sport_news = SportNews()

    def del_class_instances(self):
        self.news = None
        self.privet_ad = None
        self.sport_news = None

    def read_from_folder(self):
        # iterate over files in the directory
        for filename in os.listdir(self.folder_path):
            # get full file path
            filepath = os.path.join(self.folder_path, filename)
            
            # check the path and read the entire text from file
            if os.path.isfile(filepath):
                try:
                    with open(filepath, "r") as file:
                        text = file.read()
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")

            publication_lst = self.return_text_blocks('pub', text)

            for publication in publication_lst.copy():
                if '$news_s$' in publication and '$news_e$' in publication:
                    self.news_lst.append(publication)
                    index = publication_lst.index(publication)
                    publication_lst.pop(index)

                elif '$pr_ad_s$' in publication and '$pr_ad_e$' in publication:
                    self.privet_ad_lst.append(publication)
                    index = publication_lst.index(publication)
                    publication_lst.pop(index)
                
                elif '$sp_news_s$' in publication and '$sp_news_e$' in publication:
                    self.sport_news_lst.append(publication)
                    index = publication_lst.index(publication)
                    publication_lst.pop(index)

            for i in range(len(publication_lst)):
                involid_publication = publication_lst.pop()
                self.write_involid_publications(involid_publication, 'involide publication type')

            os.remove(filepath)

    def publish_news(self):
        for i in range(len(self.news_lst)):
            publication = self.news_lst.pop(0)
            city_lst = self.return_text_blocks('city', publication) + ['']
            body_lst = self.return_text_blocks('news', publication) + ['']
            date_lst = self.return_text_blocks('date', publication) + ['']
            city = city_lst[0]
            body = body_lst[0]
            date = date_lst[0]

            news_data = NewsData(city=city, pub_body=normalize_case(body), news_date=date)

            if self.is_long_enough(news_data.city, 3) and self.is_long_enough(news_data.pub_body, 6) and self.is_valid_date(news_data.news_date, ''):
                self.news.publish_from_data_class(news_data)       
            else:
                news_data_str = news_data.__repr__()
                self.write_involid_publications(news_data_str, 'involid data for news')
            

    def publish_private_ad(self):
        for i in range(len(self.privet_ad_lst)):
            publication = self.privet_ad_lst.pop(0)
            body_lst = self.return_text_blocks('pr_ad', publication) + ['']
            date_lst = self.return_text_blocks('date', publication) + ['']
            body = body_lst[0]
            date = date_lst[0]

            pr_ad_data = PrivateAddData(pub_body=body, exp_date=date)

            if self.is_long_enough(pr_ad_data.pub_body, 6) and self.is_not_past_date(pr_ad_data.exp_date):
                self.privet_ad.publish_from_data_class(pr_ad_data)       
            else:
                pr_ad_data_str = pr_ad_data.__repr__()
                self.write_involid_publications(pr_ad_data_str, 'involid data for private ad')

    def publish_sport_news(self):
        for i in range(len(self.sport_news_lst)):
            publication = self.sport_news_lst.pop(0)
            city_lst = self.return_text_blocks('city', publication) + ['']
            body_lst = self.return_text_blocks('sp_news', publication) + ['']
            date_lst = self.return_text_blocks('date', publication) + ['']
            sport_lst = self.return_text_blocks('sp_type', publication) + ['']
            city = city_lst[0]
            body = body_lst[0]
            date = date_lst[0]
            sport = sport_lst[0]

            sport_news_data = SportNewsData(city=city, pub_body=normalize_case(body), news_date=date, sport_type=sport)

            if self.is_long_enough(sport_news_data.city, 3) and self.is_long_enough(sport_news_data.pub_body, 6) and self.is_valid_date(sport_news_data.news_date, '') and self.is_long_enough(sport_news_data.sport_type, 3):
                self.sport_news.publish_from_data_class(sport_news_data)       
            else:
                sport_news_data_str = sport_news_data.__repr__()
                self.write_involid_publications(sport_news_data_str, 'involid data for sport news')

    def publish_all(self):
        self.instantinate_classes()
        self.read_from_folder()
        self.publish_news()
        self.publish_private_ad()
        self.publish_sport_news()
        self.del_class_instances()



news = News()
private_add = PrivateAd()
event_announcement = SportNews()

path = r"C:\Users\Vasili_Yaromenka\Documents\my_learning\Python_for_DQ\Vasili_Yaromenka_PyDQ\feeder_files"    
pff = PublishFromFiles(path)


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
        pff.publish_all()
    else:   
        print("Enter a valid input")

    if is_valid_input:
        p.publish_from_input()
