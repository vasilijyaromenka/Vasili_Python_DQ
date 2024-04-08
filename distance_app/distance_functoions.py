import math

def return_distance(lat1, lon1, lat2, lon2):

    # radius of the earth in kilometers
    R = 6371.0

    # convert degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # differences in coordinates
    delta_lat = lat2_rad - lat1_rad
    delta_lon = lon2_rad - lon1_rad

    # haversine formula
    a = math.sin(delta_lat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c
    return round(distance)


def return_distance_dct(dct_1, dct_2):
    lat1 = dct_1['lat']
    lon1 = dct_1['long']
    lat2 = dct_2['lat']
    lon2 = dct_2['long']

    distance = return_distance(lat1, lon1, lat2, lon2)
    return distance



def is_valid_latitude(lat):

    precision = len(str(lat).split('.')[-1])
    if precision != 4:
        return False
    
    lat = float(lat)
    if not isinstance(lat, float) or lat < -90 or lat > 90:
        return False
    
    return True

def is_valid_longitude(lon):
    
    precision = len(str(lon).split('.')[-1])
    if precision != 4:
        return False
    
    lon = float(lon)
    if not isinstance(lon, float) or lon < -180 or lon > 180:
        return False
    
    return True

def is_valid_city(city):

    for i in city.replace(' ',''):
        if not i.isalpha():
            return False
    
    if len(city) <2:
        return False
    
    return True

