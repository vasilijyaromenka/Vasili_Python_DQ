import sqlite3


def create_connection(db_name = 'file_pub_db'):
    with sqlite3.connect('database_gps') as connection:
        cursor = connection.cursor()
        return cursor, connection
    

def insert_city(city, lat, long):

    cursor, connection = create_connection()

    cursor.execute("""CREATE TABLE IF NOT EXISTS city_geo (
                        city        text, 
                        latitude    text,
                        longitude   text,
                        UNIQUE (city))
                    """)

    cursor.execute(f""" INSERT OR IGNORE INTO  city_geo (city, latitude, longitude)
                        VALUES('{city}', '{lat}', '{long}')
                """)

    connection.commit()  
    cursor.close() 
    connection.close()  


def select_city(city):
    cursor, connection = create_connection()

    cursor.execute("""CREATE TABLE IF NOT EXISTS city_geo (
                        city        text, 
                        latitude    text,
                        longitude   text,
                        UNIQUE (city))
                    """)

    cursor.execute(f""" SELECT latitude, longitude
                        FROM city_geo
                        WHERE LOWER(city) = LOWER('{city}')
                        UNION ALL
                        SELECT 0, 0
                """)
    
    lat, long = cursor.fetchone() 

    connection.commit()  
    cursor.close() 
    connection.close()  

    result_dct = {'city' : city, 'lat' : float(lat), 'long' : float(long)}

    return result_dct


