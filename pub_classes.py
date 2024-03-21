import textwrap
from datetime import datetime, date
import re
from abc import ABC, abstractmethod
import re
import os 
import sys
from pub_data_classes import *



# sys.path.append("/path/to/your/module/hw_04_task_3_vasili_yaromenka")
from hw_04_task_3_vasili_yaromenka import normalize_case

class Publcation:
    def __init__(self):
        self.pub_name = self.__class__.__name__
        self.length = 70 # max line length
        self.file_path = r"feed.txt"
        self.pub = None

    
    # def user_input(self, text_comment = ""):
    #     return input(text_comment)

    def set_pub_body(self):
        is_valid_input = False
        while not is_valid_input:
            pub_body = input("Enter your publication text. Minimum 6 characters: \n")
            if len(pub_body) >= 6:
                is_valid_input = True
            else:
                print('Too short!')
        return pub_body


    @abstractmethod
    def pub_end(self):
        pass


    def pub_generator(self):
        llen = self.length 
        pub_end = self.pub_end()
        pub_body = self.pub.pub_body

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


    def publish_data(self, data_instance):
        self.pub = data_instance
        post = self.pub_generator()
        self.write_to_file(post)
        return post

    @abstractmethod
    def publish_from_input(self):
        pass

        
        
        


class News(Publcation):
    def __init__(self):
        super().__init__()

    def set_news_date(self):
        news_date_str = input("Enter news date (YYYY-MM-DD) or leave empty for current date:\n")  
        if news_date_str == "":
            is_valid_input = True
        else:
            is_valid_input = False
            while not is_valid_input:                
                try:
                    news_date = datetime.strptime(news_date_str, '%Y-%m-%d').date()
                    is_valid_input = True
                except ValueError:
                    print("Invalid date format. Use 'YYYY-MM-DD'.")     
        return news_date_str


    def set_city(self):
        is_valid_input = False
        while not is_valid_input:
            city = input("Enter the city. Minimum 3 characters:\n")
            if len(city) >= 3:
                is_valid_input = True
            else:
                print('Too short!')
        return city


    def pub_end(self):
        pub_city = self.pub.pub_city.title()
        pub_date = self.pub.pub_date
        pub_end = f"{pub_city}, {pub_date}."
        return pub_end
    
    def publish_from_input(self):
        in_city = self.set_city()
        in_date = self.set_news_date()
        in_body = self.set_pub_body()
        news = NewsData(pub_city=in_city, pub_date=in_date, pub_body=in_body)
        
        post = self.publish_data(news)
        self.write_to_file(post)      
        print(f"Your post has been published: \n{post}")    
        print(self.length * '-') 



class PrivateAd(Publcation):
    def __init__(self):
        super().__init__()

    def set_exp_date(self):
        is_valid_input = False
        while not is_valid_input:
            exp_date_str = input("Enter expirational date(YYYY-MM-DD):\n")
            try:
                exp_date = datetime.strptime(exp_date_str, '%Y-%m-%d').date()
            except ValueError:
                print("Invalid date format. Please use 'YYYY-MM-DD'.")
            else:
                days_left = (exp_date - datetime.now().date()).days
                if days_left >= 0:
                        is_valid_input = True
                else:
                    print("End date cannot be in the past")

        return exp_date_str

 
    def pub_end(self):
        exp_date = self.pub.exp_date    
        days_left = self.pub.days_left
        if days_left == 0:
            pub_end = f"Actual until: {exp_date}, expires today."
        else:
            pub_end = f"Actual until: {exp_date}, {days_left} days left."
        return pub_end
    
    def publish_from_input(self):
        in_exp_date = self.set_exp_date()
        in_body = self.set_pub_body()
        private_add = PrivateAddData(exp_date=in_exp_date, pub_body=in_body)
        
        post = self.publish_data(private_add)
        self.write_to_file(post)      
        print(f"Your post has been published: \n{post}")    
        print(self.length * '-') 
    



class SportNews(News):
    def __init__(self):
        super().__init__()


    def set_sport_type(self):
        is_valid_input = False
        while not is_valid_input:
            sport = input("Enter the sport type. Minimum 3 characters:\n")
            if len(sport) >= 3:
                is_valid_input = True
            else:
                print('Too short!')
        return sport

    def pub_end(self):
        sport_type = self.pub.sport_type.title()
        city = self.pub.pub_city.title()
        news_date = self.pub.pub_date
        pub_end = f"{sport_type} news, {city}, {news_date}."
        return pub_end

    
    def publish_from_input(self):
        in_sport = self.set_sport_type()
        in_city = self.set_city()
        in_date = self.set_news_date()
        in_body = self.set_pub_body()
        sport_news = SportNewsData(sport_type=in_sport, pub_city=in_city, pub_date=in_date, pub_body=in_body)
        
        post = self.publish_data(sport_news)
        self.write_to_file(post)      
        print(f"Your post has been published: \n{post}")    
        print(self.length * '-') 



