import textwrap
from datetime import datetime, date
import re
from abc import ABC, abstractmethod


class Publcation:
    def __init__(self):
        self.pub_name = self.__class__.__name__
        self.length = 70 # max line length
        self.file_path = r"feed.txt"

    
    def user_input(self, text_comment = ""):
        return input(text_comment)

    def pub_body(self):
        is_valid_input = False
        while not is_valid_input:
            print("Enter your publication text. Minimum 6 characters:")
            pub_body = self.user_input()
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
        pub_body = self.pub_body()

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
    
    
    def write_to_file(self):
        post = self.pub_generator()
        try:
            with open(self.file_path, 'a') as file:
                file.write(post)
        except IOError as e:
            print(f"An error occurred while writing to the file: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")   

        print(f"Your post has been published: \n{post}")    
        print(self.length * '-')


    #@abstractmethod
    def publish(self):
        self.write_to_file()
        
        
        


class News(Publcation):
    def __init__(self):
        super().__init__()


    def city(self):
        is_valid_input = False
        while not is_valid_input:
            city = self.user_input("Enter the city. Minimum 3 characters:")
            if len(city) >= 3:
                is_valid_input = True
            else:
                print('Too short!')
        return city.capitalize()


    def pub_end(self):
        city = self.city()
        current_date = datetime.now().strftime('%Y-%m-%d  %H:%M')
        pub_end = f"{city}, {current_date}."
        return pub_end
    




class PrivateAd(Publcation):
    def __init__(self):
        super().__init__()
        self.exp_date = None
        self.days_left = None


    def check_exp_date(self):
        is_valid_input = False
        while not is_valid_input:
            exp_date_str = self.user_input("Enter expirational date(YYYY-MM-DD):")
            try:
                exp_date = datetime.strptime(exp_date_str, '%Y-%m-%d').date()
                is_valid_input = True
            except ValueError:
                raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")            
        self.exp_date = exp_date
    

    def days_left_calc(self):
        self.check_exp_date()

        days_left = (self.exp_date - date.today()).days
        if days_left < 0:
            raise Exception("End date cannot be in the past")
        
        self.days_left = days_left
                

    def pub_end(self):
        self.days_left_calc()
        if self.exp_date == datetime.now():
            pub_end = f"Actual until: {self.exp_date}, expires today."
        else:
            pub_end = f"Actual until: {self.exp_date}, {self.days_left} days left."
        return pub_end
    



class SportNews(News):
    def __init__(self):
        super().__init__()   

    def sport_type(self):
        is_valid_input = False
        while not is_valid_input:
            sport = self.user_input("Enter the sport type. Minimum 3 characters:")
            if len(sport) >= 3:
                is_valid_input = True
            else:
                print('Too short!')
        return sport.capitalize()

    def pub_end(self):
        current_date = datetime.now().strftime('%Y-%m-%d  %H:%M')
        city = self.city()
        sport = self.sport_type()
        pub_end = f"{sport} news, {city}, {current_date}."
        return pub_end




news = News()
private_add = PrivateAd()
event_announcement = SportNews()

is_valid_input = False

while not is_valid_input:
    pub_type = input("Choose your publication type - \n1-News, 2 - Private Ad, 3 - Event Announcement\nEnter 1-3:")
    if pub_type == '1':
        p = news
        is_valid_input = True
    elif pub_type == '2':
        p = private_add
        is_valid_input = True
    elif pub_type == '3':
        p = event_announcement
        is_valid_input = True
    else:   
        print("Enter a valid input")


p.publish()

