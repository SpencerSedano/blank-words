# Making a simple script that grabs text and returns a specific amount of
# blank spaces randomly

import random


with open("words.txt", "r") as lyrics:
    lyric_dict = [lyric for lyric in lyrics]
    changed_list = "".join(lyric_dict)
    split_list = changed_list.split()

    print(f"Words number: {len(split_list)}")

    numbers = random.sample(range(0, 240), 40)
    print(numbers)

    for i in sorted(numbers, reverse=True):
        del split_list[i]

    print(split_list)

# The join method joins everything into a BIG string, the \n is read and spaces are automatically made because of the join method


""" clean_list = [clean.replace("\n", "") for clean in my_list]

clean_list = list(filter(None, clean_list))

print(clean_list)
print(len(my_list)) """
