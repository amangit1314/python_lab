# Find the sum of all the even-valued

def evenFibSum(limit):
    if (limit < 2):
        return 0

    even1 = 0
    even2 = 2
    sm = even1 + even2

    while (even2 <= limit):
        even3 = 4 * even2 + even1

        if (even3 > limit):
            break

        even1 = even2
        even2 = even3
        sm = sm + even2

    return sm


limit = 4000000
print(evenFibSum(limit))
