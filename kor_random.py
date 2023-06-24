import random 
from pprint import pprint

# opening the file
file_obj = open("kor.txt", "r", encoding="utf-8")

# reading the data from the file
file_data = file_obj.read()

# splitting the file data into lines
lines = file_data.splitlines()
#print(lines)
file_obj.close()

my_set = set(lines)

def rand_kor():
    return random.sample(my_set, 3)

#pprint(random.sample(my_set, 3))