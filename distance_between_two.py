# Distance between two points
a = (1, 2)
b = (4, 6)
if a[0] == b[0]:
    print("Distance is: ", abs(a[1] - b[1]))

elif a[1] == b[1]:
    print("Distance is: ", abs(a[0] - b[0]))

else:
    print("Distance is: ", abs(a[0] - b[0]) + abs(a[1] - b[1]))
