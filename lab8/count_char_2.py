import collections
import pprint
file_input = input('File Name: ')


with open(file_input, 'r') as info:
    count = collections.Counter(info.read().upper())
    value = pprint.pformat(count)

file = open(file_input, "r")
data = file.read()
number_of_characters = len(data)
print('Number of characters in text file :', number_of_characters)

print(value)
