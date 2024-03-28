import sqlite3
from pub_normalize import normalize_case





def create_connection(db_name = 'file_pub_db'):
    with sqlite3.connect('file_pub_db') as connection:
        cursor = connection.cursor()
        return cursor, connection
    


def escape_args(func):
    def wrapper(*args, **kwargs):
        escaped_args = [arg.replace("'", "''") for arg in args]
        escaped_kwargs = {k: normalize_case(v.replace("'", "''")) if isinstance(v, str) else v for k, v in kwargs.items()}
        return func(*escaped_args, **escaped_kwargs)
    return wrapper


@escape_args
def insert_news(date, city, news):

    cursor, connection = create_connection()

    cursor.execute("""CREATE TABLE IF NOT EXISTS news (
                        date   date, 
                        city   text,
                        news   text,
                        UNIQUE (news, city))
                    """)

    cursor.execute(f""" INSERT OR IGNORE INTO  news (date, city, news)
                        VALUES('{date}', '{city}', '{news}')
                """)

    connection.commit()  
    cursor.close() 
    connection.close()  

@escape_args
def insert_private_ad(date, exp_date, ad):

    cursor, connection = create_connection()

    cursor.execute("""CREATE TABLE IF NOT EXISTS private_ads (
                        date        date, 
                        exp_date    date,
                        ad          text,
                        UNIQUE (ad, exp_date))
                    """)

    cursor.execute(f""" INSERT OR IGNORE INTO  private_ads (date, exp_date, ad)
                        VALUES('{date}', '{exp_date}', '{ad}')
                """)

    connection.commit()  
    cursor.close() 
    connection.close()
    

@escape_args
def insert_sport_news(date, city, sp_type, news):

    cursor, connection = create_connection()

    cursor.execute("""CREATE TABLE IF NOT EXISTS sport_news (
                        date        date, 
                        city        text,
                        sp_type     text,
                        news        text,
                        UNIQUE (city, sp_type, news))
                    """)

    cursor.execute(f""" INSERT OR IGNORE INTO  sport_news (date, city, sp_type, news)
                        VALUES('{date}', '{city}', '{sp_type}', '{news}')
                """)

    connection.commit()  
    cursor.close() 
    connection.close()  
