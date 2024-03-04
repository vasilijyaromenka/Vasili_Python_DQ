import textwrap
from datetime import datetime, timedelta
import re


class Publcation:
    def __init__(self):
        self.pub_name = self.__class__.__name__
        self.length = 70 # max line length
        self.file_path = r"C:\Users\Vasili_Yaromenka\***\feed.txt"
        self.post_txt = None # to reassign with the user input

    def input_text(self):
        post_text = input("Input your post text: ")
        if len(post_text) <= 10:
            raise Exception("Your publication must have more than sympols")
        self.post_txt = post_text

    def pub_end(self):
        pub_end = ''
        return pub_end


    def __pub_generator(self):
        text = self.post_txt

        llen = self.length 
        # split class name into space separated words
        head_words = re.findall(r'[A-Z][a-z]*', self.pub_name)
        pub_name = ' '.join(head_words)

        # place pub_name in the senter of the header and wrap it into '---'
        spaces = int((70 - len(pub_name))/2)
        header = f"{llen * '-' }\n{spaces * ' ' + pub_name }\n{llen * '-'}\n  "

        # fit post text into the feed length
        pub_lines =  textwrap.wrap(text, width=llen) 
        pub_txt = ("\n".join(pub_lines)).capitalize()

        result = f"{header}\n{pub_txt}\n\n{self.pub_end()}"
        return result
 
    def publish(self):
        self.input_text() # reassign post text
        post = self.__pub_generator()
        with open(self.file_path, 'a') as file:
            file.write(post)
        
        print(f"Your post is pulicated: \n{post}")


class News(Publcation):
    def __init__(self):
        super().__init__()
        self.city = None

    def input_city(self):
        city = input("Enter your city: ")
        if len(city) <= 2:
            raise Exception("City name must have min 3 letters")
        self.city = city

    def pub_end(self):
        current_date = datetime.now().strftime('%Y-%m-%d  %H:%M')
        pub_end = f"{self.city.capitalize()}, {current_date}."
        return pub_end
    
    def publish(self):
        self.input_city()
        try:
            super().publish()
        except Exception as e:
            print(f"Caught an exception: {e}")



class PrivateAd(Publcation):
    def __init__(self):
        super().__init__()
        self.exp_date = None

    def input_date(self):
        date = input("Enter add expiration date in format 'YYYY-MM-DD': ")
        self.exp_date = date

    def days_left(self):

        try:
            expiration_date = datetime.strptime(self.exp_date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")
        current_date = datetime.now()
        days_left = (expiration_date - current_date).days
        if days_left < 0:
            raise Exception("End date cannot be in the past")
        
        return days_left
                
    def pub_end(self):
        pub_end = f"Actual until: {self.exp_date}, {self.days_left()} days left."
        return pub_end
    
    def publish(self):
        self.input_date()
        try:
            super().publish()
        except Exception as e:
            print(f"Caught an exception: {e}")




class EventAnnouncement(PrivateAd, News):
    def __init__(self):
        super().__init__()   

    def pub_end(self):
        pub_end = f"The event will occur in {self.city.capitalize()} on {self.exp_date}, {self.days_left()} days left."
        return pub_end
    


pub_type = int(input("Choose your publication type: 1-News, 2 - Private Ad, 3 - Event Announcement\nEnter 1-3:"))

if pub_type == 1:
    p = News()
elif pub_type == 2:
    p = PrivateAd()
elif pub_type == 3:
    p = EventAnnouncement()

p.publish()
