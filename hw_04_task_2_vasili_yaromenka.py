
import random as rand

# create all the needed functiuons

# func to create a dict wit a random lenth with, random keys (from letters) and rendom int-values
def random_dict(max_len = 10, max_val = 10, upper_key = False):

    ascii = 'abcdefghijklmnopqrstuvwxyz'
    if upper_key:
        ascii = ascii.upper()

    len_dct = rand.randint(1, max_len)                    # setting the len of the dict of the current from 1 to {max_len}
    dct = {rand.choice(ascii) : rand.randint(0, max_val) for i in range(len_dct)}
    
    return dct


# function for lists with dictionaries,
# to add postfix == dictionary's index+1 to each dict key
def add_index_to_keys(lst):
    for index, dct in enumerate(lst):
        keys_lst = set(dct.keys())
        for key in keys_lst:
            new_key = f"{key}_{index+1}"
            dct[new_key] = dct.pop(key)
    return lst


# func to update one dict with another one. 
# in case there are >1 keys with the same 1st char; only k:v pair with greater val goes to the final dct (or from the dct being updated, if they are equal)
def update_dict_with_max_val(dict_to_update, source_dict):
    for key_2, val_2 in source_dict.items():
        if key_2[0] in [key[0] for key in dict_to_update.keys()]:
            for key_1, val_1 in dict_to_update.copy().items():
                if key_1[0] == key_2[0] and val_2 > val_1:
                    del dict_to_update[key_1]
                    dict_to_update[key_2] = val_2
        else: 
            dict_to_update[key_2] = val_2


# function to delete postfix in a string
def delete_postfix(txt, postfix = ''):
    if '_' in txt and txt.endswith(str(postfix)):
        postfix = '_' + txt.split('_')[-1]
        txt = txt.replace(postfix, '')
    return txt

# 1) create a list of random number of dicts (from 2 to 10)

# set list length from 2 to 10
length = rand.randint(2, 10) 
# create the required list with dicts 
list_of_dict = [ random_dict(26, 100) for i in range(length) ]


# 2) get previously generated list of dicts and create one common dict:

# add posfixes to all dicts' keys
add_index_to_keys(list_of_dict)

# an empty dict to update
common_dict = {}

for dct in list_of_dict:
    update_dict_with_max_val(common_dict, dct)


# list with all the keys in the initial list_of_dict
key_lst = [key[0] for dct in list_of_dict for key in dct.keys()]


for key in common_dict.copy().keys():
    # if there was the only key with the given letter, delete the postfix 
    if key_lst.count(key[0]) == 1:
        common_dict[delete_postfix(key)] = common_dict.pop(key)


print(common_dict)

