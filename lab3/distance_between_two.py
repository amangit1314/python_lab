# Distance between two points
from cmath import sqrt

a1 = int(input("Enter the x coordinate of point A: "))
a2 = int(input("Enter the y coordinate of point A: "))
b1 = int(input("Enter the x coordinate of point B: "))
b2 = int(input("Enter the y coordinate of point B: "))
a = (a1, a2)
b = (b1, b2)
d = int(abs(sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)))
print("Distance is:", d)
