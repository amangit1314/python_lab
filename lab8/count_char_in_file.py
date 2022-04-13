# Count no of characters in a file by open it
from collections import Counter
file = open("questions.txt", "r")

# read the content of file
data = file.read()

# get the length of the data
number_of_characters = len(data)
# print(os.path.basename("lab/txt"))

print('Number of characters in text file :', number_of_characters)


file = open('questions.txt', 'r')

s = ''
for each in file:
    s = s + each

print(s)

c = Counter(s)
count = 0
for each in c.elements():
    count += 1

print(count)
