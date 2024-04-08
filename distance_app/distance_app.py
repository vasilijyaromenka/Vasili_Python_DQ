from distance_functoions import return_distance, is_valid_latitude, is_valid_longitude, return_distance_dct, is_valid_city
from db_functions import insert_city, select_city

while True:

    is_valid_input = False 
    while not is_valid_input:
        city_1 = input('Enter the 1st city\n').strip()
        is_valid_input = is_valid_city(city_1)
        if not is_valid_input:
            print(f"{city_1} is invalid city format")

    is_valid_input = False 
    while not is_valid_input:
        city_2 = input('Enter the 2nd city\n').strip()
        is_valid_input = is_valid_city(city_2)
        if not is_valid_input:
            print(f"{city_2} is invalid city format")


    if not select_city(city_1)['lat'] and not select_city(city_1)['long']:
        is_valid_input = False
        while not is_valid_input:
            lat = input(f"Enter <{city_1}> latitude in format 55.1234 \n").strip()
            is_valid_input = is_valid_latitude(lat)
            if not is_valid_input:
                print(f"{lat} is invalid latitude format:")

        is_valid_input = False
        while not is_valid_input:
            long = input(f"Enter <{city_1}> longitude in format 55.1234 \n").strip()
            is_valid_input = is_valid_longitude(long)
            if not is_valid_input:
                print(f"{long} is invalid latitude format:")

        insert_city(city=city_1.title(), lat=lat, long=long)


    if not select_city(city_2)['lat'] and not select_city(city_2)['long']:
        is_valid_input = False
        while not is_valid_input:
            lat = input(f"Enter <{city_2}> latitude in format 55.1234 \n").strip()
            is_valid_input = is_valid_latitude(lat)
            if not is_valid_input:
                print(f"{lat} is invalid latitude format:")

        is_valid_input = False
        while not is_valid_input:
            long = input(f"Enter <{city_2}> longitude in format 55.1234 \n").strip()
            is_valid_input = is_valid_longitude(long)
            if not is_valid_input:
                print(f"{long} is invalid latitude format:")

        insert_city(city=city_2.title(), lat=lat, long=long)


    city_1_dct = select_city(city_1)
    city_2_dct = select_city(city_2)

    distance = return_distance_dct(city_1_dct, city_2_dct)

    result = f"\nThe distance b\w {city_1.title()} and {city_2.title()} is {distance} km"
    board = '\n' + len(result) * '='

    print(f"{board}{result}{board}")

test_data = """

    Vilnius
        lat = 54.6872
        lon = 25.2797
    Minsk
        lat = 53.9006
        lon = 27.5590
    Gomel
        lat = 52.4345
        lon = 30.9754
    London 
        lat = 51.5074
        lon = -0.1278
"""