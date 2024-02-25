import random as rand

# 1) create a list of random number of dicts (from 2 to 10)

# declare an empty list to append generated dictionaries
list_of_dict = []

# declare ascii_lowercase variable instead of importing the "string" module
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'


for num in range(rand.randint(2, 10)):   # setting the len of the list from 2 to 10
    len_dct = rand.randint(1, 26)           # setting the len of the dict of the current from 1 to 26
    # for each k:v pair, choose a key randomly from ascii_lowercase and value from the range 0-100
    dct = {rand.choice(ascii_lowercase) : rand.randint(0, 100) for i in range(len_dct)}
    # append the dict to the list
    list_of_dict.append(dct)


# 2) get previously generated list of dicts and create one common dict:

# an empty dict to update
common_dict = {}

# list with all the keys in list_of_dict
key_lst = [key for dct in list_of_dict for key in dct.keys()]

for dct in list_of_dict:

    dct_keys = set(dct.keys())
    # iterate over the keys of each dict in the list
    for key in dct_keys:

        if key_lst.count(key) > 1:
            # if there are more than 1 key occurrences in all the dicts, generate the new key
            new_key = key + '_' + str(list_of_dict.index(dct)+1)
            # replace the pair with the new key and the same val
            dct[new_key] = dct.pop(key)

    # add the dict to the common_dict
    common_dict.update(dct)


# keep pair with max(val) over initially same keys; if there are >1 keys with max(val)- keep the 1st one
for key in set(key_lst):
    # if there were > 1 key initially
    if key_lst.count(key) > 1:
        # get max(val) for these keys
        max_val = max([val for k, val in common_dict.items() if key in k])  # find max(val) for the all same keys
        # delete pairs with val != max(val)
        common_dict = {k : v for k, v in common_dict.items() if key not in k or v == max_val}

        # if there are >1 keys with max(val)
        # collect them into list, sort list, and delete the 1st item
        lst_of_max_keys = [k for k in common_dict.keys() if key in k]
        lst_of_max_keys.sort()
        del lst_of_max_keys[0]

        # delete pairs with the rest of keys from the dict
        if lst_of_max_keys:
            common_dict = {k : v for k, v in common_dict.items() if key not in lst_of_max_keys}

print(common_dict)

