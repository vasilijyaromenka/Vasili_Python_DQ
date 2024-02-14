import random

# 1)create list of 100 random numbers from 0 to 1000

rand_100 = random.sample(range(0, 1001), 100)
rand_t = rand_100

# 2)sort list from min to max with bubble sort

n = len(rand_100)
# iterate over all elements except the last one, that'll be already sorted
for i in range(n - 1):
    # traverse the array from 0 to n - i - 1
    for j in range(0, n - i - 1):
        # swap if the element is > than the next element
        if rand_100[j] > rand_100[j + 1]:
            rand_100[j], rand_100[j + 1] = rand_100[j + 1], rand_100[j]

# 3)calculate average for even and odd numbers

# create two lists with even and odd nums
evens_lst = [i for i in rand_100 if i % 2 == 0]
odds_lst = [i for i in rand_100 if i % 2 != 0]


# function to calculate average number of array
def average(array):
    if len(array) == 0:
        return None
    else:
        return sum(array) / len(array)


# apply the function to the lists
even_avg = round(average(evens_lst), 1)
odd_avg = round(average(odds_lst), 1)

# 4)print both average result in console

print(f"Average for even numbers - {even_avg}")
print(f"Average for odd numbers - {odd_avg}")
