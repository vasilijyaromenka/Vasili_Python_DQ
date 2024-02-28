

class Publcation:
    def __init__(self,text) -> None:
        self.text = text
        self.pub_name = 'PubName'

    def pub_decorator(self, method):
        def wrapper(*args, **kwargs):
            print("=" * 20 + self.pub_name + "=" * 20 )
            result = method(*args, **kwargs)
            print("=" * 20 + self.pub_name + "=" * 20 )
            return result
        return wrapper

    def __pub_generator(self):
        pass

    @pub_decorator    
    def public(self):
        print(self.text) 


news = Publcation("text of publication")

news.public()