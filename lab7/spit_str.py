pen = '-'
pin = ['A', 'M', 'A', 'N', 'G']
print("Joining")
print(pen.join(pin))
c = pen.join(pin)
print("Splitting")
print(c.split('-'))
people = {
    'Subham': {
        'birthday': 'Aug 15'
    },
    'Saurabh': {
        'birthday': 'Mar 21'
    },
    'Krishna': {
        'birthday': 'July 7'
    },
    'Aman': {
        'birthday': 'Jan 24'
    },

    'Milan': {
        'birthday': 'May 27'
    },
    'Runak': {
        'birthday': 'Sep 7'
    },
    'Utkarsh': {
        'birthday': 'Jan 5'
    },
}
labels = {
    'birthday': 'birth date'
}
name = input("Name:")

if name in people:
    print("%s's birthdate is %s." % (name, people[name]['birthday']))
